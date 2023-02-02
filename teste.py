import re
import mechanize
from bs4 import BeautifulSoup

url = "https://loterias.caixa.gov.br/Paginas/Download-Resultados.aspx"

def open_url(browser, url):
    return browser.open(url).read().decode('utf-8')

def extract_contest_number(soup):
    r = soup.find("div", "title-bar").contents[3].span.string
    search_result = re.search('[0-9]{4}', r)
    if search_result:
        return int(search_result.group(0))
    else:
        raise ValueError("Número do concurso não encontrado")

def extract_tags(soup):
   return soup.find_all("ul", "numbers")

def extract_numbers(r):
    numbers = []
    for i in range(6):
        numbers.append(r[0].contents[i].string)
    return numbers

def write_result(numbers):
    results = ",".join(numbers)
    with open("result_list.txt", "a") as f:
        f.write(results+'\n')

browser = mechanize.Browser()
html = open_url(browser, url)
soup = BeautifulSoup(html, "html.parser")

resulted_number = extract_contest_number(soup)

# decrescent results
while resulted_number > 0:
    r = extract_tags(soup)
    numbers = extract_numbers(r)
    write_result(numbers)
    
    resulted_number -= 1
    
    browser.select_form(name="buscaForm")
    browser["concurso"] = str(resulted_number)
    next_html = browser.submit().read().decode('utf-8')
    
    soup = BeautifulSoup(next_html, "html.parser")
