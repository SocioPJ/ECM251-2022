from modelos.plantas import Arvore, Alface
from modelos.documentos import Document, EMail, Book

def run_system():
    doc1 = Document()
    doc2 = EMail(authors = ['João'], to = 'jpsocio@hotmail.com')
    doc3 = Book(authors = ['Murilo Zanini'], title = 'Python para Zumbis')
    print(doc2)
    # print(doc3)

if __name__ == '__main__':

    # planta1 = Arvore(nome='Pau-de-laranja')
    # planta2 = Alface(nome='Alface')

    # print(planta1.ola())
    # print(planta2.ola())
    run_system()