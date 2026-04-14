from behave import given, when, then
from datetime import datetime
from PySQLconfig import db , Aluno , Disciplina
from API_ import API_Escola


# Teste para A Tabela de Alunos


@given('Novo aluno {nome} , {data_de_nascimento} ,{e_mail} , {CPF} , {telefone} , {sexo} , {naturalidade}')
def step_impl(context , nome , data_de_nascimento ,e_mail , CPF , 
              telefone , sexo , naturalidade): 
    context.dados_alunos= {
        "nome":nome,
        "data_de_nascimento":datetime.strptime(data_de_nascimento, '%Y-%m-%d').date(),
        "e_mail":e_mail,
        "cpf":CPF,
        "telefone": telefone,
        "sexo": sexo,
        "naturalidade": naturalidade,
    }

@when('requisicao para API')
def step_impl(context): 
    novo_aluno = Aluno(**context.dados_alunos)
    
    with API_Escola.app_context():
        db.session.add(novo_aluno)
        db.session.commit()
        context.aluno_criado_id = novo_aluno.id

@then('enviar para o Banco')
def step_impl(context):

    with API_Escola.app_context():
        # Agora a consulta vai funcionar!
        aluno_no_db = Aluno.query.filter_by(id=context.aluno_criado_id).first()

    assert aluno_no_db is not None

    assert aluno_no_db.nome == context.dados_alunos["nome"]



@given('Receber um {Indice} numerico do Id do banco para remover')
def step_impl(context , Indice):
     context.indice = Indice
     

@when('Usar o request de remover aluno')
def step_impl(context):
        context.indice_id = int(context.indice)

        with API_Escola.app_context():
        
            Aluno_Remove = Aluno.query.get(context.indice_id)
        
        
        if Aluno_Remove is not None:
            db.session.delete(Aluno_Remove)
            db.session.commit()

@then('o id onde o aluno estava deve ser vaziu')
def step_impl(context):
     
     with API_Escola.app_context():
         
        Aluno_Remove = Aluno.query.get(context.indice_id)
    
        assert   Aluno_Remove is None , f"Erro: A Aluno com ID {context.indice_id} ainda está no banco!"


