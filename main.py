from flask import Flask
from flask import request, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route('/api/verificar_data', methods=['POST'])
def verificar_data():
    dados = request.get_json()
    data_atual = dados['data_atual']

    try:
        data_atual = datetime.strptime(data_atual, '%d/%m/%Y')
    except ValueError:
        response = {
            'Erro': 'Você inseriu um data inválida! Por favor, respeite o formato DD/MM/AAAA.'
        }
        return jsonify(response), 400

    feriados = [
        datetime.strptime('01/01/2023', '%d/%m/%Y'), # Confraternização Universal
        datetime.strptime('20/02/2023', '%d/%m/%Y'), # Carnaval
        datetime.strptime('21/02/2023', '%d/%m/%Y'), # Carnaval
        datetime.strptime('07/04/2023', '%d/%m/%Y'), # Paixão de Cristo
        datetime.strptime('21/04/2023', '%d/%m/%Y'), # Tiradentes
        datetime.strptime('01/05/2023', '%d/%m/%Y'), # Dia do Trabalho
        datetime.strptime('08/06/2023', '%d/%m/%Y'), # Corpus Christi
        datetime.strptime('07/09/2023', '%d/%m/%Y'), # Independência do Brasil
        datetime.strptime('12/10/2023', '%d/%m/%Y'), # Nossa Senhora Aparecida - Padroeira do Brasil
        datetime.strptime('02/11/2023', '%d/%m/%Y'), # Finados
        datetime.strptime('15/11/2023', '%d/%m/%Y'), # Proclamação da República
        datetime.strptime('25/12/2023', '%d/%m/%Y'), # Natal
    ]

    if data_atual.weekday() < 5 and data_atual not in feriados:
        response = {
            'result': 'Dia útil'
        }
        return jsonify(response), 200

    elif data_atual in feriados:
        response = {
            'result': 'Feriado'
        }
        return jsonify(response), 200

    else:
        response = {
            'result': 'Fim de semana'
        }
        return jsonify(response), 200

if __name__ == '__main__':
    app.run()