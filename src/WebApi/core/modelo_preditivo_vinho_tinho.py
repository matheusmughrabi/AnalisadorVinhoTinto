import pandas as pd
from dtos.vinho_dto import VinhoDto
from core.modelo_preditivo_interface import ModeloPreditivoInterface

class ModeloPreditivoVinhoTinto(ModeloPreditivoInterface):
    def __init__(self, model):
        self.model = model

    def prever_qualidade(self, wine_dto: VinhoDto):
        prediction_data = self._to_dataframe(wine_dto)
        return self.model.predict(prediction_data)[0]
    
    def _to_dataframe(self, wine_dto: VinhoDto):
        df = pd.DataFrame([wine_dto.dict()])
        df.columns = ['fixed acidity', 'volatile acidity', 'chlorides', 
                      'total sulfur dioxide', 'sulphates', 'alcohol']
        return df