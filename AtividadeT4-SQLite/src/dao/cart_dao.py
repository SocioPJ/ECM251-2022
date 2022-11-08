from models.cart import Cart
import sqlite3
import streamlit as st

class CartDAO:
  
    _instance = None

    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = CartDAO()
        return cls._instance

    def _connect(self):
        try:
            self.conn = sqlite3.connect('./database/sqlite.db', check_same_thread= False)
            print('Conectado')
        except:
            print("Erro ao conectar")
        
    def get_all(self):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute("""
                SELECT * FROM Cart;
            """)
            resultados = []
            for resultado in self.cursor.fetchall():
                resultados.append(Cart(product_id=resultado[0], product_name=resultado[1], product_price=resultado[2],product_url=resultado[3], quantity=resultado[4]))
            self.cursor.close()
            return resultados
        except:
            print('get_all DAO erro')
    
    def inserir_item_carrinho(self, item_carrinho):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute("""
                INSERT INTO Cart (product_id, product_name, product_price, product_url, quantity)
                VALUES(?,?,?,?,?);
            """, (item_carrinho.product_id,item_carrinho.product_name,item_carrinho.product_price,item_carrinho.product_url,item_carrinho.quantity))
            self.conn.commit()
            self.cursor.close()
        except:
            print("Erro inserir_item cart_dao")
            
    def deletar_item_carrinho(self, id):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                DELETE FROM Cart 
                WHERE product_id = '{id}'
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
    
    def atualizar_quantidade_item_carrinho(self, id,quantidade):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
            UPDATE Cart 
            SET 
                quantity = ?
            WHERE product_id = ?;
            """,(quantidade,id))
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
    
    def pegar_quantidade_item_carrinho(self, id):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT quantity FROM Cart
            WHERE product_id = '{id}';
        """)
        quantidade = None
        resultado = self.cursor.fetchone()
        if resultado != None:
            quantidade = resultado[0]
        self.cursor.close()
        return quantidade
    
    def pegar_preco_item_carrinho(self, id):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT product_price FROM Cart
            WHERE product_id = '{id}';
        """)
        price = None
        resultado = self.cursor.fetchone()
        if resultado != None:
            price = resultado[0]
        self.cursor.close()
        return price
    
    # def procurar_todos_por_nome(self,name):
    #     self.cursor = self.conn.cursor()
    #     self.cursor.execute(f"""
    #         SELECT * FROM Products
    #         WHERE nome LIKE '{name}%';
    #     """)
    #     resultados = []
    #     for resultado in self.cursor.fetchall():
    #         resultados.append(Product(id=resultado[0], name=resultado[1], price=resultado[2],url = resultado[3]))
    #     self.cursor.close()
    #     return resultados