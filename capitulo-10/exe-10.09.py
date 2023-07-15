class Estado:
  def __init__(self, nome, sigla):
    self.nome = nome.title()
    self.sigla = self.valida_sigla(sigla)
    self.cidades = []
    self.populacao = 0
  
  def valida_sigla(self, sigla):
    if(len(sigla) != 2):
      raise ValueError('Quantidade de caracteres para a sigla inválidos')
    return sigla.upper()
  
  def adiciona_cidade(self, cidade):
    self.cidades.append(cidade)
  
  def exibe_cidades(self):
    texto = ''
    for cidade in self.cidades:
      texto += cidade.nome+", "
    return texto
  
  def calcula_populacao(self):
    for cidade in self.cidades:
      self.populacao += cidade.populacao
    return self.populacao
    
  
  def __str__(self) -> str:
    return f'Estado: {self.nome} \nSigla: {self.sigla} \nCidades: {self.exibe_cidades()} \nPopulação: {self.calcula_populacao()} \n'


class Cidade:
  def __init__(self, nome, populacao):
    self._nome = nome.title()
    self.populacao = self.validacao_populacao(populacao)
  
  def validacao_populacao(self, quantidade):
    try:
      quantidade = int(quantidade)
    except ValueError:
      raise ValueError('Não é permitida a entrada de caracteres como valor da população')
    else:
      if(quantidade <= 0):
        raise ValueError('Não é aceito valor menor ou igual a zero para a população de uma cidade!')
      return quantidade
  
  @property
  def nome(self):
    return self._nome
  
  def __str__(self) -> str:
    return f'{self.nome}'

class Pais:
  def __init__(self, nome, estados):
    self.nome = nome.title()
    self.estados = estados
  
  def __getitem__(self, index):
    return self.estados[index]

  def __str__(self) -> str:
    return f'{self.nome}'
  
i = 1
estados = []
while(i != 0):
  print()
  print('Para adicionar um estado digite - "1"')
  print('Para sair digite - "0"')
  i = input('Opção: ')
  if(i == '1'):
    print()
    nome_estado = input('Digite o nome do estado: ')
    sigla = input('Digite a sigla do estado: ')
    print()
    try:
      estado = Estado(nome_estado, sigla)
    except ValueError as e:
      print(f'Erro ao criar um estado: {e}')
    else:
      print(f'Estado "{estado.nome}" adicionado com sucesso')
      op = 1
      while(op != 0):
        print('Para adicionar uma cidade - "1"')
        print('Para sair digite - "0"')
        op = input('Opção: ')
        if(op == '1'):
          print()
          nome_cidade = input('Digite o nome da cidade: ')
          populacao = input('Digite a quantidade da população: ')
          print()
          try:
            cidade = Cidade(nome_cidade, populacao)
          except ValueError as e:
            print(f'Erro ao criar uma cidade: {e}')
          else:
            estado.adiciona_cidade(cidade)
            print(f'Cidade "{cidade.nome}" adicionada com sucesso')
        elif(op == '0'):
          break
        else:
          print('Valor da opção inválido')
       
      estados.append(estado)
  elif(i == '0'):
    break
  else:
    print('Valor da opção inválido')

pais = Pais('Brasil', estados)
print('**************')
for p in pais:
  print(p)
    