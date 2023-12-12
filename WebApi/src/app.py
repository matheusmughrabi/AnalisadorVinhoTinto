from flask import Flask, request, jsonify
from flask_restx import Api, Resource, ValidationError, fields
from flask_cors import CORS
from injector import Injector
from dtos.vinho_dto import VinhoDto
from core.modelo_preditivo_interface import ModeloPreditivoInterface
from IoC.container_injecao_dependencia import AppModule

app = Flask(__name__)
CORS(app)
api = Api(app, version='1.0', title='API de Qualidade do Vinho',
          description='Uma API para previsão da qualidade do vinho')

injector = Injector(AppModule())

# Modelo do Swagger correspondente ao VinhoDto
vinho_model = api.model('VinhoModel', {
    'fixedAcidity': fields.Float(required=True, description='Acidez Fixa', example=7.4),
    'volatileAcidity': fields.Float(required=True, description='Acidez Volátil', example=0.7),
    'chlorides': fields.Float(required=True, description='Cloreto', example=0.08),
    'totalSulfurDioxide': fields.Float(required=True, description='Dióxido de Enxofre Total', example=34),
    'sulphates': fields.Float(required=True, description='Sulfatos', example=0.5),
    'alcohol': fields.Float(required=True, description='Álcool', example=12.4)
})

@api.route('/prever')
class PrevisaoQualidade(Resource):
    @api.expect(vinho_model)
    def post(self):
        modelo_preditivo = injector.get(ModeloPreditivoInterface)
        dados = request.json
        try:
            vinho_dto = VinhoDto(**dados)
        except ValidationError as e:
            return {"message": str(e)}, 400
        qualidade = modelo_preditivo.prever_qualidade(vinho_dto)
        resposta = {'QualidadeDoVinho': qualidade}
        return resposta

if __name__ == '__main__':
    app.run(debug=True)
