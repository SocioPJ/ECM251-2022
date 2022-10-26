from src.models.pedido import Pedido
from.dao.pedido_dao import PedidoDAO
from src.controllers.item_controller import ItemController

class PedidoController:
    def __init__(self):
        pass
    def total_pedido(self,numero_pedido):
        item_pedido = PedidoDAO.get_instance().pegar_pedido(numero_pedido)
        total = 0
        item_controller = ItemController()
        for item in item_pedidos:
            item_elemento = item_controller.pegar_item(item.id_item)
            total += item_elemento.preco * item.quantidade
        return total
    
    def pegar_pedido(self,pedido):
        return PedidoDAO.get_instance().pegar_pedido(numero_pedido)
    
    def atualizar_pedido(self,pedido):
        return PedidoDAO.get_instance().atualizar_pedido(pedido)
    def deletar_pedido(self,id):
        return PedidoDAO.get_instance().deletar_pedido(id)
    def inserir_pedido(self,pedido):
        return PedidoDAO.get_instance().inserir_pedido(pedido)