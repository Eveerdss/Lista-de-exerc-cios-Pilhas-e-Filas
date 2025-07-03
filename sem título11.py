#Jogo da Batata Quente
class Fila:
    def __init__(self):
        self.itens = []

    def enqueue(self, item):
        self.itens.append(item)

    def dequeue(self):
        if not self.esta_vazia():
            return self.itens.pop(0)

    def esta_vazia(self):
        return len(self.itens) == 0

    def tamanho(self):
        return len(self.itens)

    def frente(self):
        if not self.esta_vazia():
            return self.itens[0]

def simular_batata_quente(lista_nomes, num_passes):
    fila = Fila()

    for nome in lista_nomes:
        fila.enqueue(nome)

    print("Nome dos jogadores:", ", ".join(lista_nomes))

    while fila.tamanho() > 1:
        print(f"\nJogadores que sobraram: {fila.tamanho()}")

        for _ in range(num_passes):
            jogador = fila.dequeue()
            fila.enqueue(jogador)
            print(f"{jogador}: batata quente...")

        eliminado = fila.dequeue()
        print(f"🥔 {eliminado} queimou!")

    vencedor = fila.frente()
    print(f"\n🏆 O vencedor(a) é: {vencedor}")
    return vencedor

simular_batata_quente(["Gato", "Cachorro", "Pato", "Coelho", "Tigre"], 7)
