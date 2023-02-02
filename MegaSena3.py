import sqlite3
from loteria_caixa import *

def save_concursos_to_db(concursos):
    conn = sqlite3.connect("resultados_mega2023.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resultados (
        acumulado TEXT,
        dataApuracao TEXT,
        dataProximoConcurso TEXT,
        dezenasSorteadasOrdemSorteio TEXT,
        exibirDetalhamentoPorCidade TEXT,
        indicadorConcursoEspecial TEXT,
        listaDezenas TEXT,
        listaRateioPremio TEXT,
        localSorteio TEXT,
        nomeMunicipioUFSorteio TEXT,
        numero TEXT,
        valorArrecadado REAL,
        valorAcumuladoConcursoEspecial REAL,
        valorAcumuladoProximoConcurso REAL,
        valorEstimadoProximoConcurso REAL,
        valorTotalPremioFaixaUm REAL
    )
    """)
    for concurso in concursos:
        dados = concurso.todosDados()

        cursor.execute("""
            INSERT INTO resultados (acumulado, dataApuracao, dataProximoConcurso, dezenasSorteadasOrdemSorteio, exibirDetalhamentoPorCidade, indicadorConcursoEspecial, listaDezenas, listaRateioPremio, localSorteio, nomeMunicipioUFSorteio, numero, valorArrecadado, valorAcumuladoConcursoEspecial, valorAcumuladoProximoConcurso, valorEstimadoProximoConcurso, valorTotalPremioFaixaUm)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (dados["acumulado"], dados["dataApuracao"], dados["dataProximoConcurso"], str(dados["dezenasSorteadasOrdemSorteio"]), dados["exibirDetalhamentoPorCidade"], dados["indicadorConcursoEspecial"], str(dados["listaDezenas"]), str(dados["listaRateioPremio"]), dados["localSorteio"], dados["nomeMunicipioUFSorteio"], dados["numero"], dados["valorArrecadado"], dados["valorAcumuladoConcursoEspecial"], dados["valorAcumuladoProximoConcurso"], dados["valorEstimadoProximoConcurso"], dados["valorTotalPremioFaixaUm"]))

    conn.commit()
    conn.close()

concursos = [MegaSena(x) for x in range(1, 2601)]
save_concursos_to_db(concursos)
