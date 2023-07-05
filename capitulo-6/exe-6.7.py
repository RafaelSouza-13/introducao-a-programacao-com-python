expressao = input('Digite a expressao com parenteses: ')
pilha = []
i = 0
while(i < len(expressao)):
  if(expressao[i] == '('):
    pilha.append(expressao[i])
  elif(expressao[i] == ')'):
    if(len(pilha) == 0):
      print('Expressao incorreta')
      break
    else:
      pilha.pop(-1)
  i += 1
if(len(expressao) == i):
  if(len(pilha) == 0):
    print('Expressao correta')
  else:
    print('Expressao incorreta')