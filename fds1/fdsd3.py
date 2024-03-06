## Praticing before the class starts

#Definindo a classe computador e seus parametros
class Computador():
    def __init__(self, placaVideo, memoriaRam, processador):
        self.placaVideo = placaVideo
        self.memoriaRam = memoriaRam
        self.processador = processador
    
    #função ligar
    def Ligar(self):
        return'Ligando...'

    #função de informações
    def Info(self):
        return'Esse computador tem', self.placaVideo, self.memoriaRam, self.processador

#Modulos baseados na classe Computador
computador1 = Computador('RTX 3050', '16gb', 'i7 1400k')
computador2 = Computador('Rx 550', '32gb', 'Ryzen 7 7700x')
computador3 = Computador('Vega 7', '8gb', 'Intel Xeon')

#exibindo na tea alguns dados sobre os modulos
print(computador1.Ligar())
computador2.Ligar()
computador3.Ligar()
print('O Primeiro computador tem',computador1.memoriaRam)
print('O Segundo computador tem um', computador2.processador)
print('O Terceiro computador tem um', computador3.placaVideo)
print(computador1.Info())

# 