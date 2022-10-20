import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Parâmetros obrigatórios
API_KEY = os.getenv('API_KEY')
codigo_cidade = 'codigoIbge=5201108'
mes_ano = 'mesAno=202202'

api_base_url = 'https://api.portaldatransparencia.gov.br/api-de-dados/'

auxilio_municipio = 'auxilio-brasil-por-municipio?'
auxilio_sacado_municipio = 'auxilio-brasil-sacado-beneficiario-por-municipio?'
auxilio_sacado_nis = 'auxilio-brasil-sacado-por-nis?'

final_url = api_base_url + auxilio_municipio + '&' + codigo_cidade + '&' + mes_ano

response = requests.get(final_url, headers={'chave-api-dados': API_KEY})
print(response._content)