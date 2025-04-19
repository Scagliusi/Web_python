import pyodbc
import hashlib

def conectar():
    conexao = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};' 
        'SERVER=localhost;'
        'DATABASE=SistemaLogin;'
        'Trusted_Connection=yes;'
    )
    return conexao

def criar_tabela_usuario():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
            IF NOT EXISTS(SELECT * FROM sysobjects WHERE name='usuarios' AND xtype='U')
            CREATE TABLE usuarios (
                id INT identity primary key,
                username VARCHAR(255) UNIQUE,
                password_hash VARCHAR(255)
            )
        '''
        )
    conn.commit()
    conn.close()