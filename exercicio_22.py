"""
Exercício 22 - Situação do aluno por faixa
Módulo 02 - Estruturas Condicionais

Enunciado:
Leia duas notas, calcule a média e informe a situação do aluno
conforme a tabela.

Regras do exercício:
Média < 5,0                    -> REPROVADO
5,0 <= Média < 7,0              -> RECUPERAÇÃO
Média >= 7,0                    -> APROVADO

Exemplo de execução:
Nota 1: 5,5
Nota 2: 6,5
Média: 6,0
Situação: RECUPERAÇÃO
"""

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2) / 2

if media < 5.0:
    situacao = "REPROVADO"
elif media < 7.0:
    situacao = "RECUPERAÇÃO"
else:
    situacao = "APROVADO"

print(f"Média: {media}")
print(f"Situação: {situacao}")
