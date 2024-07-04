class Conta:
    def __init__(self, nmr_agencia, saldo = 0):
        self._saldo = saldo
        self.nmr_agencia = nmr_agencia

    def depositar(self, valor):
        self._saldo += valor
        print(f"Deposito feito no valor de {valor} \nValor atual {self._saldo}.")

    def sacar(self, valor):
      if valor <= self._saldo:
         self._saldo -= valor
         print(f"Saque realizado no valor de {valor}, ficando com {self._saldo}")
      else:
          print("Saldo insuficiente!!!!!!")

    def mostrar_saldo(self):
        return self._saldo

