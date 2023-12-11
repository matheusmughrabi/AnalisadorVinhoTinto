from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import pickle

app = Flask(__name__)
CORS(app)

# Carregar o modelo preditivo
model = pickle.load(open('modelo_preditivo.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    print("teste")
    # Obter dados do POST request
    data = request.get_json(force=True)

    # Converter dados em DataFrame
    prediction_data = pd.DataFrame([data])

    prediction_data.columns = ['fixed acidity', 'volatile acidity', 'chlorides', 'total sulfur dioxide', 'sulphates', 'alcohol']

    # Fazer a predição
    prediction = model.predict(prediction_data)

    response_data = {'QualidadeDoVinho': prediction[0]}

    # Enviar de volta a predição como resposta JSON
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
