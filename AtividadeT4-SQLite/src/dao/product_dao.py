
from models.product import Product
import sqlite3

class ProductDAO:
    
    _instance = None

    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = ProductDAO()
        return cls._instance

    def _connect(self):
        try:
            self.conn = sqlite3.connect('./database/sqlite.db')
            print('Conectado')
        except:
            print("Erro ao conectar")
        
    def get_all(self):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute("""
                SELECT * FROM Products;
            """)
            resultados = []
            for resultado in self.cursor.fetchall():
                resultados.append(Product(id=resultado[0], nome=resultado[1], preco=resultado[2],url=resultado[3]))
            self.cursor.close()
            return resultados
        except:
            print('get_all DAO erro')
    
    def inserir_item(self, item):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute("""
                INSERT INTO Products (id, name, price, url)
                VALUES(?,?,?,?);
            """, (item.id,item.name,item.price,item.url))
            self.conn.commit()
            self.cursor.close()
        except:
            print("ID Produto ja inserido antes, tente outro ID")
            
    def deletar_item(self, id):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                DELETE FROM Products 
                WHERE id = '{id}'
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
    
    def atualizar_item(self, item):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE Products SET
                name = '{item.name}',
                price = {item.price},
                url = {item.url}
                WHERE id = '{item.id}'
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
    
    def pegar_item(self, id):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Products
            WHERE id = '{id}';
        """)
        item = None
        resultado = self.cursor.fetchone()
        if resultado != None:
            item = Product(id=resultado[0], name=resultado[1], price=resultado[2], url=resultado[3])
        self.cursor.close()
        return item
    
    def search_all_for_name(self,name):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Products
            WHERE name LIKE '{name}%';
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Product(id=resultado[0], name=resultado[1], price=resultado[2],url = resultado[3]))
        self.cursor.close()
        return resultados