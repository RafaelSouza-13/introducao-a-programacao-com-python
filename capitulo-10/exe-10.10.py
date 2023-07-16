class Cliente:
  def __init__(self, nome, telefone):
    self.nome = nome
    self.telefone = telefone

class Conta:
  def __init__(self, cliente, numero, saldo = 0):
    self.saldo = 0
    self.cliente = cliente
    self.numero = numero
    self.operacoes = []
    self.deposito(saldo)
    
  def deposito(self, valor):
    if(valor < 0):
      print('Valor invalido para essa transação')
    else:
      self.saldo += valor
      self.operacoes.append(["Deposito", valor])
  
  def saque(self, valor):
    if(self.saldo < valor):
      print('Voce não possui saldo o bastante para essa operação')
    else:
      self.saldo -= valor
      self.operacoes.append(["Saque", valor])
  
  def resumo(self):
    print(f'CC N {self.numero} saldo: {self.saldo:.2f} titular: {self.cliente.nome}')
  
  def extrato(self):
    print(f'Extrato CC N {self.numero}')
    for o in self.operacoes:
      print(f'{o[0]}: {o[1]}')
    print(f'Saldo: {self.saldo:.2f}')

class ContaEspecial(Conta):
  def __init__(self, cliente, numero, saldo=0, limite=0):
    super().__init__(cliente, numero, saldo)
    self.limite = limite
  
  def saque(self, valor):
    if self.saldo + self.limite >= valor:
      self.saldo -= valor
      self.operacoes.append(['SAQUE', valor])
      return True
    else:
      return False