# Criando nossa 1ª Classe em Python
# Sempre que você quiser criar uma classe, você vai fazer:
#
# class Nome_Classe:
#
# Dentro da classe, você vai criar a "função" (método) __init__
# Esse método é quem define o que acontece quando você cria uma instância da Classe
#
# Vamos ver um exemplo para ficar mais claro, com o caso da Televisão que a gente vinha comentando

#classes

class TV:

    cor = 'preta'

    def __init__(self, size):
        self.ligada = False
        self.tamanho = size
        self.canal = "Netflix"
        self.volume = 10

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal
        pass

tv_sala = TV(size=55)
tv_quarto = TV(size=70)

print(tv_sala.cor)
print(tv_quarto.cor)