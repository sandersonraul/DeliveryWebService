from flask import Flask, request, jsonify
import db
    
app = Flask(__name__)

@app.route("/restaurantes",methods=['GET'])
def get_restaurantes():
    restaurantes = db.query_db('select * from restaurantes')
    return jsonify(restaurantes),200

@app.route("/restaurantes",methods=['POST'])
def add_restaurante():
    if request.is_json:
        restaurante = request.get_json()
        id = db.insert_restaurantes(
            (
                restaurante['nome_fantasia'],
                restaurante['cnpj'], 
                restaurante['ativo']
            )
        )
        return {"id":id}, 201
    return {"error": "Request must be JSON"}, 415

@app.route("/users",methods=['GET'])
def get_users():
    users = db.query_db('select * from users')
    return jsonify(users),200

@app.route("/users",methods=['POST'])
def add_user():
    if request.is_json:
        user = request.get_json()
        id = db.insert_user(
            (
            user['name'],
            user['email'],
            user['password'],
            user['cpf']
            )
        )
        return {"id":id}, 201
    return {"error": "Request must be JSON"}, 415

@app.route("/users/<int:id>", methods=["DELETE"])
def delete_address(id):
    db.query_db(f'DELETE from users WHERE id= {id}')
    
    return 'ok', 200  
@app.route("/users/<int:id>",methods=['GET'])
def get_users_byid(id):
    address = db.query_db(f'select * from users where id = {id}')
    return jsonify(address),200

@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    users = request.get_json()
    db.query_db(f'UPDATE users SET name = "{users["name"]}",email = "{users["email"]}", password = "{users["password"]}", cpf = "{users["cpf"]}" where id = {id}')
    return 'ok', 200

@app.route("/pedidos",methods=['GET'])
def get_pedidos():
    pedidos = db.query_db('select * from pedidos')
    return jsonify(pedidos),200

@app.route("/pedidos",methods=['POST'])
def add_pedidos():
    if request.is_json:
        pedido = request.get_json()
        id = db.insert_pedidos(
            (
                pedido['nome'],
                pedido['status_pedido'], 
                pedido['data_de_criacao'],
                pedido['data_de_atualizacao'], 
                pedido['rua'], 
                pedido['numero'], 
                pedido['bairro']
            )
        )
        return {"id":id}, 201
    return {"error": "Request must be JSON"}, 415

@app.route("/couriers",methods=['POST'])
def add_courier():
    if request.is_json:
        courier = request.get_json()
        id = db.insert_courier(
            (
            courier['name'],
            courier['email'],
            courier['password'],
            courier['cpf']
            )
        )
        return {"id":id}, 201
    return {"error": "Request must be JSON"}, 415

@app.route("/couriers",methods=['GET'])
def get_couriers():
    couriers = db.query_db('select * from couriers')
    return jsonify(couriers),200
@app.route("/addresses",methods=['POST'])
def add_address():
    if request.is_json:
        address = request.get_json()
        id = db.insert_address(
            (
            address['city'],
            address['state_a']
            )
        )
        return {"id":id}, 201
    return {"error": "Request must be JSON"}, 415

@app.route("/addresses",methods=['GET'])
def get_addresses():
    addresses = db.query_db('select * from addresses')
    return jsonify(addresses),200

if __name__ == '__main__':
    init_db = False
    
    db.init_app(app)
    
    if init_db:
        with app.app_context():
            db.init_db()
    
    app.run(debug=True,host="0.0.0.0", port=8090)
