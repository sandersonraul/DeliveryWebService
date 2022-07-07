from flask import Flask, request, jsonify
import db
    
app = Flask(__name__)

@app.route("/users",methods=['GET'])
def get_users():
    users = db.query_db('select * from users')
    return jsonify(users),200

@app.route("/users",methods=['POST'])
def add_user():
    if request.is_json:
        user = request.get_json()
        id = db.insert((user['nome'],user['email']))
        return {"id":id}, 201
    return {"error": "Request must be JSON"}, 415

@app.route("/pedidos",methods=['GET'])
def get_pedidos():
    pedidos = db.query_db('select * from pedidos')
    return jsonify(pedidos),200

@app.route("/pedidos",methods=['POST'])
def add_pedidos():
    if request.is_json:
        pedido = request.get_json()
        id = db.insert_pedidos((pedido['nome'],pedido['status_pedido'], pedido['data_de_criacao'],pedido['data_de_atualizacao'], pedido['rua'], pedido['numero'], pedido['bairro']))
#        (nome, status_pedido, data_de_criacao, data_de_atualizacao,rua,numero,bairro)
        return {"id":id}, 201
    return {"error": "Request must be JSON"}, 415
if __name__ == '__main__':
    init_db = True
    
    db.init_app(app)
    
    if init_db:
        with app.app_context():
            db.init_db()
    
    app.run(debug=True,host="0.0.0.0", port=8090)