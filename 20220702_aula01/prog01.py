# entrada e saída via terminal

"""
utilizamos 2 funcoes bulti-in do python quando queremos mostrar e ler informacoes do terminal
print() -> Imprime uma mensagem na tela. Recebe uma expressao válida do python e retornar para o terminal.
input() -> Recebe uma informação do teclado. Os dados capturados pelo teclado são tipo STR.
"""


# string multi-linha
"""
: (dois pontos) = novo bloco de código
Cada bloco de cód precisa ter uma identação de 4 caracteres.
"""

if __name__ == "__main__":
    pass    # ignora a linha (é comentário)

    print("Olá")
    # python é dinamicamente topaca, ou seja, não precisamos deinir o tipo de uma variável no momento da criação.
    # python altera o tipo de variável de forma automatica se novo valor for atribuído.
    soma = 2 + 2
    print(soma)

    # = -> operador de atribuição
    idade = int(input("Informe a sua idade: "))

    # converter o valor da variável idade para tipo numérico
    # OU idade = int(idade)
    # OU idade(input("Informe a sua idade: "))

    # podemos montar uma string de 2 maneiras: format() ou f-strings

    print("sua idade é {}".format(idade))
    nova_idade = 10 + idade
    print(f"sua nova idade é {nova_idade}")
