from flask import Flask, jsonify, request
from webcrawler import start_crawler


app = Flask(__name__)

@app.route('/processo', methods=['POST'])
def receber_json_arquivo():
    global numero

    content = request.get_json()
    numero = content.get('numero')
   
    return jsonify({'mensagem': numero})


@app.route('/dadosProcessuais')
def get_items():
    result = start_crawler(numero)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
