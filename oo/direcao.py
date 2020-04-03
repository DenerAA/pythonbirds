class Direcao:
    direcao= ['Norte', 'Leste', 'Sul', 'Oeste']

    def __init__(self):
        self.valor= self.direcao[0]

    def girar_a_direita(self):
        posicao = self.direcao.index(self.valor) + 1
        self.valor = self.direcao[0 if posicao >= len(self.direcao) else posicao]

    def girar_a_esquerda(self):
        posicao = self.direcao.index(self.valor) - 1
        self.valor = self.direcao[len(self.direcao) - 1 if posicao < 0 else posicao]

