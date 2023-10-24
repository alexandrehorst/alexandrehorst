import requests

# Request para saber o faturamento total
response_faturamento = requests.get('http://127.0.0.1:5000/')
response_faturamento = response_faturamento.json()
print('Faturamento total de vendas:', response_faturamento['faturamento'],'\n')
print('Resposta em formato JSON: ', response_faturamento, '\n')  # resposta em formato json

# Resquest para saber o valor faturado com cada produto
response_produtos = requests.get('http://127.0.0.1:5000/vendas/produtos')
response_produtos = response_produtos.json()
print('Faturamento de venda de cada produto em formato JSON: \n')  # resposta em formato json
print(response_produtos, '\n')  # resposta em formato json

# Resquest para saber o valor faturado com reterminado produto
nome_produto = input('Entre com o nome do produto cujo faturamento deseja consultar: ')
try:
    response_fat_produto = requests.get(f'http://127.0.0.1:5000/vendas/produtos/{nome_produto}')
    response_fat_produto = response_fat_produto.json()
    print(f"\nO valor faturado com  a venda de {nome_produto} foi de R$ {response_fat_produto['Valor Final']}\n")
    print('Resposta em formato JSON: ', response_fat_produto)  # resposta em formato json
except:
    print('Produto não encontrado. Verifique se o produto informado foi digitado corretamente.')