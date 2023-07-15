class Televisao:
  def __init__(self, marca, tamanho, canal):
    self.ligada = False
    self.canal = canal
    self.marca = marca
    self.tamanho = tamanho
  
  def __str__(self) -> str:
    return f'Televisão de marca: {self.marca} com tamanho: {self.tamanho}'