import requests
from BeautifulSoup import BeautifulSoup

def megasena_api():
  URL_ULTIMOS_RESULTADOS = 'http://www1.caixa.gov.br/loterias/loterias/megasena/megasena_pesquisa_new.asp'
	page = requests.get(URL_ULTIMOS_RESULTADOS)
	bs = BeautifulSoup(page.content)
	numeros_sena =  [ n.contents[0] for n in bs.findAll('li')[:6]]
	
	results = page.content.split('|')
	
	return {'concurso': results[0], 'premio': results[1], 'numero_vencedores': results[3],
				'valor_vencedores': results[4], 'data_sorteio': results[11], 'numeros': numeros_sena}


import json
print(json.dumps(megasena_api()))