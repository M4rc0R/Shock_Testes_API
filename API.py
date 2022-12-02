from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/ValidaLogin', methods = ['POST'])
def ValidaApi():
    user = "XPTO"
    senha = "xpto"
    user_in = (request.get_json()["user"])
    senha_in = (request.get_json()["senha"])


    if user_in == user:
        if senha_in == senha:
            mensagem = {"status":"logado"}

        else:
            mensagem = {"status":"invalido"}
    
    else:
        mensagem = {"status":"invalido"}

    return jsonify(mensagem)


Data = [
    {
        'image':'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Dart-logo.png/768px-Dart-logo.png',
        'descricao': 'imagem1'
    },
    {
        'image':'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Dart-logo.png/768px-Dart-logo.png',
        'descricao': 'imagem2'
    },
    {
        'image':'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Dart-logo.png/768px-Dart-logo.png',
        'descricao': 'imagem3'
    },
]

@app.route('/PegaImagens', methods = ['GET'])
def DataImagens():
    return jsonify(Data)

app.run()