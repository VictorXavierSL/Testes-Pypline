from flask import Flask, request, jsonify
from PySQLconfig import db, Aluno , Disciplina
from datetime import datetime

API_Escola = Flask(__name__)


API_Escola.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///escola.db'
API_Escola.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(API_Escola)


with API_Escola.app_context():
    db.create_all()


@API_Escola.route('/alunos', methods=['POST'])
def cadastrar_aluno():
    dados = request.get_json()
    
    try:

        data_nasc = datetime.strptime(dados['data_nascimento'], '%Y-%m-%d').date()
        
        novo_aluno = Aluno(
            nome=dados['nome'],
            data_nascimento=data_nasc,
            email=dados['email'],
            cpf=dados['cpf'],
            telefone=dados.get('telefone'),
            sexo=dados.get('sexo'),
            naturalidade=dados.get('naturalidade')
        )
        
        db.session.add(novo_aluno)
        db.session.commit()
        
        return jsonify({"mensagem": "Aluno cadastrado!", "id": novo_aluno.id}), 201
    
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

@API_Escola.route('/Disciplina', methods=['POST'])
def cadastrar_Disciplina():
    dados = request.get_json()
    
    try:

        data_inicial = datetime.strptime(dados['data_inicial'], '%Y-%m-%d').date()
        data_final = datetime.strptime(dados['data_inicio'], '%Y-%m-%d').date()
        Tipo_de_Disciplina = dados['data_inicial']
        vagas_Int = int(dados['numero_vagas'])
        
        if Tipo_de_Disciplina == "S": 
            Tipo_de_Disciplina = True
        else: 
            Tipo_de_Disciplina = False

        novo_Disciplina = Disciplina(
            titulo=dados['titulo'],
            data_inicial=data_inicial,
            data_final=data_final,
            Vagas=vagas_Int,
            telefone=dados.get('telefone'),
            Disciplina_verao=Tipo_de_Disciplina,
            
        )
        
        

        db.session.add(novo_Disciplina)
        db.session.commit()
        
        return jsonify({"mensagem": "Diciplina cadastrada!", "id": Disciplina.id}), 201
    
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

@API_Escola.route('/DeletarDiciplina', methods=['DELETE'])
def apagar_materia():
    dados = request.get_json()
    try:

        indice_id =  int(dados['DeletarDiciplina'])
        Diciplina_Remove = Disciplina.query.get(indice_id)
        
        if Diciplina_Remove is None:
            return jsonify({"erro": "Materia nao encontrada"}), 404
        
        db.session.delete(Diciplina_Remove)
        db.session.commit()

        return jsonify({"mensagem": "Materia removida com sucesso!"}), 200
    except Exception as e: 
        return jsonify({"erro": str(e)}), 400
    
@API_Escola.route('/DeletarAlunos', methods=['DELETE'])
def apagar_Alunos():
    dados = request.get_json()
    try:

        indice_id =  int(dados['DeletarAlunos'])
        Alunos_Remove = Disciplina.query.get(indice_id)
        
        if Alunos_Remove is None:
            return jsonify({"erro": "Materia nao encontrada"}), 404
        
        db.session.delete(Alunos_Remove)
        db.session.commit()

        return jsonify({"mensagem": "Alunos removido com sucesso!"}), 200
    except Exception as e: 
        return jsonify({"erro": str(e)}), 400




if __name__ == '__main__':
    API_Escola.run(debug=True)