"""
Exercício 17 - Par ou ímpar
Módulo 02 - Estruturas Condicionais

Enunciado:
Leia um número inteiro e informe se ele é par ou ímpar.

Regra:
Um número é par quando o resto da divisão por 2 é igual a zero.

Exemplo de execução:
Digite um número: 18
Resultado: PAR
"""

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    resultado = "PAR"
else:
    resultado = "ÍMPAR"

print(f"Resultado: {resultado}")
