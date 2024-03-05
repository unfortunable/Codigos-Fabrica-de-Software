# verificar se um número é par ou ímpar

numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print('É par')
else:
    print('É ímpar')

# loop com while 

n = 5
while n > 0:
    n -= 1
    print(n)

# loop com for

frutas = ['Banana', 'Maçã', 'Abacate']
for x in frutas:
    print(x)

# função que retorne algo

def media(y,z,b):
    return(y + z + b)/3

print(media(4,9,9))

# função que não retorna nada

def subt(l,g):
    return(l-g)


class Animal:
    def __init__(self, raca, porte):
        self.raca = raca
        self.porte = porte

class Cachorro(Animal):
    def som(self):
        print('Auau')
class Gato(Animal):
    def som(self):
        print('Miau')
    
meu_cachorro = Cachorro("Vira-Lata", "Médio")
meu_gato = Gato("Vira-Lata", "Médio")
meu_cachorro.som()
meu_gato.som()
