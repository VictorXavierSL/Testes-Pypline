from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Disciplina(db.Model):
    __tablename__ = 'disciplinas'
    
    id = db.Column(db.Integer, primary_key=True)
    Titulo = db.Column(db.String(100), nullable=False)
    data_inicial = db.Column(db.Date, nullable=False)
    data_final = db.Column(db.Date, nullable=False)
    numero_vagas = db.Column(db.Integer, default=0)
    materia_verao = db.Column(db.Boolean, default=False) # True ou False

  
    
class Aluno(db.Model):
    __tablename__ = 'alunos'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    data_de_nascimento = db.Column(db.Date, nullable=False)
    e_mail = db.Column(db.String(100), unique=True, nullable=False)
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    telefone = db.Column(db.String(20))
    sexo = db.Column(db.String(20))
    naturalidade = db.Column(db.String(50))

  

