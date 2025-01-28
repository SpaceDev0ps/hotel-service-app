from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import db, User, ServiceOrder
import os
import sys
import locale

# ========== CONFIGURAÇÕES INICIAIS ==========
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hotel123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024  # 2MB

# Forçar codificação UTF-8
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# ========== INICIALIZAÇÃO DE EXTENSÕES ==========
db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ========== CRIAÇÃO DO ADMIN ==========
def create_admin():
    with app.app_context():
        if not User.query.filter_by(username='admin').first():
            admin = User(
                name='Administrador',
                username='admin',
                role='admin'
            )
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()

# ========== ROTAS ========== (MANTIDAS COMO ANTES)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and user.check_password(request.form['password']):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Usuário ou senha incorretos')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if User.query.filter_by(username=request.form['username']).first():
            flash('Nome de usuário já existe!')
            return redirect(url_for('register'))
        
        new_user = User(
            name=request.form['name'],
            username=request.form['username'],
            role=request.form['role'],
            room=request.form.get('room')
        )
        new_user.set_password(request.form['password'])
        db.session.add(new_user)
        db.session.commit()
        flash('Cadastro realizado! Faça login.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def dashboard():
    if current_user.role == 'guest':
        orders = ServiceOrder.query.filter_by(guest_id=current_user.id).all()
    elif current_user.role == 'staff':
        orders = ServiceOrder.query.filter_by(status='pending').all()
    else:
        orders = ServiceOrder.query.all()    
    return render_template('dashboard.html', orders=orders)

@app.route('/create', methods=['POST'])
@login_required
def create_order():
    if current_user.role != 'guest':
        flash('Apenas hóspedes podem criar ordens!')
        return redirect(url_for('dashboard'))
    
    photo = None
    if 'photo' in request.files:
        file = request.files['photo']
        if file.filename != '':
            filename = f"order_{ServiceOrder.query.count() + 1}_{file.filename}"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            photo = filename
    
    new_order = ServiceOrder(
        category=request.form['category'],
        description=request.form['description'],
        priority=request.form['priority'],
        guest_id=current_user.id,
        photo=photo
    )
    db.session.add(new_order)
    db.session.commit()
    flash('Ordem criada com sucesso!')
    return redirect(url_for('dashboard'))

@app.route('/complete/<int:order_id>')
@login_required
def complete_order(order_id):
    if current_user.role not in ['staff', 'admin']:
        flash('Apenas funcionários podem completar ordens!')
        return redirect(url_for('dashboard'))
    
    order = ServiceOrder.query.get(order_id)
    order.status = 'completed'
    order.assigned_to = current_user.id
    db.session.commit()
    flash('Ordem marcada como concluída!')
    return redirect(url_for('dashboard'))

# ========== INICIALIZAÇÃO DO APP ==========
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        create_admin()
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    
    # Modificação crucial para resolver o erro:
    app.run(host='0.0.0.0', port=5000, debug=True)  # <--- LINHA CORRIGIDA