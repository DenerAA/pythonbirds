class Pessoa:
    olhos = 2

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
    luciano.sobrenome = 'Luiz Filho'
    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.sobrenome)
    print(luciano.__dict__)
    print(luiz.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(luiz.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(luiz.olhos))