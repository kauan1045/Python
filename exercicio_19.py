"""
Exercício 19 - Maior e menor de três números
Módulo 02 - Estruturas Condicionais

Enunciado:
Leia três números reais e mostre o maior e o menor valor informado.

Requisito:
O programa deve funcionar também quando houver valores repetidos.

Exemplo de execução:
Valores: 8, 15, 4
Maior: 15
Menor: 4
"""

a = float(input("Primeiro valor: "))
b = float(input("Segundo valor: "))
c = float(input("Terceiro valor: "))

maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c

menor = a
if b < menor:
    menor = b
if c < menor:
    menor = c

print(f"Maior: {maior}")
print(f"Menor: {menor}")
