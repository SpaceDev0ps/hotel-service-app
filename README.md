🏨 Hotel Service App
Um sistema completo para gerenciamento de solicitações de serviços em hotéis, desenvolvido com Flask, SQLAlchemy e Flask-Login. Permite que hóspedes criem solicitações, funcionários as atendam e administradores gerenciem o sistema.

🚀 Funcionalidades
Autenticação de Usuários:

Registro e login para hóspedes, funcionários e administradores.

Controle de acesso baseado em roles (admin, staff, guest).

Solicitações de Serviço:

Hóspedes podem criar solicitações (limpeza, manutenção, room service, etc.).

Anexo de fotos opcional.

Prioridade (baixa, média, alta) e status (pendente, em andamento, concluído).

Dashboard Dinâmico:

Visualização de solicitações conforme o tipo de usuário.

Funcionários veem apenas solicitações pendentes.

Administradores têm acesso completo.

Banco de Dados SQLite:

Armazenamento seguro de usuários e solicitações.

Criação automática do banco de dados e tabelas.

🛠️ Tecnologias Utilizadas
Backend:

Python 3.8+

Flask (Framework Web)

SQLAlchemy (ORM para banco de dados)

Flask-Login (Autenticação de usuários)

Frontend:

HTML5 + Bootstrap 5 (Interface responsiva)

CSS3 (Estilos personalizados)

Banco de Dados:

SQLite (Banco de dados embutido)

📋 Pré-requisitos
Python 3.8 ou superior

Pip (Gerenciador de pacotes do Python)

Git (Opcional, para controle de versão)

🛠️ Instalação

    Clone o repositório:
git clone https://github.com/seu-usuario/hotel-service-app.git
cd hotel-service-app

    Crie um ambiente virtual (recomendado):
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

    Instale as dependências:
pip install -r requirements.txt

    Configure o banco de dados:
python -c "from app import app, db; with app.app_context(): db.create_all()"

    Execute o aplicativo:
python app.py

Acesse no navegador:

Abra http://localhost:5000.

👤 Contas para Teste
Administrador:

Usuário: admin

Senha: admin123

Hóspede:

Crie uma conta com role "guest".

Funcionário:

Crie uma conta com role "staff".

🖼️ Screenshots
Página de Login
Login Page

Dashboard
Dashboard

Nova Solicitação
New Order

    📂 Estrutura do Projeto

hotel-service-app/
├── app.py               # Aplicativo principal
├── models.py            # Definição do banco de dados
├── requirements.txt     # Dependências do projeto
├── static/              # Arquivos estáticos (CSS, imagens)
│   ├── style.css
│   └── uploads/
└── templates/           # Templates HTML
    ├── base.html
    ├── dashboard.html
    ├── login.html
    └── register.html



📝 Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

🤝 Contribuição
Contribuições são bem-vindas! Siga os passos abaixo:

Faça um fork do projeto.

Crie uma branch para sua feature (git checkout -b feature/nova-feature).

Commit suas alterações (git commit -m 'Adiciona nova feature').

Push para a branch (git push origin feature/nova-feature).

Abra um Pull Request.

📧 Contato
Autor: Marcos Cardoso

Email: contato@spacedevops.com.br

GitHub: github.com/SpaceDev0ps
