"""
Exercício 16 - Positivo, negativo ou zero
Módulo 02 - Estruturas Condicionais

Enunciado:
Leia um número real e informe se ele é positivo, negativo ou igual a zero.

Exemplo de execução:
Digite um número: -7
Resultado: NEGATIVO
"""

numero = float(input("Digite um número: "))

if numero > 0:
    resultado = "POSITIVO"
elif numero < 0:
    resultado = "NEGATIVO"
else:
    resultado = "ZERO"

print(f"Resultado: {resultado}")
