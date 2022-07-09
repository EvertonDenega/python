"""
A partir de uma sequencia de número, salvar em duas listas.
# Uma lista com números positivos e outra negativos.
Utilizar funcao range

# se o numero for impar, salvar na lista de ímpar.
# se for par, salvar na lista de par.

# mostrar qual é a lista com mais números
# se houver empate, mostrar que é empate
# Dica: usar built-in (len)

"""

from random import randint

if __name__ == '__main__':
    pass

    # a funcao range gera números ate um limite estabelecido

    lista_pares = []
    lista_impares = []

    for i in range(100):
        numero = randint(0, 1000)

        resultado = numero % 2
        if resultado == 1:
            lista_pares.append(numero)
        else:
            lista_impares.append(numero)

    print(lista_pares)
    print(lista_impares)

    if len(lista_pares) > len(lista_impares):
        print(f"Foram sorteado mais números PARES. São {len(lista_pares)} itens")
    elif len(lista_pares) < len(lista_impares):
        print(f"Foram sorteado mais números ÍMPARES. São {len(lista_impares)} itens")
    else:
        print(f"As lista possuem a mesma quantidade de números - {len(lista_impares)}")