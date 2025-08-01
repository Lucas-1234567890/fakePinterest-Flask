from fakePinterest import database, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(usuario_id):
    return Usuario.query.get(int(usuario_id))

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String(100), nullable=False)
    email = database.Column(database.String(100), unique=True, nullable=False)
    senha = database.Column(database.String(100), nullable=False)
    fotos = database.relationship('Foto', backref='usuario', lazy=True)

    def get_id(self):
        return self.id
    

class Foto(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String(200),default='default.png')
    data_criacao = database.Column(database.DateTime, default=datetime.utcnow())
    usuario_id = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
