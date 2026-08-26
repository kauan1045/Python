#Entrada de dados
salarioAtual = float(input("Salário atual:"))
#Caculo
aumento= salarioAtual * 0.15
novoSalario  = salarioAtual + aumento
#Retorno - usando :.2f para mostrar 2 casas depois do ponto
print(f"Amuento: R$ {aumento}\n"
    f"Novo salário: R$ {novoSalario:.2f}")