class ContaBancaria:
    def __init__(self, numero, titular, saldo) -> None:
        self._numero = numero
        self._titular = titular
        self._saldo = saldo

    def get_numero(self):
        return self._numero

    def get_titular(self):
        return self._titular

    def get_saldo(self):
        return self._saldo

    def set_saldo(self, novo_saldo):
        if novo_saldo >= 0:
            self._saldo = novo_saldo
        else:
            print("O saldo não pode ser negativo.")

    def depositar(self, valor):
        self._saldo += valor
        return self._saldo
    
    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
        else:
            print('Valor indisponível.')
            
        return self._saldo

# Exemplo de uso
conta1 = ContaBancaria(123, 'Joao', 100)
conta1.depositar(1000)

# Utilizando o método setter
conta1.set_saldo(500)

# Imprimir informações da conta
print(f"Número da conta: {conta1.get_numero()}")
print(f"Titular da conta: {conta1.get_titular()}")
print(f"Saldo da conta: {conta1.get_saldo()}")
