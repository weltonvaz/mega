import sqlite3

# -*- coding: utf-8 -*-
from loteria_caixa import *

concurso = MegaSena()
dados = concurso.todosDados()

# Cria conexão com banco de dados
conn = sqlite3.connect('resultados_mega.db')
cursor = conn.cursor()

# Cria tabela no banco de dados
cursor.execute("""
CREATE TABLE IF NOT EXISTS resultados (
    acumulado BOOLEAN,
    dataApuracao TEXT,
    dataProximoConcurso TEXT,
    dezenasSorteadasOrdemSorteio TEXT,
    exibirDetalhamentoPorCidade BOOLEAN,
    id INTEGER,
    indicadorConcursoEspecial INTEGER,
    listaDezenas TEXT,
    listaDezenasSegundoSorteio TEXT,
    listaMunicipioUFGanhadores TEXT,
    listaRateioPremio TEXT,
    listaResultadoEquipeEsportiva TEXT,
    localSorteio TEXT,
    nomeMunicipioUFSorteio TEXT,
    nomeTimeCoracaoMesSorte TEXT,
    numero INTEGER,
    numeroConcursoAnterior INTEGER,
    numeroConcursoFinal_0_5 INTEGER,
    numeroConcursoProximo INTEGER,
    numeroJogo INTEGER,
    observacao TEXT,
    premiacaoContingencia TEXT,
    tipoJogo TEXT,
    tipoPublicacao INTEGER,
    ultimoConcurso BOOLEAN,
    valorArrecadado REAL,
    valorAcumuladoConcurso_0_5 REAL,
    valorAcumuladoConcursoEspecial REAL,
    valorAcumuladoProximoConcurso REAL,
    valorEstimadoProximoConcurso REAL,
    valorSaldoReservaGarantidora REAL,
    valorTotalPremioFaixaUm REAL
)
""")

# Insere dados na tabela
cursor.execute("""
INSERT INTO resultados (
    acumulado,
    dataApuracao,
    dataProximoConcurso,
    dezenasSorteadasOrdemSorteio,
    exibirDetalhamentoPorCidade,
    id,
    indicadorConcursoEspecial,
    listaDezenas,
    listaDezenasSegundoSorteio,
    listaMunicipioUFGanhadores,
    listaRateioPremio,
    listaResultadoEquipeEsportiva,
    localSorteio,
    nomeMunicipioUFSorteio,
    nomeTimeCoracaoMesSorte,
    numero,
    numeroConcursoAnterior,
    numeroConcursoFinal_0_5,
    numeroConcursoProximo,
    numeroJogo,
    observacao,
    premiacaoContingencia,
    tipoJogo,
    tipoPublicacao,
    ultimoConcurso,
    valorArrecadado,
    valorAcumuladoConcurso_0_5,
    valorAcumuladoConcursoEspecial,
    valorAcumuladoProximoConcurso,
    valorEstimadoProximoConcurso,
    valorSaldoReservaGarantidora,
    valorTotalPremioFaixaUm
