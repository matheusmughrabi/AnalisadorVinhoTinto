from abc import ABC, abstractmethod

class ModeloPreditivoInterface(ABC):
    @abstractmethod
    def prever_qualidade(self, input_data):
        pass