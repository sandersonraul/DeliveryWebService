DROP TABLE IF EXISTS restaurants;

CREATE TABLE restaurants (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(50) NOT NULL,
  cnpj VARCHAR(50) NOT NULL,
  email VARCHAR(50),
  active BOOLEAN NOT NULL,
  address_id INTERGER DEFAULT 1,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY(address_id) REFERENCES addresses(id)
);

DROP TABLE IF EXISTS orders;

CREATE TABLE orders (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  descr VARCHAR(50) UNIQUE NOT NULL,
  value DECIMAL(17,2) NULL DEFAULT NULL,
  status VARCHAR(15) NOT NULL,
  restaurant_id INTEGER,
  address_id INTERGER,
  FOREIGN KEY(restaurant_id) REFERENCES restaurants(id)
);

DROP TABLE IF EXISTS delivery;

CREATE TABLE delivery (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  order_id INTEGER NOT NULL,
  status VARCHAR(30),
  couriers_id INTEGER NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY(order_id) REFERENCES orders(id),
  FOREIGN KEY(couriers_id) REFERENCES couriers(id)
);

DROP TABLE IF EXISTS addresses;

CREATE TABLE addresses (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  city VARCHAR(50) NOT NULL,
  state_a VARCHAR(30) NOT NULL,
  street VARCHAR(50),
  number INTEGER,
  neighborhood VARCHAR(50),
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS couriers;

CREATE TABLE couriers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(30) NOT NULL,
  email VARCHAR(30) UNIQUE NOT NULL,
  password VARCHAR(30) NOT NULL,
  cpf VARCHAR(30) UNIQUE NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(30) NOT NULL,
  email VARCHAR(30) UNIQUE NOT NULL,
  password VARCHAR(30) NOT NULL,
  address_id INTEGER,
  cpf VARCHAR(30) UNIQUE NOT NULL,
  FOREIGN KEY(address_id) REFERENCES addresses(id)
);
