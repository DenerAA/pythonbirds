class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=27):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 50

    @classmethod
    def nome_e_atributos_de_classes(cls):
        return f'[{cls} - olhos {cls.olhos}]'

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
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classes(), luciano.nome_e_atributos_de_classes())