# --- INICIALIZAÇÃO ---
# Criamos uma lista vazia que servirá como nosso banco de dados de produtos
estoque = []

# --- LOOP DE CADASTRO ---
while True:
    # Pergunta se o usuário quer continuar, padronizando a resposta para comparação
    continuar = input('Deseja cadastrar um novo produto? (S/N) ').strip().title()
    
    # Condição de parada: se for diferente de "S", o loop encerra
    if continuar != "S":
        break
    
    # --- COLETA E TRATAMENTO DE DADOS ---
    produto = input('Digite o nome do produto: ').strip().title()
    
    # Tratamos a vírgula para evitar erro na conversão para float
    preco = input('Digite o preço do produto: ').replace(',', '.')
    preco = float(preco)
    
    qtd = int(input('Digite a quantidade do produto: '))
    
    # Cálculo do valor total deste item específico
    valor_total = preco * qtd
    
    # --- ESTRUTURA DE DADOS ---
    # Organizamos as informações do produto atual em um dicionário
    item = {
        'Produto': produto, 
        'Preço': preco, 
        'Quantidade': qtd, 
        'Valor total': valor_total 
    }
    
    # Adicionamos o dicionário (item) na nossa lista global (estoque)
    estoque.append(item)

# --- RELATÓRIO FINAL ---
print('\n========== RELATÓRIO DE ESTOQUE ==========')

# Variável acumuladora para somar o valor de todo o inventário
valor_final = 0

# Percorremos a lista de dicionários para exibir cada produto
for item in estoque:
    # Exibição formatada com 2 casas decimais no valor total
    print(f"PRODUTO: {item['Produto']} | PREÇO UN: R$ {item['Preço']:.2f} | QTD: {item['Quantidade']} | TOTAL: R$ {item['Valor total']:.2f}")
    
    # Somamos o valor do item atual ao montante total
    valor_final += item['Valor total']

# --- FINALIZAÇÃO ---
print('-' * 50)
print(f'VALOR TOTAL DO INVENTÁRIO: R$ {valor_final:.2f}')
