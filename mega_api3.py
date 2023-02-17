# -*- coding: utf-8 -*-
from loteria_caixa import MegaSena
from datetime import date, timedelta
from datetime import datetime

# Abrindo um arquivo para escrita
with open("resultados_megasena.txt", "w") as file:
    # Escrevendo o cabeçalho do arquivo
    file.write("numero_concurso,dezenas_sorteadas\n")

    # Loop para baixar os resultados de todos os sorteios
    for i in range(1, 2565):
        concurso = MegaSena(i)
        
        dados = concurso.todosDados()
        data = datetime.strptime(concurso.dataApuracao(), "%d/%m/%Y").date()
        
        numero = dados.get('numero')
        if numero:
            file.write("{},{},{}\n".format(data.toordinal(),numero, " ".join(concurso.listaDezenas())))
        else:
            print("Não foi possível obter o número do concurso")
        