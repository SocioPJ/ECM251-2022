from controllers.user_controller import UserController
from models.user import User

controller = UserController()

controller.deletar_usuario(0)
controller.deletar_usuario(1)
controller.deletar_usuario(2)
controller.deletar_usuario(3)
controller.deletar_usuario(4)
controller.deletar_usuario(5)
controller.deletar_usuario(6)
controller.deletar_usuario(7)
controller.deletar_usuario(8)
controller.deletar_usuario(9)
controller.deletar_usuario(10)
# controller.inserir_usuario(User(0,'joao','jpsocio@hotmail.com','arroz'))
# controller.inserir_usuario(User(1,'ana','ana@hotmail.com','cocada'))
# controller.inserir_usuario(User(2,'murilo','murilo@hotmail.com','farofa'))
# controller.deletar_usuario(0)
# print(controller.pegar_todos_usuarios())
# for usuario in controller.pegar_todos_usuarios():
#     print(usuario.id)
    