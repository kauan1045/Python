"""
Exercício 31 - Divisível por 3 e por 5
Módulo 02 - Estruturas Condicionais

Enunciado:
Leia um número inteiro e informe em qual situação ele se encontra.

Regras do exercício:
Divisível por 3 e por 5   -> DIVISÍVEL POR 3 E 5
Apenas por 3               -> DIVISÍVEL APENAS POR 3
Apenas por 5                -> DIVISÍVEL APENAS POR 5
Por nenhum dos dois          -> NÃO DIVISÍVEL POR 3 NEM 5

Exemplo de execução:
Entrada: 30 -> DIVISÍVEL POR 3 E 5
"""

numero = int(input("Digite um número: "))

divisivel_3 = numero % 3 == 0
divisivel_5 = numero % 5 == 0

if divisivel_3 and divisivel_5:
    resultado = "DIVISÍVEL POR 3 E 5"
elif divisivel_3:
    resultado = "DIVISÍVEL APENAS POR 3"
elif divisivel_5:
    resultado = "DIVISÍVEL APENAS POR 5"
else:
    resultado = "NÃO DIVISÍVEL POR 3 NEM 5"

print(f"Resultado: {resultado}")
