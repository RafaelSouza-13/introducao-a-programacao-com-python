def fibonacci(quantidade_termos):
  antecessor = 1
  sucessor = 2
  total = 0
  if quantidade_termos == 0:
    return 0
  elif quantidade_termos == 1 or quantidade_termos == 2:
    return 1
  else:
    x = 3
    while(x <= quantidade_termos):
      total = antecessor + sucessor
      antecessor = sucessor
      sucessor = total
      x += 1
    return total
  
fb = fibonacci(6)
print(fb)
      