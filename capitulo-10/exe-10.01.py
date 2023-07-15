class Televisao:
  def __init__(self, marca, tamanho):
    self.ligada = False
    self.canal = 2
    self.marca = marca
    self.tamanho = tamanho
  
  def __str__(self) -> str:
    return f'Televisão de marca: {self.marca} com tamanho: {self.tamanho}'

tv1 = Televisao('Sony', 40)
tv2 = Televisao('LG', 30)
print(tv1)
print(tv2)