"""
listas:
- estruturas de dados que podem tambem ser chamadas de containeres (estruturas que armazenam outros dados)
- São: mutáveis, ordenáveis e heterogêneas (podem armazenar diversos tipos de dados, inclusive outras listas)
dicionário
tuplas:
"""

if __name__ == '__main__':
    pass

    # sintaxe de criação de listas
    carros = ["Gol", "Marea", "Parati"]
    print(carros)

    # Inserindo novo carro no final da lista
    carros.append("Vectra")
    print(carros)

    """
    carros = ['Gol', 'Marea', 'Kombi', 'Parati', 'Vectra']
    índice      0       1       2           3       4
    índic neg. -5       -4      -3          -2         -1                
    """

    # Inserindo um novo carro no índice 2 da lista. Índices começam em Zero na esquerda.
    carros.insert(2, "Kombi")
    print(carros)

    # Como índices são indexáveis, conseguimos acessar um determinado item a partir do índice.
    print(carros[2])

    # Podemos utilizar índices negativos. Índices negativos iniciam em -1 na direita.
    print(carros[-2])

    # O Python tambem permite fatiar (slice) listas, definindo o índice de ínicio, fim e 'step'
    # ou seja, de quantos em quantos itens.

    # Isso é uma lista comprehension (maneira mais enxuta de criar listas)
    lista = [numero for numero in range(1000)]
    print(lista)

    nova_lista = lista[100:120] #slice de sequencia de 100 a 120.
    print(nova_lista)

    nova_lista = lista[100:120:2] #slice de sequencia de 100 a 120 de 2 em 2
    print(nova_lista)

    # Gera uma nova lista começando do índice 0 até 19 de 1 em 1.
    nova_lista = lista[:20]
    print(nova_lista)

    # Gera uma nova lista começando do índice 500 até [-1] de 1 em 1
    nova_lista = lista[500:]
    print(nova_lista)

    # Gera uma cópia da lista criada
    nova_lista = lista[:]
    print(nova_lista)

    """
    lista[i:f:s]
    i = índice inicial
    f = índice final
    s = step (de quantos em quantos)
    Este parâmetros não são obrigatórios. 
    Se omitir o i será gerada uma lista iniciando em 0 até f.
    Se omitir o f será gerada uma lista iniciando em i até lista -1. (último item)
    Se omitir o s será gerada uma lista em sequencia de 1.
    
    O índice final é exclusivo, ele não é retornado. Ao invés disso, o item retornado é o (índice final - 1)
    """

    # copiando listas. Maneira INCORRETA (ficam com a mesma id)
    lista_de_compras1 = ["Sabão", "Banana", "Tomate"]
    lista_de_compras2 = lista_de_compras1
    lista_de_compras2.append("Batata")
    print(lista_de_compras1)
    print(lista_de_compras2)

    # Maneira correta de copiar os valores de uma lista para outra
    lista_de_compras2 = lista_de_compras1.copy()
    lista_de_compras3 = lista_de_compras1[:]

    lista_de_compras2.append("cerveja")
    print(lista_de_compras1)
    print(lista_de_compras2)
    print(lista_de_compras3)
    pass