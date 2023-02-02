import sqlite3
conn = sqlite3.connect('dados_concurso.db')
cursor = conn.cursor()

cursor.execute("""
    ALTER TABLE resultados
    ADD COLUMN premiacaoContingencia text
    
""")

conn.commit() 
conn.close()