"""
Exercício 26 - Reajuste por faixa salarial
Módulo 02 - Estruturas Condicionais

Enunciado:
Leia o salário atual e calcule o novo salário conforme a tabela de
reajuste.

Requisito:
Mostre o percentual aplicado, o valor do aumento e o novo salário.

Regras do exercício:
Até R$ 1.500,00                        -> 15%
De R$ 1.500,01 até R$ 3.000,00         -> 10%
Acima de R$ 3.000,00                   -> 5%
"""

salario_atual = float(input("Salário atual: "))

if salario_atual <= 1500:
    percentual = 15
elif salario_atual <= 3000:
    percentual = 10
else:
    percentual = 5

aumento = salario_atual * percentual / 100
novo_salario = salario_atual + aumento

print(f"Percentual: {percentual}%")
print(f"Aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")
