"""
Exercício 28 - É possível formar um triângulo?
Módulo 02 - Estruturas Condicionais

Enunciado:
Leia três medidas positivas e informe se elas podem formar um
triângulo.

Regra:
Três lados formam um triângulo quando cada lado é menor que a soma
dos outros dois.

Exemplo de execução:
Lados: 3, 4 e 5
Resultado: FORMAM UM TRIÂNGULO
"""

a = float(input("Primeiro lado: "))
b = float(input("Segundo lado: "))
c = float(input("Terceiro lado: "))

if a < b + c and b < a + c and c < a + b:
    print("Resultado: FORMAM UM TRIÂNGULO")
else:
    print("Resultado: NÃO FORMAM UM TRIÂNGULO")
