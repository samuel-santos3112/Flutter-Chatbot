from flask import Flask, jsonify,request
import time

app = Flask(__name__)

@app.route("/bot", methods=["POST"])
def response():
    query = dict(request.form)['query']
    res = query + " " + time.ctime()
    return jsonify({"response" : res})


@app.route("/", methods=["GET"])
def home():
    return jsonify({"Message" : "Está funcionando"})   


if __name__=="__main__":
    app.run(host="0.0.0.0",)