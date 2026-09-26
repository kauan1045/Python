"""
Exercício 27 - Classificação de IMC
Módulo 02 - Estruturas Condicionais

Enunciado:
Leia o peso em quilogramas e a altura em metros. Calcule o IMC e
classifique o resultado usando apenas as regras didáticas da tabela.

Regra:
IMC = peso / (altura * altura)

Regras do exercício:
IMC < 18,5                     -> ABAIXO DA FAIXA
18,5 <= IMC < 25,0              -> FAIXA NORMAL
25,0 <= IMC < 30,0               -> ACIMA DA FAIXA
IMC >= 30,0                      -> FAIXA ELEVADA

Exemplo de execução:
Peso: 72 kg
Altura: 1,80 m
IMC: 22,2
Classificação: FAIXA NORMAL
"""

peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = peso / (altura * altura)

if imc < 18.5:
    classificacao = "ABAIXO DA FAIXA"
elif imc < 25.0:
    classificacao = "FAIXA NORMAL"
elif imc < 30.0:
    classificacao = "ACIMA DA FAIXA"
else:
    classificacao = "FAIXA ELEVADA"

print(f"IMC: {imc:.1f}")
print(f"Classificação: {classificacao}")
