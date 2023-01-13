import itertools
import sqlite3

# Cria uma conexão com o banco de dados
conn = sqlite3.connect('combinations.db')
cursor = conn.cursor()

# Cria a tabela 'combinations' no banco de dados
cursor.execute('''
    CREATE TABLE IF NOT EXISTS combinations (
        id INTEGER PRIMARY KEY,
        combination TEXT
    )
''')

# Gera todas as combinações de 6 números entre 1 e 60
combinations = list(itertools.combinations(range(1, 61), 6))

# Insere cada combinação na tabela 'combinations'
for i, combination in enumerate(combinations):
    cursor.execute(f"INSERT INTO combinations (id, combination) VALUES({i+1}, '{combination}')")

# Salva as alterações no banco de dados e fecha a conexão
conn.commit()
conn.close()
