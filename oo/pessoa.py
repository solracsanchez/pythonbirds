class Pessoa:
    def __init__(self, *filhos, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Olá'


if __name__ == '__main__':

    for v in range(int(input(f'Digite o numero filhos:'))):
        filho = Pessoa()
        filho.nome = input(f'Digite o nome do filho {v+1}: ')
        filho.idade = int(input(f'Digite a idade do filho {v+1}: '))
    pai = Pessoa(filho, nome='Mariano')
    print(pai.cumprimentar())
    print(pai.nome)
    print(pai.idade)
    for filho in pai.filhos:
        print(filho.nome)
        print(filho.idade)

