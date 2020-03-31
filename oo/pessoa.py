class Pessoa:
    def __init__(self, *filhos, nome=None, idade=27):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    luciano = Pessoa(nome='Luciano')
    luiz = Pessoa(luciano,nome='Luiz')
    print(luiz.nome)
    for f in luiz.filhos:
        print(f.nome)