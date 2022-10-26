class Pedido:
    def __init__(self,id,id_item,quantidade, numero_pedido, id_cliente, data_hora):
        self.id = id
        self.id_item = id_item
        self.quantidade = quantidade
        self.numero_pedido = numero_pedido
        self.id_cliente = id_cliente
        self.data_hora = data_hora
        
    def __str__(self):
        return f'Pedido: id:{self.id}, - Item: {self.id_item}, - Quantidade: {self.quantidade}, - Numero do Pedido: {self.numero_pedido}, - Id do Cliente: {self.id_cliente}, - Data e Hora: {self.data_hora}'