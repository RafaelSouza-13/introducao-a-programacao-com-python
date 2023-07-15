class Televisao:
  def __init__(self, marca, tamanho, max, min):
    self.ligada = False
    self.marca = marca
    self.tamanho = tamanho
    self.canal_maximo = self.tratamento_max_min(max, min)
    self.canal_minimo = self.tratamento_canal_negativo(min)
    self.canal = self.canal_minimo
  
  def mudar_canal_cima(self):
    if(self.canal < self.canal_maximo):
      self.canal += 1
    else:
      self.canal = self.canal_minimo
      
  def mudar_canal_baixo(self):
    if(self.canal > self.canal_minimo):
      self.canal -= 1
    else:
      self.canal = self.canal_maximo
      
  def tratamento_max_min(self, max, min):
    if(min >= max):
      raise ValueError('Canal minimo maior ou igual ao canal maximo')
    return max
  
  def tratamento_canal_negativo(self, canal):
    if(canal <= 0):
      raise ValueError('Não é permitida a entrava de valores negativos ou 0')
    return canal
  
  @property
  def mostrar_canal_atual(self):
    return f'Canal atual: {self.canal}'
  
  def lista_canais(self):
    print(f'Canais disponiveis: ', end="")
    for canal in range(self.canal_minimo, self.canal_maximo + 1):
      print(canal, end=", ")
  
  def __str__(self) -> str:
    return f'Televisão de marca: {self.marca} com tamanho: {self.tamanho}'

try:
  tv = Televisao('Sony', 30, 5, 2)
except ValueError as e:
  print(f'Erro ao criar a instancia de televisão: {e}')
else:
  print(tv)
  print(tv.mostrar_canal_atual)
  for i in range(5):
    tv.mudar_canal_cima()
    print(tv.mostrar_canal_atual)

  print('/////////////////')
  print(tv)
  print(tv.mostrar_canal_atual)
  for i in range(5):
    tv.mudar_canal_baixo()
    print(tv.mostrar_canal_atual)

