"""
Exercicio 2
Dada uma sequencia randomica de letras e numeros, criar um programa que consiga diferenciar
essas letras e numeros, com as regras a seguir:
1. ao final do programa mostrar uma lista com os números que fazem parte da string
- mostrar tambem a soma deses números.

2. mostrar uma lista com as letras que fazem parte desta string.
- Entre estas letras, mostrar quais são vogais e quais são consoantes

Ex. hf6f5568da
Lista números: [6, 5, 5, 6, 8]. Utilizar a função sum()
Soma dos números: [30] sum(lista_numeros)
Lista letras: hffda
vogais: [a]
consoantes: [h, f, f, d]

dica: utilizar funcao isdigit
"""

from random import choices
from string import ascii_lowercase, digits

if __name__ == '__main__':
    # o método de string JOIN junta uma lista de itens em uma string, separando pelo caractere
    string_randomica = ''.join(choices(f"{ascii_lowercase}{digits}", k=50))
    print(string_randomica)
    lista_numeros = []
    lista_letras = []
    vogais = "aeiou"
    lista_vogais = []
    lista_consoantes = []

    # números
    for caractere in string_randomica:
        if caractere.isdigit():
            lista_numeros.append(int(caractere))
        else:
            lista_letras.append(caractere)
            if caractere in vogais:
                lista_vogais.append(caractere)
            else:
                lista_consoantes.append(caractere)

    print(f"Lista de números: {lista_numeros}")
    print(f"A soma dos números é: {sum(lista_numeros)}")
    print(f"Lista das letras: {lista_letras}")
    print(f"Lista das Vogais: {lista_vogais}")
    print(f"Lista das Consoantes: {lista_consoantes}")
