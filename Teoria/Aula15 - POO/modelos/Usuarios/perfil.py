from datetime import date
class Perfil:
    def __init__(self,nome):
        self._nome = nome
        self._foto = None
        self.data_nascimento = date.today()
        self._descricao = 'Sem descrição no momento.'
        self._telefone = ''
    
    def set_nome(self,nome):
        self._nome = nome
    
    def set_foto(self,foto):
        self._foto = foto
    
    def set_descricao(self,descricao):
        self._descricao = descricao
    
    def set_telefone(self,telefone):
        self._telefone = telefone
        
    def set_data_nascimento(self,data_nascimento):
        self.set_data_nascimento = data_nascimento
    
    def get_nome(self):
        return self._nome

    def get_foto(self):
        return self._foto
    
    def get_descricao(self):
        return self._descricao
    
    def get_telefone(self):
        return self._telefone
        