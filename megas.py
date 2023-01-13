import itertools
import sqlite3

# Cria uma conexão com o banco de dados
conn = sqlite3.connect('combinations.db')
cursor = conn.cursor()

# Cria a tabela 'combinations' no banco de dados
cursor.execute('''
    CREATE TABLE IF NOT EXISTS combinations (
        id INTEGER PRIMARY KEY,
        num1 INTEGER,
        num2 INTEGER,
        num3 INTEGER,
        num4 INTEGER,
        num5 INTEGER,
        num6 INTEGER
    )
''')

# Gera todas as combinações de 6 números entre 1 e 60
combinations = list(itertools.combinations(range(1, 61), 6))

# Insere cada combinação na tabela 'combinations'
for i, combination in enumerate(combinations):
    cursor.execute(f"INSERT INTO combinations (id, num1, num2, num3, num4, num5, num6) VALUES({i+1}, {combination[0]}, {combination[1]}, {combination[2]}, {combination[3]}, {combination[4]}, {combination[5]})")

# Salva as alterações no banco de dados e fecha a conexão
conn.commit()
conn.close()
