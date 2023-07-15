texto = 'O rato roeu a roupa do rei de roma'
texto_tratado = texto.replace(" ", "").lower()
dicionario = {}
inicio = 1
for letra in texto_tratado:
  dicionario[letra] = dicionario.get(letra, 0) + 1

print(dicionario)