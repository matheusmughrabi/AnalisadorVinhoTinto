from flask import Flask, request, jsonify
from flask_cors import CORS
from injector import Injector
from IoC.container_injecao_dependencia import AppModule
from dtos.vinho_dto import VinhoDto
from core.modelo_preditivo_interface import ModeloPreditivoInterface

# Inicialização do aplicativo Flask
app = Flask(__name__)
CORS(app)
injector = Injector(AppModule())

@app.route('/prever', methods=['POST'])
def gerarPrevisao():
    modelo_preditivo = injector.get(ModeloPreditivoInterface)  # Obter o preditor do container
    
    dados = request.get_json(force=True)
    
    vinho_dto = VinhoDto(**dados)
    
    qualidade = modelo_preditivo.prever_qualidade(vinho_dto)
    
    resposta = {'QualidadeDoVinho': qualidade}
    
    return jsonify(resposta)

if __name__ == '__main__':
    app.run(debug=True)
