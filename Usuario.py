import hashlib
from db_sqlserver import conectar

class Usuario:

    def __init__(self,id,username,password_hash):
        self.id = id
        self.username =username
        self.password_hash= password_hash

    def verificar_senha(self, senha_digitada):
        hash_digitado = hashlib.sha256(senha_digitada.encode()).hexdigest()
        return self.password_hash == hash_digitado

    @classmethod
    def buscar_por_username(cls, username):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT id,username,password_hash FROM usuarios WHERE username = ?',(username))
        row = cursor.fetchone()
        conn.close

        if row:
            return cls(*row) ## * serve como um desempacotador de tuplas 
        return None
    
    @classmethod ##Um @classmethod é chamado antes de qualquer objeto ser criado, e usa cls(...) para instanciar (criar) um novo objeto da própria classe, retornando ele no final.
    def criar_usuario(cls, username, senha):
        if cls.buscar_por_username(username):
            raise ValueError("Usuário já existe.")

        hashed = hashlib.sha256(senha.encode()).hexdigest()
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO usuarios (username, password_hash) VALUES (?, ?)', (username, hashed))
        conn.commit()

        # Recupera o id do usuário recém-criado
        cursor.execute('SELECT @@IDENTITY') 
        new_id = cursor.fetchone()[0]
        conn.close()

        return cls(new_id, username, hashed)

