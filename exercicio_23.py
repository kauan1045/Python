"""
Exercício 23 - Categoria de votação
Módulo 02 - Estruturas Condicionais

Enunciado:
Leia a idade de uma pessoa e informe a categoria de votação conforme
as regras didáticas da tabela.

Regras do exercício:
Menor de 16 anos   -> NÃO PODE VOTAR
16 ou 17 anos      -> VOTO OPCIONAL
18 a 69 anos       -> VOTO OBRIGATÓRIO
70 anos ou mais    -> VOTO OPCIONAL

Exemplo de execução:
Idade: 15
Resultado: NÃO PODE VOTAR
"""

idade = int(input("Idade: "))

if idade < 16:
    categoria = "NÃO PODE VOTAR"
elif idade <= 17:
    categoria = "VOTO OPCIONAL"
elif idade <= 69:
    categoria = "VOTO OBRIGATÓRIO"
else:
    categoria = "VOTO OPCIONAL"

print(f"Resultado: {categoria}")
