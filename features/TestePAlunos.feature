# language: pt

Funcionalidade: teste de Banco de dados

    Esquema do Cenário: salvar dados no Banco
    Dado Novo aluno <nome> , <data_de_nascimento> ,<e_mail> , <CPF> , <telefone> , <sexo> , <naturalidade>
    Quando requisicao para API
    Então enviar para o Banco

    Exemplos: 
        | nome            | data_de_nascimento | e_mail              | CPF             |telefone             |  sexo                |naturalidade         |
        |João da Silva    |2025-01-20          |joao@escola.com      | 123.456.789-00  |(11) 99999-9999      | Masculino            |Palmas-TO            |
        |João da Silva    |2045-01-20          |joao@escola.com      | 123.456.789-00  |(11) 99999-9999      | Masculino            |Palmas-TO            |
        |João da Silva    |2025-01-20          |joao@escola.com      | 123.458.789-00  |(11) 99999-9999      | Masculino            |Palmas-TO            |
        |João da Silva    |0001-01-20          |joao@escola.com      | 000.000.000-00  |(11) 999999999       | Masculino            |Palmas-TO            |
        |João da Silva    |0099-01-20          |joao@escola.com      | 123.450.789-00  |(11) 99999-9999      | Masculino            |Palmas-TO            |

    Esquema do Cenário: Remover Alunos do Banco
    Dado Receber um <Indice> numerico do Id do banco para remover
    Quando Usar o request de remover aluno
    Então o id onde o aluno estava deve ser vaziu
    Exemplos: 
        |Indice| 
        |7     | 
        |1     | 
        |5     | 
        |1     | 

