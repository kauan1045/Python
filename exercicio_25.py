"""
Exercício 25 - Preço conforme a forma de pagamento
Módulo 02 - Estruturas Condicionais

Enunciado:
Leia o preço de um produto e a opção de pagamento. Calcule e mostre
o valor final conforme a tabela.

Regras do exercício:
1 - Dinheiro ou Pix   -> 10% de desconto
2 - Débito            -> 5% de desconto
3 - Crédito à vista   -> sem alteração
4 - Crédito parcelado -> 8% de acréscimo

Exemplo de execução:
Preço: 200,00
Opção: 1
Valor final: R$ 180,00
"""

preco = float(input("Preço: "))
opcao = int(input("Opção: "))

if opcao == 1:
    valor_final = preco * 0.90
elif opcao == 2:
    valor_final = preco * 0.95
elif opcao == 3:
    valor_final = preco
elif opcao == 4:
    valor_final = preco * 1.08
else:
    valor_final = None

if valor_final is None:
    print("OPÇÃO INVÁLIDA")
else:
    print(f"Valor final: R$ {valor_final:.2f}")
