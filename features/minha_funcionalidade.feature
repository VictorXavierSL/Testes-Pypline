# language: pt

Funcionalidade: teste de Banco de dados

    Esquema do Cenário: Adicionar Materias
    Dado imput do Usuario <Titulo> , <dataInicial> , <DataFinal> , <NumeroDeVagas> e <MateriaDeVerao>
    Quando usar a funcao de adicioanr novos dados
    Então adicionar um nova Materia

    Exemplos: 
        |Titulo       |dataInicial    |DataFinal    |NumeroDeVagas  |MateriaDeVerao  |
        |  Materia X  | 2010-12-26    | 2011-02-26  | 10            | N              |
        |  Materia 7  | 2010-12-26    | 2011-02-26  | 7             | S              |


    Esquema do Cenário: Remover Materias
    Dado imput do Usuario <Indice>
    Quando usar a funcao de remover Materia
    Então A materia deve ser removida

    Exemplos: 
        |Indice|
        |  1   |
        |  0   |

