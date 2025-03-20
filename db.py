import sqlite3

#criar o banco de dados e a tabela
def init_db():
    conn = sqlite3.connect('api_compromissos\\base_dados\\compromissos.db') 
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS compromissos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        data TEXT NOT NULL,
        hora TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# adicionar um compromisso n
def adicionar_compromisso_bd(titulo, data, hora):
    conn = sqlite3.connect('api_compromissos\\base_dados\\compromissos.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO compromissos (titulo, data, hora)
    VALUES (?, ?, ?)
    ''', (titulo, data, hora))
    conn.commit()
    conn.close()

# listar todos os compromissos
def listar_compromissos_bd():
    conn = sqlite3.connect('api_compromissos\\base_dados\\compromissos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM compromissos')
    compromissos = cursor.fetchall()
    conn.close()
    return compromissos

#excluindo compromisso
def excluir_compromisso_bd(titulo):
    conn = sqlite3.connect('api_compromissos\\base_dados\\compromissos.db')
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM compromissos WHERE titulo = ?''', (titulo,))
    conn.commit()
    conn.close()
