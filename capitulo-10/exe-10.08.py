class Cliente:
  def __init__(self, nome, telefone):
    self.nome = nome
    self.telefone = telefone
  
  def __str__(self) -> str:
    return f'Nome: {self.nome} com telefone: {self.telefone}'

class Conta:
  def __init__(self, clientes, numero, saldo = 0):
    self.saldo = 0
    self.clientes = clientes
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
    print(f'CC N {self.numero}, saldo: {self.saldo:.2f}')
    print('Proprietario(s) da conta: ')
    for cliente in self.clientes:
      print(cliente)
  
  def extrato(self):
    print(f'Extrato CC N {self.numero}')
    for o in self.operacoes:
      print(f'{o[0]}: {o[1]}')
    print(f'Saldo: {self.saldo:.2f}')

joao = Cliente('João', '999999999')
jose = Cliente('José', '888888888')
conta1 = Conta([joao, jose], 4, 500)
conta1.resumo()