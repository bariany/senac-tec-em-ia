#instalar o conector do MySQL
# pip install mysql-connector-python
#essa biblioteca permitira que o python e mysql se comuniquem

import mysql.connector
conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'lojatech'
)

if conexao.is_connected():
    print('Conexão realizada com sucesso!')

cursor = conexao.cursor(
    dictionary=True
)

cursor.execute(
    'SELECT * FROM produtos;'

)
produtos = cursor.fetchall()
print(produtos)


cursor.execute(
    'SELECT nome, preco_venda, preco_custo FROM produtos;'

)
produtos = cursor.fetchall()
for produto in produtos:
    diferenca = produto['preco_venda'] - produto['preco_custo']

    print(produto['nome'])
    
    print(f'Preço de custo R$ {produto['preco_custo']}')

    print(f'Preço de venda R$ {produto['preco_venda']}')

    print(f'Diferença: R$ {diferenca}')

    print('------------')
          

# Qual produto possui maior preço de venda
maior_preco = 0

for produto in produtos:
    if produto['preco_venda'] > maior_preco:
        maior_preco = produto ['preco_venda']
        produto_maior_preco = produto['nome']

print(f'Produto com maior preço: {produto_maior_preco}')
print(f'Preço R$ {maior_preco}') 

# Quantidade total de unidades vendidas

cursor.execute(
    'SELECT status, valor FROM pagamentos;'

)
pagamentos = cursor.fetchall()

quantidade_total = 0

for pagamento in pagamentos:
    if pagamento['status'] == 'APROVADO':
        quantidade_total = quantidade_total + pagamento['valor']

print(f'Quantidade total: {quantidade_total}')



cursor.close()
conexao.close()

#######*EXERCICIOS*######

#1. Conecte ao banco
conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'lojatech'
)

if conexao.is_connected():
    print('Conexão realizada com sucesso!')

cursor = conexao.cursor(
    dictionary=True
)

#2. Liste todos os produtos
cursor.execute(
'SELECT * FROM  produtos;'
)

produtos = cursor.fetchall()
print(produtos)

#3. Mostre nome e preço de venda
cursor.execute(
'SELECT nome,preco_venda FROM  produtos;'
)

produtos = cursor.fetchall()
print(produtos)

#4. Identifique p produto mais caro
maior_preco = 0

for produto in produtos:
    if produto['preco_venda'] > maior_preco:
        maior_preco = produto ['preco_venda']
        produto_maior_preco = produto['nome']

print(f'Produto com maior preço: {produto_maior_preco}')
print(f'Preço R$ {maior_preco}') 

#5. Identifique o produto mais barato
menor_preco = float('inf')

for produto in produtos:
    if produto['preco_venda'] < menor_preco:
        menor_preco = produto['preco_venda']
        produto_menor_preco = produto['nome']

print(f'Produto com menor preço: {produto_menor_preco}')
print(f'Preço R$ {menor_preco}')

#6. Calcule a diferença entre preço de custo e preço de venda 
cursor.execute(
    'SELECT nome, preco_venda, preco_custo FROM produtos;'

)
produtos = cursor.fetchall()
for produto in produtos:
    diferenca = produto['preco_venda'] - produto['preco_custo']
    
    print(f"Produto: {produto['nome']}")
    print(f"Diferença: R$ {diferenca}")

#7. Conte quantos produtos foram retornados
produtos = cursor.fetchall()
quantidade_produtos = len(produtos)

print(f'Quantidade de produtos retornados: {quantidade_produtos}')

#8. Busque os registros da tabela itens_pedido
cursor.execute('SELECT * FROM itens_pedido')
itens_pedido = cursor.fetchall()
print(itens_pedido)

#9. Some todas as quatidade de vendas
total_quantidade = sum(item['quantidade'] for item in itens_pedido)

print(f'Total de produtos vendidos: {total_quantidade}')

#10. Some todos os subtotais dos produtos
total_subtotal = sum(item['subtotal'] for item in itens_pedido)

print(f'Total dos subtotais: R$ {total_subtotal}')