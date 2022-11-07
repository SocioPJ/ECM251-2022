from controllers.user_controller import UserController
from models.user import User

controller = UserController()

usuario = controller.buscar_todos_usuarios_email("jpsocio@hotmail.com")
print(usuario[0])

# new_name_input = input('Digite novo nome: ')
# new_password_input = input('Digite nova senha: ')

# usuario[0].name = 'gato'
usuario[0].password = 'jose'

print(usuario)
print(usuario[0])
print(usuario[0].name)
print(usuario[0].password)
print(usuario[0].email)
usuario = usuario[0]
print(usuario.password)
controller.atualizar_usuario(usuario)
# print(controller.atualizar_usuario(usuario[0]))
# usuario = controller.buscar_todos_usuarios_email("jpsocio@hotmail.com")
# print(usuario[0])









# controller.deletar_usuario('jpsocio@hotmail.com')
# controller.deletar_usuario('ana@hotmail.com')
# controller.deletar_usuario('murilo@hotmail.com')


# controller.inserir_usuario(User('joao','jpsocio@hotmail.com','arroz'))
# controller.inserir_usuario(User('ana','ana@hotmail.com','cocada'))
# controller.inserir_usuario(User('murilo','murilo@hotmail.com','farofa'))
#print(controller.pegar_todos_usuarios()[0].email)
# for i in range(len(controller.pegar_todos_usuarios())):
#     print(controller.pegar_todos_usuarios()[i].email)

# controller.inserir_usuario(User('joao',email_input,'arroz'))
# for i in range(len(controller.pegar_todos_usuarios())):
#     if email_input != controller.pegar_todos_usuarios()[i].email:
#         print('Email não cadastrado')
#         controller.inserir_usuario(User('joao',email_input,'arroz'))
#     else:
#         print('Email já cadastrado,tente outro')
#         break
# emails = []
# for i in range(len(controller.pegar_todos_usuarios())):
    
#     emails.append(controller.pegar_todos_usuarios()[i].email)
    
# print(emails)
# email_input = input("Email :")
# if email_input not in emails:
#     print('Email não cadastrado')
#     controller.inserir_usuario(User('joao',email_input,'arroz'))
# else:
#     print('Email já cadastrado')
# controller.deletar_usuario(0)
# print(controller.pegar_todos_usuarios())
# for usuario in controller.pegar_todos_usuarios():
#     print(usuario.id)
    