def opcoes_validas(validas):
  validas = validas.lower()
  while True:
    letra = input('Digite uma letra: ').lower()
    if letra in validas:
      print('Opcao valida')
      break
    else:
      print('Opcao invalida')
    
validas = 'aeiou'
opcoes_validas(validas)
