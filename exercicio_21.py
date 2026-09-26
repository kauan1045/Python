"""
Exercício 21 - Aprovado ou reprovado
Módulo 02 - Estruturas Condicionais

Enunciado:
Leia duas notas, calcule a média e informe se o aluno foi aprovado
ou reprovado.

Regra:
Média maior ou igual a 7,0 significa APROVADO.
Abaixo de 7,0 significa REPROVADO.

Exemplo de execução:
Nota 1: 8,0
Nota 2: 6,0
Média: 7,0
Situação: APROVADO
"""

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2) / 2

if media >= 7.0:
    situacao = "APROVADO"
else:
    situacao = "REPROVADO"

print(f"Média: {media}")
print(f"Situação: {situacao}")
