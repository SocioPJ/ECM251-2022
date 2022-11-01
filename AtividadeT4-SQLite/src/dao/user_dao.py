from models.user import User
import sqlite3
import streamlit as st

class UserDAO:
  
    _instance = None

    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = UserDAO()
        return cls._instance

    def _connect(self):
        try:
            self.conn = sqlite3.connect('./database/sqlite.db', check_same_thread= False)
            print('Conectado')
        except:
            print("Erro ao conectar (user_dao)")
        
    def get_all(self):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute("""
                SELECT * FROM User;
            """)
            resultados = []
            for resultado in self.cursor.fetchall():
                resultados.append(User(id=resultado[0], name=resultado[1], email=resultado[2],password=resultado[3]))
            self.cursor.close()
            return resultados
        except:
            print('get_all DAO erro (user_dao)')
    
    def inserir_usuario(self, user):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute("""
                INSERT INTO User (id, name, email, password)
                VALUES(?,?,?,?);
            """, (user.id,user.name,user.email,user.password))
            self.conn.commit()
            self.cursor.close()
        except:
            print("Erro inserir_usuario product_dao")
            
    def deletar_usuario(self, id):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                DELETE FROM User 
                WHERE id = '{id}'
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
    
    def atualizar_usuario(self, user):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE User SET
                id = {user.id}
                name = '{user.name}',
                price = {user.price},
                url = {user.url}
                WHERE id = '{user.id}'
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
    
    def pegar_usuario(self, id):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM User
            WHERE id = '{id}';
        """)
        item = None
        resultado = self.cursor.fetchone()
        if resultado != None:
            item = User(id=resultado[0], name=resultado[1], email=resultado[2], password=resultado[3])
        self.cursor.close()
        return item
    
    def procurar_todos_por_nome(self,name):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM User
            WHERE nome LIKE '{name}%';
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(User(id=resultado[0], name=resultado[1], email=resultado[2], password=resultado[3]))
        self.cursor.close()
        return resultados