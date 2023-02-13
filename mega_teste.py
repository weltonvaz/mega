from loteria_caixa import MegaSena
def converter(lista_str):
    return [int(x) for x in lista_str]
    


for i in range(1, 2563):
    concurso = MegaSena(i)
    print(concurso.numero(),converter(concurso.listaDezenas()))
    

