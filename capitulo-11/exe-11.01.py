import sqlite3
from contextlib import closing

with sqlite3.connect("precos.db") as conexao:
  with closing(conexao.cursor()) as cursor:
    cursor.execute('CREATE TABLE precos(nome VARCHAR(20), preco DECIMAL)')
    cursor.execute('INSERT INTO precos(nome, preco) VALUES(?,?)', ("Sorvete", 12))
    cursor.execute('INSERT INTO precos(nome, preco) VALUES(?,?)', ("Pudim", 15))
    cursor.execute('INSERT INTO precos(nome, preco) VALUES(?,?)', ("Bolo", 10))
    cursor.execute('INSERT INTO precos(nome, preco) VALUES(?,?)', ("Taça suprema", 20))

 