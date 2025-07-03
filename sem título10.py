#Fila de Atendimento
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def esta_vazia(self):
        return self.inicio is None

    def enqueue(self, valor):
        novo_no = No(valor)
        if self.esta_vazia():
            self.inicio = self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no

    def dequeue(self):
        if self.esta_vazia():
            return None
        valor = self.inicio.valor
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        return valor

    def mostrar(self):
        atual = self.inicio
        fila_str = []
        while atual:
            fila_str.append(atual.valor)
            atual = atual.proximo
        print("Fila atual:", " -> ".join(fila_str) if fila_str else "Não tem ninguém")

def novo_cliente(fila, nome_cliente):
    fila.enqueue(nome_cliente)
    print(f"{nome_cliente} entrou na fila.")
    fila.mostrar()

def atender_cliente(fila):
    cliente = fila.dequeue()
    if cliente:
        print(f"Em atendimento: {cliente}")
    else:
        print("Nenhum cliente.")
    fila.mostrar()

fila_atendimento = Fila()

novo_cliente(fila_atendimento, "Gato")
novo_cliente(fila_atendimento, "Cachorro")
novo_cliente(fila_atendimento, "Papagaio")

atender_cliente(fila_atendimento)

novo_cliente(fila_atendimento, "Coelho")

atender_cliente(fila_atendimento)
atender_cliente(fila_atendimento)
atender_cliente(fila_atendimento)
atender_cliente(fila_atendimento)  
