# EXERCÍCIO FOLHA DE PGTO
# mostrar o salário do funcionário de acordo com o tipo de funcionar que está sendo processado.
# Temos 3 tipos:
# CLT -> valor salário fixo
# TERCEIRIZADO -> horas trabalhadas X o valor das horas
# COMISSIONADO -> salário é porcentagem do valor das vendas realizadas. Considerar % livremente.

if __name__ == "__main__":
    pass

print("CÁLCULO DE SALÁRIO")
tipo_funcionario = input("Informe o tipo de funcionário: CLT ou TERCEIRIZADO ou COMISSIONADO: ").upper()
salario = 0

if tipo_funcionario == 'CLT':
    salario = int((input("Informe o valor do salário CLT: ")))

elif tipo_funcionario == 'TERCEIRIZADO':
    horas = int((input("Informe o número de horas trabalhadas: ")))
    valor_horas = int((input("Informe o valor pago por hora: ")))
    salario = horas * valor_horas

elif tipo_funcionario == 'COMISSIONADO':
    vendas = int((input("Informe o total de vendas do funcionário: ")))
    comissao = int((input("Informe o percentual de comissão do funcionário (sem o %): ")))
    salario = (vendas * comissao) / 100

else:
    (print("Tipo de funcionário não encontrado. Digitar CLT ou TERCEIRIZADO ou COMISSIONADO"))

if salario > 0:
    print(f"O salário do funcionário {tipo_funcionario} é de {salario:.2f}")