"""
Exercício 34 - Quantidade de dias do mês
Módulo 02 - Estruturas Condicionais

Enunciado:
Leia o número de um mês e um ano. Mostre quantos dias o mês possui.

Regra:
Meses 1, 3, 5, 7, 8, 10 e 12 possuem 31 dias.
Meses 4, 6, 9 e 11 possuem 30 dias.
Fevereiro possui 28 dias, ou 29 em ano bissexto.

Requisito:
Se o mês estiver fora de 1 a 12, mostre MÊS INVÁLIDO.

Exemplo de execução:
Mês: 2, Ano: 2024 -> 29 dias
Mês: 13, Ano: 2026 -> MÊS INVÁLIDO
"""

mes = int(input("Mês: "))
ano = int(input("Ano: "))

bissexto = ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)

if mes in (1, 3, 5, 7, 8, 10, 12):
    dias = 31
    print(f"{dias} dias")
elif mes in (4, 6, 9, 11):
    dias = 30
    print(f"{dias} dias")
elif mes == 2:
    dias = 29 if bissexto else 28
    print(f"{dias} dias")
else:
    print("MÊS INVÁLIDO")
