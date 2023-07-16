import sqlite3
from contextlib import closing

with sqlite3.connect("precos.db") as conexao:
  with closing(conexao.cursor()) as cursor:
    cursor.execute('SELECT nome, preco FROM precos')
    resultados = cursor.fetchall()
    for resultado in resultados:
      print(f'Nome: {resultado[0]} com preço: {resultado[1]}')

