#Sistema de Gestão de Estoque

def adicionar_produto(nome, sku, qtd, preco):
    
    estoque.append({"nome": nome, "sku": sku, "qtd": qtd, "preco": preco})
    print("\n ---Produto adicionado---")
    print(f"Nome: {nome}")
    print(f"SKU: {sku}")
    print(f"Quantidade: {qtd}")
    print(f"Preço R$: {preco:.2f}")

def listar_produtos():
    if not estoque:
        print("Estoque vazio.")
        return
    print("\n---Produtos em Estoque---")
    for produto in estoque:
        print(f"SKU:{produto['sku']}, Nome:{produto['nome']}, Quantidade:{produto['qtd']}, Preço: R${produto['preco']:.2f}")

def atualizar_quantidade(estoque, sku_procurado, nova_qtd):
    encontrado = False
    for produto in estoque:
        if produto['sku'] == sku_procurado:
            produto['qtd'] = nova_qtd
            encontrado = True
            print(f"Quantidade do produto {sku_procurado} atualizada para {nova_qtd}.")
            break
    if not encontrado:
        print(f"Produto com SKU '{sku_procurado}' não encontrado")

estoque = []

while True:
    print("\n--- Sistema de Gestão de Estoque ---")
    print("1. Adicionar Produto")
    print("2. Listar Produtos")
    print("3. Atualizar Quantidade")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        sku = str(input("Digite o SKU do produto: "))
        nome = str(input("Digite o nome do produto: "))
        qtd = int(input("Digite a quantidade do produto em estoque: "))
        preco = float(input("Digite o preço unitário do produto: "))
        adicionar_produto(sku, nome, qtd, preco)
        continue
    elif opcao == '2':
        listar_produtos()
        continue
    elif opcao == '3':
        sku_procurado = input("Digite o SKU procurado: ")
        nova_qtd = input("Digite a nova quantidade: ")
        atualizar_quantidade(estoque, sku_procurado, nova_qtd)
        continue
    elif opcao == '4':
        print("Saindo do sistema. Até mais!")
        break 
    else:
        print("Opção inválida. Tente novamente.") 
