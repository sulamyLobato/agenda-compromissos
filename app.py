from flask import Flask, jsonify, request
from db import init_db, adicionar_compromisso_bd, listar_compromissos_bd, excluir_compromisso_bd

app = Flask(__name__)


init_db()

# Rota para listar
@app.route('/compromissos', methods=['GET'])
def listar_compromissos():
    compromissos = listar_compromissos_bd()
    return jsonify([{'id': c[0], 'titulo': c[1], 'data': c[2], 'hora': c[3]} for c in compromissos])

# Rota para adicionar
@app.route('/compromisso', methods=['POST'])
def adicionar_compromisso():
    dados = request.get_json()
    titulo = dados['titulo']
    data = dados['data']
    hora = dados['hora']
    adicionar_compromisso_bd(titulo, data, hora)
    return jsonify({'titulo': titulo, 'data': data, 'hora': hora}), 201



# Rota para deletar
@app.route('/compromisso/<string:titulo>', methods=['DELETE'])
def excluir_compromisso(titulo):
    excluir_compromisso_bd(titulo)  
    return jsonify({"message": "Compromisso deletado com sucesso", "titulo": titulo}), 200



if __name__ == '__main__':
    app.run(debug=True)
