from src.models.product import Product
import sqlite3

class ProductDAO:
    
    _instance = None

    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = ()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('../database/sqlite.db')
        
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
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            INSERT INTO Itens (id, name, price, url)
            VALUES(?,?,?,?);
        """, (item.id,item .name,item.price,item.url))
        self.conn.commit()
        self.cursor.close()
    