from modelos.plantas import Arvore, Alface


if __name__ == '__main__':

    planta1 = Arvore(nome='Pau-de-laranja')
    planta2 = Alface(nome='Alface')

    print(planta1.ola())
    print(planta2.ola())