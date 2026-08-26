
try:
    precoProduto = float(input("Preço:"))
except ValueError:
    print("Não é possivel calcular letras")
desconto  = precoProduto * 0.1
precoFinal = precoProduto - desconto

print(f"Desconto: R$ {desconto:.2f}\n"
      f"Preço final: R$ {precoFinal:.2f}")