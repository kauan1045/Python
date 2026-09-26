"""
Exercício 32 - Número dentro do intervalo
Módulo 02 - Estruturas Condicionais

Enunciado:
Leia um número real e informe se ele está dentro do intervalo
fechado de 10 até 20.

Regra:
Os valores 10 e 20 pertencem ao intervalo (intervalo fechado).

Exemplo de execução:
Entrada: 10 -> DENTRO
Entrada: 20,1 -> FORA
"""

numero = float(input("Digite um número: "))

if 10 <= numero <= 20:
    resultado = "DENTRO"
else:
    resultado = "FORA"

print(f"Resultado: {resultado}")
