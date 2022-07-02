"""
Operadores matemáticos
+ (soma)
- (subtração)
/ (divisão)
* (multiplicação)
% (módulo)
** (exponencial)

Operadores de comparação
> (maior que)
< (menor que)
>= (maior ou igual)
<= (menor ou igual)
== (igual a)
!= (diferente de)

Operadores lógicos
or (OU)
and (E)
not (NÃO)

Estruturas de decisão (if... elif... else...)
if True = executa o bloco de código
elif
else
"""

if __name__ == "__main__":
    pass

nota1 = float(input("Informe a 1ª nota: "))
nota2 = float(input("Informe a 2ª nota: "))
nota3 = float(input("Informe a 3ª nota: "))
media = float((nota1 + nota2 + nota3) / 3)
if media >= 7:
    resultado = "Aprovado"
elif media >= 5 and media < 7:
    resultado = "em recuperação"
else:
    resultado = "Reprovado"
# formatando a saída para mostrar apenas 1 cada depois da vírgula (.1f)
print(f"A média do aluno é {media:.1f}. Resultado: {resultado}.")