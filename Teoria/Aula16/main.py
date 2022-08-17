from modelos.plantas import Arvore, Alface
from modelos.documentos import Document, EMail, Book

def run_system():
    doc1 = Document()
    doc2 = EMail(authors = ['João', 'Maria'])
    doc3 = Book(authors = ['Murilo Zanini'])
    print(doc2.get_authors())
    print(doc3)

if __name__ == '__main__':

    planta1 = Arvore(nome='Pau-de-laranja')
    planta2 = Alface(nome='Alface')

    print(planta1.ola())
    print(planta2.ola())
    run_system()