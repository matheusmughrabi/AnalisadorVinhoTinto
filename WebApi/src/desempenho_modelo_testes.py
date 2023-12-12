import pickle
from core.modelo_preditivo_vinho_tinho import ModeloPreditivoVinhoTinto
from dtos.vinho_dto import VinhoDto
import pytest
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Dados de teste
dados_teste = [
    {'fixedAcidity': 11.4, 'volatileAcidity': 0.28, 'chlorides': 0.076, 'totalSulfurDioxide': 34, 'sulphates': 0.56, 'alcohol': 10.4},
    {'fixedAcidity': 7.8, 'volatileAcidity': 0.88, 'chlorides': 0.098, 'totalSulfurDioxide': 67, 'sulphates': 0.65, 'alcohol': 9.8},
    {'fixedAcidity': 7.8, 'volatileAcidity': 0.76, 'chlorides': 0.092, 'totalSulfurDioxide': 53, 'sulphates': 0.58, 'alcohol': 9.8},
    {'fixedAcidity': 8.8, 'volatileAcidity': 0.96, 'chlorides': 0.092, 'totalSulfurDioxide': 54, 'sulphates': 0.55, 'alcohol': 9.6},
    {'fixedAcidity': 9.8, 'volatileAcidity': 0.86, 'chlorides': 0.082, 'totalSulfurDioxide': 55, 'sulphates': 0.59, 'alcohol': 9.7},
    {'fixedAcidity': 7.8, 'volatileAcidity': 0.56, 'chlorides': 0.092, 'totalSulfurDioxide': 56, 'sulphates': 0.60, 'alcohol': 9.9},
]

# Valores de qualidade do vinho esperados para os dados de teste
qualidades_esperadas = ['Bom', 'Ruim', 'Bom', 'Ruim', 'Ruim', 'Ruim']

# Inicializar o modelo
model = pickle.load(open('modelo_preditivo.pkl', 'rb'))
modelo = ModeloPreditivoVinhoTinto(model)

# Converter dados de teste para VinhoDto
dados_teste_dto = [VinhoDto(**dados) for dados in dados_teste]

def test_acuracia_modelo():
    previsoes = [modelo.prever_qualidade(vinho_dto) for vinho_dto in dados_teste_dto]
    acuracia = accuracy_score(qualidades_esperadas, previsoes)
    assert acuracia > 0.8

def test_precisao_modelo():
    previsoes = [modelo.prever_qualidade(vinho_dto) for vinho_dto in dados_teste_dto]
    precisao = precision_score(qualidades_esperadas, previsoes, average='weighted')
    assert precisao > 0.75

def test_f1_score_modelo():
    previsoes = [modelo.prever_qualidade(vinho_dto) for vinho_dto in dados_teste_dto]
    f1 = f1_score(qualidades_esperadas, previsoes, average='weighted')
    assert f1 > 0.75
