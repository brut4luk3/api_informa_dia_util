from flask import Flask
from flask import request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/api/informa_dia_util', methods=['POST'])
def verificar_data():
    dados = request.get_json()
    data_atual = dados['data_atual']
    estado = dados['estado']

    if '-' in data_atual:
        data_atual = datetime.strptime(data_atual, '%Y-%m-%d').strftime('%d/%m/%Y')

    try:
        data_atual = datetime.strptime(data_atual, '%d/%m/%Y')
    except ValueError:
        response = {
            'Erro': 'Você inseriu um data inválida! Por favor, respeite o formato DD/MM/AAAA.'
        }
        return jsonify(response), 400

    quantidade_caracteres_estado = len(estado)

    if quantidade_caracteres_estado > 3:
        response = {
            'Erro': 'Você inseriu a UF de um estado inválida.'
        }
        return jsonify(response), 400

    ano_atual = datetime.now().year

    feriados_nacionais = [
        datetime.strptime(f'01/01/{ano_atual}', '%d/%m/%Y'), # Confraternização Universal
        datetime.strptime(f'20/02/{ano_atual}', '%d/%m/%Y'), # Carnaval
        datetime.strptime(f'21/02/{ano_atual}', '%d/%m/%Y'), # Carnaval
        datetime.strptime(f'07/04/{ano_atual}', '%d/%m/%Y'), # Paixão de Cristo
        datetime.strptime(f'21/04/{ano_atual}', '%d/%m/%Y'), # Tiradentes
        datetime.strptime(f'01/05/{ano_atual}', '%d/%m/%Y'), # Dia do Trabalho
        datetime.strptime(f'08/06/{ano_atual}', '%d/%m/%Y'), # Corpus Christi
        datetime.strptime(f'07/09/{ano_atual}', '%d/%m/%Y'), # Independência do Brasil
        datetime.strptime(f'12/10/{ano_atual}', '%d/%m/%Y'), # Nossa Senhora Aparecida - Padroeira do Brasil
        datetime.strptime(f'02/11/{ano_atual}', '%d/%m/%Y'), # Finados
        datetime.strptime(f'15/11/{ano_atual}', '%d/%m/%Y'), # Proclamação da República
        datetime.strptime(f'25/12/{ano_atual}', '%d/%m/%Y'), # Natal
        datetime.strptime(f'31/12/{ano_atual}', '%d/%m/%Y')  # Véspera do Ano Novo
    ]

    feriados_acre = [
        datetime.strptime(f'20/01/{ano_atual}', '%d/%m/%Y'),  # Dia do Católico
        datetime.strptime(f'25/01/{ano_atual}', '%d/%m/%Y'),  # Dia do Evangélico
        datetime.strptime(f'15/06/{ano_atual}', '%d/%m/%Y'),  # Aniversário do Estado do Acre
        datetime.strptime(f'05/09/{ano_atual}', '%d/%m/%Y'),  # Dia da Amazônia
        datetime.strptime(f'17/11/{ano_atual}', '%d/%m/%Y'),  # Tratado de Petrópolis
    ]

    feriados_alagoas = [
        datetime.strptime(f'24/06/{ano_atual}', '%d/%m/%Y'),  # Dia de São João
        datetime.strptime(f'29/06/{ano_atual}', '%d/%m/%Y'),  # Dia de São Pedro
        datetime.strptime(f'16/09/{ano_atual}', '%d/%m/%Y'),  # Emancipação Política de Alagoas
        datetime.strptime(f'20/11/{ano_atual}', '%d/%m/%Y'),  # Dia da Consciência Negra
    ]

    feriados_amapa = [
        datetime.strptime(f'19/03/{ano_atual}', '%d/%m/%Y'),  # Dia de São José
        datetime.strptime(f'25/07/{ano_atual}', '%d/%m/%Y'),  # Dia de São Tiago
        datetime.strptime(f'05/10/{ano_atual}', '%d/%m/%Y'),  # Criação do Estado do Amapá
        datetime.strptime(f'20/11/{ano_atual}', '%d/%m/%Y'),  # Dia da Consciência Negra
    ]

    feriados_amazonas = [
        datetime.strptime(f'05/09/{ano_atual}', '%d/%m/%Y'),  # Elevação do Amazonas à categoria de província
        datetime.strptime(f'20/11/{ano_atual}', '%d/%m/%Y'),  # Dia da Consciência Negra
        datetime.strptime(f'08/12/{ano_atual}', '%d/%m/%Y'),  # Dia de Nossa Senhora da Conceição
    ]

    feriados_bahia = [
        datetime.strptime(f'02/07/{ano_atual}', '%d/%m/%Y'),  # Independência do Estado da Bahia
    ]

    feriados_ceara = [
        datetime.strptime(f'19/03/{ano_atual}', '%d/%m/%Y'),  # Dia de São José
        datetime.strptime(f'25/03/{ano_atual}', '%d/%m/%Y'),  # Data Magna do Ceará
    ]

    feriados_distrito_federal = [
        datetime.strptime(f'21/04/{ano_atual}', '%d/%m/%Y'),  # Fundação de Brasília
        datetime.strptime(f'30/11/{ano_atual}', '%d/%m/%Y'),  # Dia do Evangélico
    ]

    feriados_espirito_santo = [
        datetime.strptime(f'28/10/{ano_atual}', '%d/%m/%Y'),  # Dia do Servidor Público
    ]

    feriados_maranhao = [
        datetime.strptime(f'28/07/{ano_atual}', '%d/%m/%Y'),  # Dia da Adesão do Maranhão à Independência do Brasil
    ]

    feriados_mato_grosso = [
        datetime.strptime(f'20/11/{ano_atual}', '%d/%m/%Y'),  # Dia da Consciência Negra
    ]

    feriados_mato_grosso_do_sul = [
        datetime.strptime(f'11/10/{ano_atual}', '%d/%m/%Y'),  # Criação do Estado do Mato Grosso do Sul
    ]

    feriados_minas_gerais = [
        datetime.strptime(f'21/04/{ano_atual}', '%d/%m/%Y'),  # Data Magna de Minas Gerais
    ]

    feriados_para = [
        datetime.strptime(f'15/08/{ano_atual}', '%d/%m/%Y'),  # Adesão do Grão-Pará à independência do Brasil
    ]

    feriados_paraiba = [
        datetime.strptime(f'05/08/{ano_atual}', '%d/%m/%Y'),  # Fundação do Estado da Paraíba
    ]

    feriados_pernambuco = [
        datetime.strptime(f'06/03/{ano_atual}', '%d/%m/%Y'),  # Data Magna do Estado de Pernambuco
        datetime.strptime(f'24/06/{ano_atual}', '%d/%m/%Y'),  # Dia de São João
    ]

    feriados_piaui = [
        datetime.strptime(f'13/03/{ano_atual}', '%d/%m/%Y'),  # Dia da Batalha do Jenipapo
        datetime.strptime(f'19/10/{ano_atual}', '%d/%m/%Y'),  # Dia do Piauí
    ]

    feriados_rio_de_janeiro = [
        datetime.strptime(f'23/04/{ano_atual}', '%d/%m/%Y'),  # Dia de São Jorge
        datetime.strptime(f'20/11/{ano_atual}', '%d/%m/%Y'),  # Dia da Consciência Negra
    ]

    feriados_rio_grande_do_norte = [
        datetime.strptime(f'29/06/{ano_atual}', '%d/%m/%Y'),  # Dia de São Pedro
        datetime.strptime(f'03/10/{ano_atual}', '%d/%m/%Y'),  # Mártires de Cunhaú e Uruaçu
    ]

    feriados_rio_grande_do_sul = [
        datetime.strptime(f'20/09/{ano_atual}', '%d/%m/%Y'),  # Revolução Farroupilha (Dia do Gaúcho)
    ]

    feriados_rondonia = [
        datetime.strptime(f'05/10/{ano_atual}', '%d/%m/%Y'),  # Criação de Roraima
    ]

    feriados_santa_catarina = [
        datetime.strptime(f'15/08/{ano_atual}', '%d/%m/%Y'),  # Dia do Estado de Santa Catarina
    ]

    feriados_sao_paulo = [
        datetime.strptime(f'09/07/{ano_atual}', '%d/%m/%Y'),  # Revolução Constitucionalista de 1932
    ]

    feriados_sergipe = [
        datetime.strptime(f'08/07/{ano_atual}', '%d/%m/%Y'),  # Emancipação política de Sergipe
    ]

    feriados_tocantins = [
        datetime.strptime(f'08/09/{ano_atual}', '%d/%m/%Y'),  # Nossa Senhora da Natividade
        datetime.strptime(f'05/10/{ano_atual}', '%d/%m/%Y'),  # Criação de Tocantins
    ]

    if estado == 'AC':
        if data_atual in feriados_acre:
            response = {
                'result': 'Feriado'
            }
            return jsonify(response), 200

    if estado == 'AL':
        if data_atual in feriados_alagoas:
            response = {
                'result': 'Feriado'
            }
            return jsonify(response), 200

    if estado == 'AP':
        if data_atual in feriados_amapa:
            response = {
                'result': 'Feriado'
            }
            return jsonify(response), 200

    if estado == 'AM':
        if data_atual in feriados_amazonas:
            response = {
                'result': 'Feriado'
            }
            return jsonify(response), 200

    if estado == 'BA':
        if data_atual in feriados_bahia:
            response = {
                'result': 'Feriado'
            }
            return jsonify(response), 200

    if estado == 'CE':
        if data_atual in feriados_ceara:
            response = {
                'result': 'Feriado'
            }
            return jsonify(response), 200

    if estado == 'DF':
        if data_atual in feriados_distrito_federal:
            response = {
                'result': 'Feriado'
            }
            return jsonify(response), 200

    if estado == 'ES':
        if data_atual in feriados_espirito_santo:
            response = {
                'result': 'Feriado'
            }
            return jsonify(response), 200

    if estado == 'MA':
        if data_atual in feriados_maranhao:
            response = {
                'result': 'Feriado'
            }
            return jsonify(response), 200

    if estado == 'MT':
        if data_atual in feriados_mato_grosso:
            response = {
                'result': 'Feriado'
            }
            return jsonify(response), 200

    if estado == 'MS':
        if data_atual in feriados_mato_grosso_do_sul:
            response = {
                'result': 'Feriado'
            }
            return jsonify(response), 200

    if estado == 'MG':
        if data_atual in feriados_minas_gerais:
            response = {
                'result': 'Feriado'
            }
            return jsonify(response), 200

    if estado == 'PA':
        if data_atual in feriados_para:
            response = {
                'result': 'Feriado'
            }
            return jsonify(response), 200

    if estado == 'PB':
        if data_atual in feriados_paraiba:
            response = {
                'result': 'Feriado'
            }
            return jsonify(response), 200

    if estado == 'PE':
        if data_atual in feriados_pernambuco:
            response = {
                'result': 'Feriado'
            }
            return jsonify(response), 200

    if estado == 'PI':
        if data_atual in feriados_piaui:
            response = {
                'result': 'Feriado'
            }
            return jsonify(response), 200

    if estado == 'RJ':
        if data_atual in feriados_rio_de_janeiro:
            response = {
                'result': 'Feriado'
            }
            return jsonify(response), 200

    if estado == 'RN':
        if data_atual in feriados_rio_grande_do_norte:
            response = {
                'result': 'Feriado'
            }
            return jsonify(response), 200

    if estado == 'RS':
        if data_atual in feriados_rio_grande_do_sul:
            response = {
                'result': 'Feriado'
            }
            return jsonify(response), 200

    if estado == 'RO':
        if data_atual in feriados_rondonia:
            response = {
                'result': 'Feriado'
            }
            return jsonify(response), 200

    if estado == 'SC':
        if data_atual in feriados_santa_catarina:
            response = {
                'result': 'Feriado'
            }
            return jsonify(response), 200

    if estado == 'SP':
        if data_atual in feriados_sao_paulo:
            response = {
                'result': 'Feriado'
            }
            return jsonify(response), 200

    if estado == 'SE':
        if data_atual in feriados_sergipe:
            response = {
                'result': 'Feriado'
            }
            return jsonify(response), 200

    if estado == 'TO':
        if data_atual in feriados_tocantins:
            response = {
                'result': 'Feriado'
            }
            return jsonify(response), 200

    if estado == 'all':
        pass

    if data_atual.weekday() < 5 and data_atual not in feriados_nacionais:
        response = {
            'result': 'Dia útil'
        }
        return jsonify(response), 200

    elif data_atual in feriados_nacionais:
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