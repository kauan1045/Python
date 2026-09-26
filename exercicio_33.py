"""
Exercício 33 - Dia da semana
Módulo 02 - Estruturas Condicionais

Enunciado:
Leia um número de 1 a 7 e mostre o dia da semana correspondente.
Para qualquer outro valor, mostre OPÇÃO INVÁLIDA.

Exemplo de execução:
Entrada: 1 -> SEGUNDA-FEIRA
Entrada: 9 -> OPÇÃO INVÁLIDA
"""

numero = int(input("Digite um número de 1 a 7: "))

dias = {
    1: "SEGUNDA-FEIRA",
    2: "TERÇA-FEIRA",
    3: "QUARTA-FEIRA",
    4: "QUINTA-FEIRA",
    5: "SEXTA-FEIRA",
    6: "SÁBADO",
    7: "DOMINGO",
}

resultado = dias.get(numero, "OPÇÃO INVÁLIDA")
print(f"Resultado: {resultado}")
