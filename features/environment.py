from API_ import API_Escola , db


def before_all(context):
    
    context.client = API_Escola.test_client()

def before_scenario(context, scenario):
    
    with API_Escola.app_context():
        db.drop_all()   
        db.create_all() 

def after_scenario(context, scenario):

    with API_Escola.app_context():
        db.session.remove()