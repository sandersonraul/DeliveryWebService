import requests

api_url = 'http://127.0.0.1:8090/restaurants'

def insert():
  rest = {"name": "Marcia lanches2", "cnpj": "56135221515", "email": "marcialanches2@gmail.com", "address_id": 1 }
  response = requests.post(api_url, json=rest)
  print(response.json())

def update(id):
  rest = {"name": "Marcia lanches", "cnpj": "2515151515", "email": "marcialanches@gmail.com", "active": 0, "address_id": 1 }
  response = requests.put(f'http://127.0.0.1:8090/restaurants/{id}', json=rest)
  print(response.text)

def delete(id):
  response = requests.delete(f"http://127.0.0.1:8090/restaurants/{id}")
  print(response.txt)

def insert_address():
  addr = {"city": "Peum", "state_a": "RN", "street": "brisa do lago", "number": 109, "neighborhood": "centro"}
  response = requests.post(f"http://127.0.0.1:8090/addresses", json=addr)
  print(response.json())
# insert_address()
# insert()
# update(1)
delete(2)