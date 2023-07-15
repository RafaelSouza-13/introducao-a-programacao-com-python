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

rafael = Cliente('Rafa', '999999999')
conta_rafa = Conta(rafael, 23, 100)

conta_rafa.resumo()
conta_rafa.deposito(50)
conta_rafa.saque(10000)
conta_rafa.extrato()