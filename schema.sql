DROP TABLE IF EXISTS restaurantes;

CREATE TABLE restaurantes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome_fantasia VARCHAR(30) NOT NULL,
  cnpj VARCHAR(50) NOT NULL,
  email VARCHAR(50),
  ativo BOOLEAN NOT NULL,
  endereco_id INTERGER,
  rua VARCHAR(30),
  numero INTEGER,
  bairro VARCHAR(30),
  created_at CURRENT_TIMESTAMP,
  updated_at CURRENT_TIMESTAMP
);


DROP TABLE IF EXISTS pedidos;

CREATE TABLE pedidos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome VARCHAR(30) UNIQUE NOT NULL,
  status_pedido Boolean NOT NULL,
  data_de_criacao VARCHAR(30) NOT NULL,
  data_de_atualizacao VARCHAR(30) NOT NULL,
  rua VARCHAR(30) NOT NULL,
  numero INTEGER NOT NULL,
  bairro VARCHAR(30) NOT NULL
);