from flask import Flask, request, jsonify
from flask_cors import CORS
import db
app = Flask(__name__)
cors = CORS(app)

@app.route("/restaurants",methods=['GET'])
def get_restaurants():
    restaurants = db.query_db('select * from restaurants')
    return jsonify(restaurants),200

@app.route("/restaurants/<int:id>",methods=["GET"])
def get_restaurant_by_id(id):
    restaurant = db.query_db(f"select * from restaurants where id = {id}")
    return jsonify(restaurant), 200

@app.route("/restaurants/<int:id>", methods=["PUT"])
def update_restaurante(id):
    if request.is_json:
        res = request.get_json()
        db.query_db(f'update restaurants set name = "{res["name"]}", cnpj = "{res["cnpj"]}", email = "{res["email"]}", active = "{res["active"]}", address_id = "{res["address_id"]}" where id = {id}')
        return 'updated successfully', 200
    return {"error": "Request must be JSON"}, 415

@app.route("/restaurants",methods=['POST'])
def add_restaurante():
    if request.is_json:
        restaurante = request.get_json()
        id = db.insert_restaurants(
            (
                restaurante['name'],
                restaurante['cnpj'], 
                restaurante['email'],
                restaurante['address_id'],
            )
        )
        return {"id":id}, 201
    return {"error": "Request must be JSON"}, 415

@app.route("/restaurants/<int:id>",methods=["DELETE"])
def delete_restaurant(id):
    db.query_db(f"DELETE FROM restaurants WHERE id = {id}")
    return 'Deleted successfully',200

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
def delete_users(id):
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

@app.route("/orders",methods=['GET'])
def get_orders():
    orders = db.query_db('select * from orders')
    return jsonify(orders),200

@app.route("/orders/<int:id>",methods=["GET"])
def get_order_by_id(id):
    pedido = db.query_db(f"select * from orders where id = {id}")
    return jsonify(pedido),200

@app.route("/orders",methods=['POST'])
def add_orders():
    if request.is_json:
        order = request.get_json()
        id = db.insert_orders(
            (
                order['descr'], 
                order['value'],
                order['restaurant_id'],
                order['address_id'],    
            )
        )
        return {"id":id}, 201
    return {"error": "Request must be JSON"}, 415

@app.route("/orders/<int:id>", methods=['PUT'])
def update_order(id):
    if request.is_json:
        order = request.get_json()
        db.query_db(f'UPDATE orders set descr = "{order["descr"]}", value = "{order["value"]}", status = "{order["status"]}", restaurant_id = "{order["restaurant_id"]}", address_id = "{order["address_id"]}" WHERE id = {id}')
        return 'Updated successfully', 201
    return {"error": "Request must be JSON"}, 415

@app.route("/orders/<int:id>",methods=["DELETE"])
def delete_order(id):
    db.query_db(f"DELETE FROM orders WHERE id = {id}")
    return 'Deleted successfully',200
 
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

@app.route("/couriers/<int:id>", methods=['PUT'])
def update_courier(id):
    if request.is_json:
        courier = request.get_json()
        db.query_db(f'update couriers set name = "{courier["name"]}", email = "{courier["email"]}", password = "{courier["password"]}", cpf = "{courier["cpf"]}" where id = {id} ')
        return 'Updated successfully', 201
    return {"error": "Request must be JSON"}, 415

@app.route("/couriers",methods=['GET'])
def get_couriers():
    couriers = db.query_db('select * from couriers')
    return jsonify(couriers),200

@app.route("/couriers/<int:id>",methods=["GET"])
def get_couriers_by_id(id):
    courier = db.query_db(f"select * from couriers where id = {id}")
    return jsonify(courier),200

@app.route("/couriers/<int:id>",methods=["DELETE"])
def delete_courier(id):
    courier = db.query_db(f"select * from couriers where id = {id}")
    return jsonify(courier),200

@app.route("/addresses",methods=['POST'])
def add_address():
    if request.is_json:
        address = request.get_json()
        id = db.insert_address(
            (
            address['city'],
            address['state_a'],
            address['street'],
            address['number'],
            address['neighborhood']
            )
        )
        return {"id":id}, 201
    return {"error": "Request must be JSON"}, 415

@app.route("/addresses/<int:id>", methods=['PUT'])
def update_address(id):
    if request.is_json:
        address = request.get_json()
        db.query_db(f'update addresses set city = "{address["city"]}", state_a = "{address["state_a"]}", street = "{address["street"]}", number = "{address["number"]}", neighborhood = "{address["neighborhood"]}" where id = {id}')
        return 'Updated successfully', 201
    return {"error": "Request must be JSON"}, 415

@app.route("/addresses",methods=['GET'])
def get_addresses():
    addresses = db.query_db('select * from addresses')
    return jsonify(addresses),200

@app.route("/addresses/<int:id>",methods=["GET"])
def get_address_by_id(id):
    address = db.query_db(f"select * from addresses where id = {id}")
    return jsonify(address),200

@app.route("/addresses/<int:id>",methods=["DELETE"])
def delete_address(id):
    address = db.query_db(f"delete from addresses where id = {id}")
    return jsonify(address),200

@app.route("/delivery",methods=['GET'])
def get_delivery():
    delivery = db.query_db('select * from delivery')
    return jsonify(delivery),200 

@app.route("/delivery/<int:id>",methods=["GET"])
def get_delivery_by_id(id):
    delivery = db.query_db(f"select * from delivery where id = {id}")
    return jsonify(delivery),200  

@app.route("/delivery", methods=["POST"])
def add_delivery():
    if request.is_json:
        delivery = request.get_json()
        id = db.insert_delivery(
            (
            delivery['order_id'],
            delivery['courier_id'],
            )
        )
        return {"id":id}, 201
    return {"error": "Request must be JSON"}, 415


@app.route("/delivery/<int:id>", methods=["PUT"])
def update_delivery(id):
    if request.is_json:
        delivery = request.get_json()
        db.query_db(f'UPDATE delivery set status = "{delivery["status"]}" where id = {id}')
        return 'Updated successfully', 201
    return {"error": "Request must be JSON"}, 415


if __name__ == '__main__':
    init_db = False
    
    db.init_app(app)
    
    if init_db:
        with app.app_context():
            db.init_db()
    
    app.run(debug=True,host="0.0.0.0", port=8090)
