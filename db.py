import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

DATABASE = 'database.db'

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            DATABASE,
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def insert_restaurantes(args=()):
    sql = ''' INSERT INTO restaurantes(nome_fantasia, cnpj, ativo )
              VALUES(?,?,?) '''
    cur = get_db().cursor()
    cur.execute(sql, args)
    get_db().commit()
    return cur.lastrowid

def insert_user(args=()):
    sql = ''' INSERT INTO users(name,email,password,cpf)
              VALUES(?,?,?,?) '''
    cur = get_db().cursor()
    cur.execute(sql, args)
    get_db().commit()
    return cur.lastrowid    


def insert_pedidos(args=()):
    sql = ''' INSERT INTO pedidos(nome, status_pedido, data_de_criacao, data_de_atualizacao, rua, numero, bairro)
              VALUES(?,?,?,?,?,?,?) '''
    cur = get_db().cursor()
    cur.execute(sql, args)
    get_db().commit()
    return cur.lastrowid

def insert_address(args=()):
    sql = ''' INSERT INTO addresses(city,state_a)
              VALUES(?,?) '''
    cur = get_db().cursor()
    cur.execute(sql, args)
    get_db().commit()
    return cur.lastrowid

def insert_courier(args=()):
    sql = ''' INSERT INTO couriers(name,email,password,cpf)
              VALUES(?,?,?,?) '''
    cur = get_db().cursor()
    cur.execute(sql, args)
    get_db().commit()
    return cur.lastrowid

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = [dict((cur.description[i][0], value) \
       for i, value in enumerate(row)) for row in cur.fetchall()]
   
    get_db().commit()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
        
def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')
