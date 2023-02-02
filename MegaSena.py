# -*- coding: utf-8 -*-
import sqlite3
from loteria_caixa import *

concurso = MegaSena()

conn = sqlite3.connect("resultados_mega.db")
cursor = conn.cursor()

table_name = "resultados_mega"

# Criar a tabela, se ainda não existir
cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (acumulado BOOLEAN, dataApuracao TEXT, dataProximoConcurso TEXT, dezenasSorteadasOrdemSorteio TEXT, exibirDetalhamentoPorCidade BOOLEAN, id INTEGER, indicadorConcursoEspecial INTEGER, listaDezenas TEXT, listaDezenasSegundoSorteio TEXT, listaMunicipioUFGanhadores TEXT, listaRateioPremio TEXT, listaResultadoEquipeEsportiva TEXT, localSorteio TEXT, nomeMunicipioUFSorteio TEXT, nomeTimeCoracaoMesSorte TEXT, numero INTEGER, numeroConcursoAnterior INTEGER, numeroConcursoFinal_0_5 INTEGER, numeroConcursoProximo INTEGER, numeroJogo INTEGER, observacao TEXT, premiacaoContingencia TEXT, tipoJogo TEXT, tipoPublicacao INTEGER, ultimoConcurso BOOLEAN, valorArrecadado REAL, valorAcumuladoConcurso_0_5 REAL, valorAcumuladoConcursoEspecial REAL, valorAcumuladoProximoConcurso REAL, valorEstimadoProximoConcurso REAL, valorSaldoReservaGarantidora REAL, valorTotalPremioFaixaUm REAL)")

dados = concurso.todosDados()

# Inserir os dados na tabela
cursor.execute(f"INSERT INTO {table_name} VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (dados["acumulado"], dados["dataApuracao"], dados["dataProximoConcurso"], ",".join(dados["dezenasSorteadasOrdemSorteio"]), dados["exibirDetalhamentoPorCidade"], dados["id"], dados["indicadorConcursoEspecial"], ",".join(dados["listaDezenas"]), dados["listaDezenasSegundoSorteio"], ",".join(dados["listaMunicipioUFGanhadores"]), str(dados["listaRateioPremio"]), dados["listaResultadoEquipeEsportiva"], dados["localSorteio"], dados["nomeMunicipioUFSorteio"], dados["nomeTimeCoracaoMesSorte"], dados["numero"], dados
