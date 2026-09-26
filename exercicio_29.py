"""
Exercício 29 - Tipo de triângulo
Módulo 02 - Estruturas Condicionais

Enunciado:
Leia três medidas. Primeiro verifique se elas formam um triângulo.
Se formarem, classifique-o como equilátero, isósceles ou escaleno.

Regras do exercício:
Três lados iguais    -> EQUILÁTERO
Dois lados iguais     -> ISÓSCELES
Três lados diferentes -> ESCALENO

Exemplo de execução:
Lados: 5, 5, 5 -> EQUILÁTERO
Lados: 1, 2, 3 -> NÃO FORMA TRIÂNGULO
"""

a = float(input("Primeiro lado: "))
b = float(input("Segundo lado: "))
c = float(input("Terceiro lado: "))

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        tipo = "EQUILÁTERO"
    elif a == b or a == c or b == c:
        tipo = "ISÓSCELES"
    else:
        tipo = "ESCALENO"
    print(f"Resultado: {tipo}")
else:
    print("Resultado: NÃO FORMA TRIÂNGULO")
