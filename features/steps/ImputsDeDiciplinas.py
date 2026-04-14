from behave import given, when, then
from datetime import datetime
from PySQLconfig import db , Aluno , Disciplina
from API_ import API_Escola

@given('imput do Usuario {Titulo} , {dataInicial} , {DataFinal} , {NumeroDeVagas} e {MateriaDeVerao}')
def step_impl(context , Titulo , dataInicial ,DataFinal , NumeroDeVagas , MateriaDeVerao): 
    
    if MateriaDeVerao == "S": 
            MateriaDeVerao = True
    else: 
            MateriaDeVerao = False
    context.dados_Disciplina= {
        "Titulo":Titulo,
        "data_inicial":datetime.strptime(dataInicial, '%Y-%m-%d').date(),
        "data_final":datetime.strptime(DataFinal, '%Y-%m-%d').date(),
        "numero_vagas":NumeroDeVagas,
        "materia_verao": MateriaDeVerao
    }

@when('usar a funcao de adicioanr novos dados')
def step_impl(context): 
    novo_Disciplina = Disciplina(**context.dados_Disciplina)
    
    with API_Escola.app_context():
        db.session.add(novo_Disciplina)
        db.session.commit()
        context.Disciplina_criado_id = novo_Disciplina.id

@then('adicionar um nova Materia')
def step_impl(context):

    with API_Escola.app_context():
   
        Disciplina_no_db = Disciplina.query.filter_by(id=context.Disciplina_criado_id).first()

    assert Disciplina_no_db is not None

    assert Disciplina_no_db.Titulo == context.dados_Disciplina["Titulo"]

@given('imput do Usuario {Indice}')
def step_impl(context , Indice):
     context.indice = Indice


     
@when('usar a funcao de remover Materia')
def step_impl(context):
        context.indice_id = int(context.indice)

        with API_Escola.app_context():
        
            Diciplina_Remove = Disciplina.query.get(context.indice_id)
        
        
        if Diciplina_Remove is not None:
            db.session.delete(Diciplina_Remove)
            db.session.commit()

@then('A materia deve ser removida')
def step_impl(context):
     
     with API_Escola.app_context():
         
        Diciplina_Remove = Disciplina.query.get(context.indice_id)
    
        assert   Diciplina_Remove is None , f"Erro: A matéria com ID {context.indice_id} ainda está no banco!"