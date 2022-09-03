
def ex01(texto):
    """
    Exercício 01
    Escreva uma função que receba um texto qualquer e organize as letras deste texto em ordem alfabética.

    Escreva também 2 testes unitários para esta função.
    1o teste: retornar exatamente a string em ordem alfabética (caminho feliz)
    2o teste: capturar excessão caso o usuário passe um valor diferente de string

    Crie o módulo tests/test_exercicios.py
    Crie a classe TestExercicios que contem os testes unitários dos exercícios.

    Dica: converta a string para uma lista antes de ordenar as letras por ordem alfabética
    Dica: converta novamente esta lista para a string já com a ordenação
    """
    if isinstance(texto, str):
        lista_letras = list(texto)
        lista_letras.sort()
        return "".join(lista_letras)

    raise Exception("Você deve passar um tipo string para a função.")

