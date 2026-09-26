"""
Exercício 30 - Aprovação de empréstimo
Módulo 02 - Estruturas Condicionais

Enunciado:
Leia o valor de um imóvel, o salário mensal do comprador e o prazo
de pagamento em anos. Calcule a prestação mensal e informe se o
empréstimo foi aprovado.

Regra:
Prestação = valor do imóvel / (anos * 12)
O empréstimo é aprovado quando a prestação não ultrapassa 30% do
salário.

Requisito:
Mostre o valor da prestação e o limite de 30% do salário.

Exemplo de execução:
Valor do imóvel: 180000,00
Salário: 6000,00
Prazo: 30 anos
Prestação: R$ 500,00
Limite: R$ 1.800,00
Resultado: APROVADO
"""

valor_imovel = float(input("Valor do imóvel: "))
salario = float(input("Salário: "))
prazo_anos = int(input("Prazo (anos): "))

prestacao = valor_imovel / (prazo_anos * 12)
limite = salario * 0.30

if prestacao <= limite:
    resultado = "APROVADO"
else:
    resultado = "NEGADO"

print(f"Prestação: R$ {prestacao:.2f}")
print(f"Limite: R$ {limite:.2f}")
print(f"Resultado: {resultado}")
