from models.user import User
from dao.user_dao import UserDAO


class UserController():
    def __init__(self) -> None:
        # #Carrega os dados dos usuários
        # self.users = [
        #     User(name="joao", password="arroz", email="joao@mail.com"),
        #     User(name="joao2", password="arroz2", email="joao@amaarroz.com"),
        #     User(name="tais", password="petacular", email="tais_@condida.com"),
        # ]
        pass
    
    def inserir_usuario(self, usuario) -> bool:
        try:
            UserDAO.get_instance().inserir_usuario(usuario)
        except:
            return False 
        return True
    
    def pegar_todos_usuarios(self) -> list[UserDAO]:
        try: 
            return UserDAO.get_instance().get_all()
        except:
            print("Erro ao pegar todos itens")
            
    def deletar_usuario(self, id) -> bool:
        try:
            return UserDAO.get_instance().deletar_usuario(id)
        except:
            print(" Erro ao deletar usuario ")
    
    def atualizar_item(self,usuario):
        try:
            return UserDAO.get_instance().atualizar_usuario(usuario)
        except:
            print("Erro ao atualizar item")
    
    def buscar_todos_itens_nome(self, name) -> list[User]:
        itens = UserDAO.get_instance().procurar_todos_por_nome(name)
        return itens
    
    def checkUser(self,user):
        return user in self.users

    def checkLogin(self, email, password):
        user_teste = User(name=None, password=password, email=email)
        for user in UserDAO.get_instance().get_all():
            if user.email == user_teste.email and user.password == user_teste.password:
                return True            
        return False
    
    def getName(self, name):
        for user in self.users:
            if user.name == name:
                return user.name
        return None