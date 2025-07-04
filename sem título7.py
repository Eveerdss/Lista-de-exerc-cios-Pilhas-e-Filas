#Invertendo uma Palavra com Pilha
class Pilha:
    def __init__(self):
        self.itens = []

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        if not self.esta_vazia():
            return self.itens.pop()

    def esta_vazia(self):
        return len(self.itens) == 0

def inverter_string(texto):
    pilha = Pilha()

    for letra in texto:
        pilha.push(letra)

    invertida = ''
    while not pilha.esta_vazia():
        invertida += pilha.pop()

    return invertida

entrada = "Evellyn Rodrigues da Silva"
saida = inverter_string(entrada)
print("Palavra:", entrada)
print("Palavra invertida:", saida)


