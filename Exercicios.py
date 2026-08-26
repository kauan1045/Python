#Apresentação da calculadora 
print("# Calculadora de Soma")
# Tratamento de erro 
try:
#Entrada de número fornecido pelo usuario 
    pNumero = float(input("Digte o primeiro número:"))
    sNumero = float(input("Digte o segundo número:"))
# Nome do erro como valor que desejo que ele retorne, quando desparar o erro 
except ValueError:
    print("Valor incorreto")
#Realização da soma dos dois valores fornecidos pelo usuario
Soma = sNumero + pNumero
#Resultado final
print(f"Soma dos valores:{Soma}")