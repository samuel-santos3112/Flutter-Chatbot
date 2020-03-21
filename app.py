from flask import Flask, jsonify, request,flash,session
from models import Usuario
from conexao import Session
import control
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdhasdugqutw1623ashbd'

@app.route("/bot", methods=["POST"])
def response():
    message = request.form['query']
    res = message + " " + time.ctime()
    return jsonify({"response" : res})


@app.route("/", methods=["GET"])
def home():
    return jsonify({"Message" : "Está funcionando"})

@app.route('/criar_usuario' , methods = ['POST'])
def criar_usuario():
    try:
        data = request.json
        usuario = Usuario(nome = data['nome'], senha = data['senha'])
        control.criar(usuario)
        flash('Criado com sucesso')
        return jsonify({data['nome'] : " inserido com sucesso"})
    except Exception as e:
        return jsonify({'Erro ao inserir' : e})

if __name__ == '__main__':
    app.run(host='0.0.0.0')

