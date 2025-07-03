# Simulador de Histórico de Navegação
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

class Navegador:
    def __init__(self, pagina_inicial):
        self.historico_voltar = Pilha()
        self.historico_avancar = Pilha()
        self.pagina_atual = pagina_inicial
        print(f"Navegador iniciado em: {self.pagina_atual}")

    def visitar_pagina(self, url):
        self.historico_voltar.push(self.pagina_atual)
        self.pagina_atual = url
        self.historico_avancar = Pilha()  # limpa o histórico de avançar
        print(f"Visitando: {self.pagina_atual}")

    def voltar(self):
        if not self.historico_voltar.esta_vazia():
            self.historico_avancar.push(self.pagina_atual)
            self.pagina_atual = self.historico_voltar.pop()
            print(f"Voltando para: {self.pagina_atual}")
        else:
            print("Não há páginas para voltar.")

    def avancar(self):
        if not self.historico_avancar.esta_vazia():
            self.historico_voltar.push(self.pagina_atual)
            self.pagina_atual = self.historico_avancar.pop()
            print(f"Avançando para: {self.pagina_atual}")
        else:
            print("Não há páginas para avançar.")

nav = Navegador("inicial.com")
nav.visitar_pagina("google.com")
nav.visitar_pagina("youtube.com")
nav.visitar_pagina("github.com")

nav.voltar()
nav.voltar()

nav.avancar()
nav.visitar_pagina("wikipedia.org")
nav.voltar()


