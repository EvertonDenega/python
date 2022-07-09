"""
TUPLAS:
- estruturas de dados que podem tambem ser chamadas de containeres (estruturas que armazenam outros dados)
São:
- Iteráveis,
- Indexáveis
- Imutáveis
- Heterogêneas. Podem armazenar diversos dados.
"""


if __name__ == '__main__':

    tpl = ("Banana", "Maçã",)

    # Tuplas são Iteráveis
    for item in tpl:
        print(item)

    # Tuplas são Indexáveis
        print(tpl[1])

    # Tuplas são Imutáveis
    try:
        # esta linha causara um type error
        tpl[1] = "Batata"
    except Exception:
        print("Não pode fazer isso")

    # Tuplas são Heterogêneas, armazenam diversos tipos de items inclusive outras tuplas.
    tpl2 = ("Nome", 23, [5 ,6, 7], (2, 3))
    print(tpl2)