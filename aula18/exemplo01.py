import pandas as pd
import numpy as np

try:
    print('\nObtendo dados...')
    endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    # utf-8, iso-8859-1, latin1, cp1252
    df_ocorrencias = pd.read_csv(endereco_dados, sep=';', encoding='iso-8859-1')
    # print(df_ocorrencias.head())

    # delimitando as variáveis
    df_roubo_veiculo = df_ocorrencias[['munic', 'roubo_veiculo']]

    # totalizando as ocorrências por municípios
    df_roubo_veiculo = df_roubo_veiculo.groupby('munic', as_index=False)['roubo_veiculo'].sum()
    
    # ordenando o dataframe
    df_roubo_veiculo = df_roubo_veiculo.sort_values(by= 'roubo_veiculo', ascending=False)

except Exception as e:
    print(f'Erro ao obter dados: {e}')

try:
    print('\nCalculando as medidas...')
    array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])

    mean_roubo_veiculo = np.mean(array_roubo_veiculo)
    median_roubo_veiculo = np.median(array_roubo_veiculo)
    distancia = abs(((mean_roubo_veiculo - median_roubo_veiculo) / median_roubo_veiculo) * 100)

    print('\nMedidas de tendência central')
    print(30 * "=")
    print(f'Média: {mean_roubo_veiculo:.2f}')
    print(f'Mediana: {median_roubo_veiculo:.2f}')
    print(f'Distância: {distancia:.2f} %')

except Exception as e:
    print(f'Erro ao calcular medidas: {e}')