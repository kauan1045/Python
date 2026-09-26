"""
Exercício 24 - Ano bissexto
Módulo 02 - Estruturas Condicionais

Enunciado:
Leia um ano inteiro e informe se ele é bissexto.

Regra:
Um ano é bissexto quando é divisível por 400, ou quando é divisível
por 4 e não é divisível por 100.

Exemplo de execução:
Ano: 2024
Resultado: ANO BISSEXTO
"""

ano = int(input("Ano: "))

if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    resultado = "BISSEXTO"
else:
    resultado = "NÃO BISSEXTO"

print(f"Resultado: {resultado}")
