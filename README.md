# FakePinterest

Clone simples do Pinterest focado em cadastro, login e upload de fotos pelo usuário.

## Descrição

FakePinterest é um projeto web feito com Flask que permite criar conta, fazer login e postar imagens. O usuário pode visualizar seu perfil com as fotos enviadas, além de navegar pelo feed geral com as imagens de todos os usuários. Interface responsiva com upload de imagens e segurança básica via Flask-Login e bcrypt.

## Tecnologias usadas

- Python 3.x
- Flask (Flask-Login, Flask-WTF, SQLAlchemy)
- Jinja2 (templates HTML)
- SQLite (via SQLAlchemy)
- HTML, CSS (Grid e Flexbox)
- Werkzeug para upload seguro de arquivos
- Bcrypt para hash de senha

## Funcionalidades

- Cadastro de usuários com validação e hash de senha
- Login e logout com sessão segura
- Upload de fotos com proteção contra nomes inseguros
- Visualização do perfil com lista de fotos postadas
- Feed público com as fotos mais recentes de todos usuários
- Validação e exibição de erros nos formulários

## Como rodar localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/Lucas-1234567890/fakePinterest-Flask
   cd fakePinterest
    ```

## Requisitos
- Python 3.8+
- Pip
- Biblioteca Flask e extensões
- Pasta para upload configurada com permissão de escrita

## Estrutura de pastas
- /templates — arquivos HTML com Jinja2

- /static/css — folhas de estilo CSS

- /static/fotos_post — uploads de imagens

- fakePinterest — código Python (app, models, forms)

- requirements.txt — dependências do projeto

## Autor
Lucas Amorim Porciuncula

## Licença
Este projeto é open source. Sinta-se livre para usar e modificar.


