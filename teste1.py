from loteria_caixa import MegaSena

concurso = MegaSena()

results = []
results.append(concurso.todosDados())
results.append(concurso.tipoJogo())
results.append(concurso.numero())
results.append(concurso.nomeMunicipioUFSorteio())
results.append(concurso.dataApuracao())
results.append(concurso.valorArrecadado())
results.append(concurso.valorEstimadoProximoConcurso())
results.append(concurso.valorAcumuladoProximoConcurso())
results.append(concurso.valorAcumuladoConcursoEspecial())
results.append(concurso.valorAcumuladoConcurso_0_5())
results.append(concurso.acumulado())
results.append(concurso.indicadorConcursoEspecial())
results.append(concurso.dezenasSorteadasOrdemSorteio())
results.append(concurso.listaResultadoEquipeEsportiva())
results.append(concurso.numeroJogo())
results.append(concurso.nomeTimeCoracaoMesSorte())
results.append(concurso.tipoPublicacao())
results.append(concurso.observacao())
results.append(concurso.localSorteio())
results.append(concurso.dataProximoConcurso())
results.append(concurso.numeroConcursoAnterior())
results.append(concurso.numeroConcursoProximo())
results.append(concurso.valorTotalPremioFaixaUm())
results.append(concurso.numeroConcursoFinal_0_5())
results.append(concurso.listaMunicipioUFGanhadores())
results.append(concurso.listaRateioPremio())
results.append(concurso.listaDezenas())
results.append(concurso.listaDezenasSegundoSorteio())
results.append(concurso.id())

with open("results.txt", "w") as f:
    for result in results:
        f.write(str(result) + "\n")
