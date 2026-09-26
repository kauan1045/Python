"""
Exercício 18 - Maior de dois números
Módulo 02 - Estruturas Condicionais

Enunciado:
Leia dois números reais e mostre qual deles é o maior. Se os valores
forem iguais, informe que não existe maior.

Exemplo de execução:
Primeiro valor: 12
Segundo valor: 7
Maior valor: 12
"""

valor1 = float(input("Primeiro valor: "))
valor2 = float(input("Segundo valor: "))

if valor1 > valor2:
    print(f"Maior valor: {valor1}")
elif valor2 > valor1:
    print(f"Maior valor: {valor2}")
else:
    print("VALORES IGUAIS")
