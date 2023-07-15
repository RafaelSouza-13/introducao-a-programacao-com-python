def validacao_string(palavra, maximo, minimo):
  tamanho = len(palavra)
  if tamanho <= maximo and tamanho >= minimo:
    return True
  return False

palavra = input('Digite um texto: ')
MAXIMO = 20
MINIMO = 5
resultado = validacao_string(palavra, MAXIMO, MINIMO)
print(resultado)