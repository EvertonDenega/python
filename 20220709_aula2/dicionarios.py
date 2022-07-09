"""
DICIONÁRIOS:
- estruturas de dados em formato 'chave:valor' que podem armazenar qualquer tipo de dado inclusive outros dicionarios.
São:
- Iteráveis, podem ser usados dentro de laço 'for'
- Indexáveis, o índice é uma string/chave
- Mutáveis, podem ser alterado
- Heterogêneos. Podem armazenar diversos dados.
"""


if __name__ == '__main__':

    # Criando um dicionário
    info = {}
    info = {
        "nome": "Curso de Python",
        "turma": "20220702",
        "Módulo": "Fundamentos",
        "notas": [5, 6, 7]
            }

    info = dict()
    info = dict(
        nome="Curso de Python",
        turma="20220702",
        modulo="Fundamentos",
        notas=[5, 6, 7],
        mais_info=dict(obs="")
    )
    print(info)

    # dicionarios são indexaveis. Indicamos o nome da chave para acessar o valor e alterar.
    print(info["turma"])
    info["turma"] = "20220802"
    print(info["turma"])

    # o método get() retorna o valor associado à chave. Se não existir, retorna o valor none.
    # podemos definir um valor padrao a ser retornado caso a chave não exista.
    print(info.get("batata", "A chave não existe"))
    print(info["turma"])

    # Dicionários são mutáveis, pode adicionar/remover chaves e alterar valores associados à chave:
    # criando chave 'Localização:
    info["Localização"] = "Blumenau"
    print(info)

    # Método setdefault() retorna o valor associado à chave. Se a chave nao existir, ele cria.
    print(info.setdefault("sala", "black"))
    print(info)

    # Método update() atualiza o par chave-valor do dicionário.
    info.update({"sala": "yellow", "periodo": "agosto"})
    print(info)
    print("="*100)
    # Dicionários são interáveis. Podem ser processados em um laço 'for'
    # por padrão, em um laço for, são retornadas as chaves desse dicionário.
    # tambem podemos explicitar o retorno das chaves utilizando o método .keys()
    for item in info:
        print(item)

    for item in info.keys():
        print(item)

    for value in info.values():
        print(value)

    # o método items() retorna uma lista d etplas com chaves e valores.
