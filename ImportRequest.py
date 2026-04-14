import requests

url = 'http://127.0.0.1:5000/alunos'

# O seu JSON vira um dicionário no Python
meu_payload = {
  "nome": "João da Silva",
  "data_nascimento": "2025-01-20",
  "email": "joao@escola.com",
  "cpf": "123.456.789-00",
  "telefone": "(11) 99999-9999",
  "sexo": "Masculino",
  "naturalidade": "Palmas-TO"
}


resposta = requests.post(url, json=meu_payload)

