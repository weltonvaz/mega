import sqlite3

# Conectar ao banco de dados (cria se não existir)
conn = sqlite3.connect('dados_concurso.db')
cursor = conn.cursor()

# Criar a tabela resultados
cursor.execute('''
CREATE TABLE IF NOT EXISTS resultados (
    acumulado BOOLEAN,
    data_apuracao DATE,
    data_proximo_concurso DATE,
    dezenas_sorteadas_ordem_sorteio TEXT,
    indicador_concurso_especial INTEGER,
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lista_dezenas TEXT,
    local_sorteio TEXT,
    nome_municipio_uf_sorteio TEXT,
    nome_time_coracao_mes_sorte TEXT,
    numero INTEGER,
    numero_jogo INTEGER,
    observacao TEXT,
    tipo_jogo TEXT,
    tipo_publicacao INTEGER,
    valor_arrecadado REAL,
    valor_acumulado_concurso_0_5 REAL,
    valor_acumulado_concurso_especial REAL,
    valor_acumulado_proximo_concurso REAL,
    valor_estimado_proximo_concurso REAL
);
''')

# Inserir os dados do dicionário na tabela resultados
dados = {'acumulado': True, 'dataApuracao': '01/02/2023', 'dataProximoConcurso': '04/02/2023', 'dezenasSorteadasOrdemSorteio': ['52', '48', '05', '20', '17', '04'], 'exibirDetalhamentoPorCidade': True, 'id': None, 'indicadorConcursoEspecial': 1, 'listaDezenas': ['04', '05', '17', '20', '48', '52'], 'listaDezenasSegundoSorteio': None, 'listaMunicipioUFGanhadores': [], 'listaRateioPremio': [{'descricaoFaixa': '6 acertos', 'faixa': 1, 'numeroDeGanhadores': 0, 'valorPremio': 0.0}, {'descricaoFaixa': '5 acertos', 'faixa': 2, 'numeroDeGanhadores': 151, 'valorPremio': 52127.84}, {'descricaoFaixa': '4 acertos', 'faixa': 3, 'numeroDeGanhadores': 13422, 'valorPremio': 837.78}], 'listaResultadoEquipeEsportiva': None, 'localSorteio': 'ESPAÇO DA SORTE', 'nomeMunicipioUFSorteio': 'SÃO PAULO, SP', 'nomeTimeCoracaoMesSorte': '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', 'numero': 2560, 'numeroConcursoAnterior': 2559, 'numeroConcursoFinal_0_5': 2565, 'numeroConcursoProximo': 2561, 'numeroJogo': 2, 'observacao': '', 'premiacaoContingencia': None, 'tipoJogo': 'MEGA_SENA', 'tipoPublicacao': 3, 'ultimoConcurso': True, 'valorArrecadado': 136523016.0, 'valorAcumuladoConcurso_0_5': 9114140.03, 'valorAcumuladoConcursoEspecial': 11051958.41, 'valorAcumuladoProximoConcurso': 116878183.88, 'valorEstimadoProximoConcurso': 135000000.0, 'valorSaldoReservaGarantidora': 0.0, 'valorTotalPremioFaixaUm': 0.0}

cursor.execute("""
INSERT INTO resultados (acumulado, dataApuracao, dataProximoConcurso, dezenasSorteadasOrdemSorteio, exibirDetalhamentoPorCidade, id, indicadorConcursoEspecial, listaDezenas, listaDezenasSegundoSorteio, listaMunicipioUFGanhadores, listaRateioPremio, listaResultadoEquipeEsportiva, localSorteio, nomeMunicipioUFSorteio, nomeTimeCoracaoMesSorte, numero, numeroConcursoAnterior, numeroConcursoFinal_0_5, numeroConcursoProximo, numeroJogo, observacao, premiacaoContingencia, tipoJogo, tipoPublicacao, ultimoConcurso, valorArrecadado, valorAcumuladoConcurso_0_5, valorAcumuladoConcursoEspecial, valorAcumuladoProximoConcurso, valorEstimadoProximoConcurso, valorSaldoReservaGarantidora, valorTotalPremioFaixaUm)
VALUES (:acumulado, :dataApuracao, :dataProximoConcurso, :dezenasSorteadasOrdemSorteio, :exibirDetalhamentoPorCidade, :id, :indicadorConcursoEspecial, :listaDezenas, :listaDezenasSegundoSorteio, :listaMunicipioUFGanhadores, :listaRateioPremio, :listaResultadoEquipeEsportiva, :localSorteio, :nomeMunicipioUFSorteio, :nomeTimeCoracaoMesSorte, :numero, :numeroConcursoAnterior, :numeroConcursoFinal_0_5, :numeroConcursoProximo, :numeroJogo, :observacao, :premiacaoContingencia, :tipoJogo, :tipoPublicacao, :ultimoConcurso, :valorArrecadado, :valorAcumuladoConcurso_0_5, :valorAcumuladoConcursoEspecial, :valorAcumuladoProximoConcurso, :valorEstimadoProximoConcurso, :valorSaldoReservaGarantidora, :valorTotalPremioFaixaUm)
""", dados)

#Commitar as mudanças no banco de dados
conn.commit()

#Fechar a conexão com o banco de dados
conn.close()





