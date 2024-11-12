import pandas as pd

# Carregar o arquivo Excel
df = pd.read_excel('lista_de_compras.xlsx')

# Verifique se a coluna 'id' existe antes de tentar removê-la
if 'id' in df.columns:
    df = df.drop(columns=['id'])

# Adicione uma nova linha sem definir o 'id'
nova_linha = pd.DataFrame({'produtos': ['frango']})
df = pd.concat([df, nova_linha], ignore_index=True)

print(df)
# Salva o DataFrame no mesmo arquivo Excel, sem o índice
df.to_excel('lista_de_compras.xlsx', index=False)

print("Nova linha adicionada e arquivo salvo com sucesso!")
