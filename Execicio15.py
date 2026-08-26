uPreco = float(input("Preço Unitário:"))
qtd  = int(input("Quantidade:"))
frete = float(input("Frente:"))

subTotal = uPreco * qtd
total = subTotal + frete

print(f"Subtotal: R$ {subTotal:.2f}\n"
      f"Total: R$ {total:.2f}")