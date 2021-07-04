"""

"""
import requests
from bs4 import BeautifulSoup

url = 'https://stackoverflow.com/questions/tagged/python'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')
# Iterando sob a página
# Descobrir o título das perguntas primeiro. Inspecionar o elemento na página e printar:
for pergunta in html.select('.question-summary'):
    titulo = pergunta.select_one('.question-hyperlink')
    data = pergunta.select_one('.relativetime')
    votos = pergunta.select_one('.vote-count-post')
    user_a = pergunta.select_one('.user-details')
    print(titulo.text, data.text, votos.text, user_a.text,  sep='\t')
