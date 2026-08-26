salarioFixo = float(input("Digite seu salário fixo:"))
totalVendido = float(input("Digite Total vendido:"))

comissao = totalVendido * 0.04
salarioTotal = salarioFixo + comissao

print(f"Comissão:{comissao:.2f}\n"
      f"Salário total:{salarioTotal:.2f}")