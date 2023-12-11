from injector import Module, provider, singleton
import pickle
from core.modelo_preditivo_interface import ModeloPreditivoInterface
from core.modelo_preditivo_vinho_tinho import ModeloPreditivoVinhoTinto

class AppModule(Module):
    @singleton
    @provider
    def provide_model(self) -> ModeloPreditivoInterface:
        model = pickle.load(open('modelo_preditivo.pkl', 'rb'))
        return ModeloPreditivoVinhoTinto(model)