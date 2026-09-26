"""
Exercício 20 - Três valores em ordem crescente
Módulo 02 - Estruturas Condicionais

Enunciado:
Leia três números inteiros e mostre os valores em ordem crescente.

Requisito:
Aceite valores repetidos.

Exemplo de execução:
Valores: 9, 2, 5
Ordem crescente: 2, 5, 9
"""

a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))

valores = [a, b, c]

for i in range(len(valores)):
    for j in range(len(valores) - 1 - i):
        if valores[j] > valores[j + 1]:
            valores[j], valores[j + 1] = valores[j + 1], valores[j]

print(f"Ordem crescente: {valores[0]}, {valores[1]}, {valores[2]}")
