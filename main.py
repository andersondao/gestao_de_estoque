nome_produto = str(input("Digite o nome do produto: "))
sku = str(input("Digite o SKU do produto: "))
quantidade_estoque = int(input("Digite a quantidade do produto em estoque: "))
preco_unitario = float(input("Digite o preço unitário do produto: "))

print("\n ---Produto adicionado---")
print(f"Nome: {nome_produto}")
print(f"SKU: {sku}")
print(f"Quantidade: {quantidade_estoque}")
print(f"Preço R$: {preco_unitario:.2f}")

if quantidade_estoque <= 10:
    print("Estoque baixo")
elif quantidade_estoque <= 20:
    print("Estoque crítico")
else:
    print("Adequado")