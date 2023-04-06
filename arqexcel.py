import pandas as pd


# Passo 4: Ordenar numa tabela os valores coletados
bitcoin = 143453
moedas = ['Bitcoin', 'Dólar', 'Euro']
valores = [bitcoin, 5.01, 5.55]

dataframe = pd.DataFrame({
    'Moeda': moedas,
    'Valor': valores

})
print(dataframe)

# Passo 5: Gerar um arquivo Excel

dataframe.to_excel('moedas.xlsx', index=False)
# Passo 6: Enviar o arquivo via e-mail