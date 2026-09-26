"""
Exercício 35 - Valor do ingresso
Módulo 02 - Estruturas Condicionais

Enunciado:
O ingresso custa R$ 30,00. Leia a idade e informe se a pessoa é
estudante. Calcule o valor final conforme as regras.

Regra:
Paga meia-entrada quem tiver menos de 12 anos, quem for estudante ou
quem tiver 60 anos ou mais. O desconto é de 50% e não é acumulativo.

Exemplo de execução:
Idade: 20
Estudante: SIM
Valor do ingresso: R$ 15,00
"""

PRECO_CHEIO = 30.00

idade = int(input("Idade: "))
estudante = input("Estudante (SIM/NÃO): ").strip().upper()

tem_desconto = idade < 12 or estudante == "SIM" or idade >= 60

if tem_desconto:
    valor = PRECO_CHEIO * 0.50
else:
    valor = PRECO_CHEIO

print(f"Valor do ingresso: R$ {valor:.2f}")
