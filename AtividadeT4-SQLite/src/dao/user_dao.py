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
                resultados.append(User(name=resultado[1], email=resultado[2],password=resultado[3]))
            self.cursor.close()
            return resultados
        except:
            print('get_all DAO erro (user_dao)')
    
    def inserir_usuario(self, user):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute("""
                INSERT INTO User (name, email, password)
                VALUES(?,?,?);
            """, (user.name,user.email,user.password))
            self.conn.commit()
            self.cursor.close()
        except:
            print("Erro inserir_usuario user_dao")
            
    def deletar_usuario(self, email):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                DELETE FROM User 
                WHERE email = '{email}'
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
                UPDATE User 
                SET name = ?,
                    email = ?,
                    password = ?
                WHERE 
                    email = ?;
            """,(user.name,user.email,user.password,user.email))
            self.conn.commit()
            self.cursor.close()
        except:
            print('Erro DAO atualizar usuario')
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
    
    def procurar_todos_por_email(self,email):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM User
            WHERE email LIKE '{email}%';
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(User(name=resultado[1], email=resultado[2], password=resultado[3]))
        self.cursor.close()
        return resultados