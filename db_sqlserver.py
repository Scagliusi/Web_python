import pyodbc
import hashlib
import os
from dotenv import load_dotenv

def conectar():
    conexao = pyodbc.connect(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={os.getenv('DB_SERVER')};"
        f"DATABASE={os.getenv('DB_DATABASE')};"
        "Trusted_Connection=yes;"
        f"UID={os.getenv('DB_USERNAME')};"
        f"PWD={os.getenv('DB_PASSWORD')};"
        "Encrypt=no;"
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
