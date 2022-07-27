from random import randint

class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa abaixo do nível recomendado. Caixa atual {}'.format(self.caixa))
        else:
            print('O valor do caixa está ok. Caixa atual {}'.format(self.caixa))

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Empréstimo recusado. Dinheiro não disponível em caixa.')

    def add_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


#AGENCIA VIRTUAL
class AgenciaVirtual(Agencia):

    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000)
        self.caixa = 1000000
        self.caixa_paypal = 0

    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor

    def sacar_paypal(self, valor):
        self.caixa += valor
        self.caixa_paypal -= valor


#AGENCIA COMUM
class AgenciaComum(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 1000000

#AGENCIA PREMIUM
class AgenciaPremium(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 10000000

    def add_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            #add cliente
            super().add_cliente(nome, cpf, patrimonio)
        else:
            print('O cliente n tem o patrimonio mínimo para ser premium.')


if __name__ == '__main__':
    agencia1 = Agencia(991085665, 20000000, 4568)
    agencia_virtual = AgenciaVirtual('www.ag.com', 2222333, 123456610001)
    agencia_virtual.verificar_caixa()
    agencia_comum = AgenciaComum(991085665, 9999990001)
    agencia_premium = AgenciaPremium(33585167, 888888800001)

    agencia_virtual.depositar_paypal(20000)
    print(agencia_virtual.caixa)
    print(agencia_virtual.caixa_paypal)

    agencia_premium.add_cliente('Lira', '123.456.788-45', 50000000)
    print(agencia_premium.clientes)

    agencia_comum.add_cliente('irmao Lira', 4656568754, 10)
    print(agencia_comum.clientes)