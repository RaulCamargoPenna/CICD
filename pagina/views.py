from django.shortcuts import render
from .models import Tokens_mercado_livre_correto
from app.settings import V3_TOKEN
import requests

def retornar_token(filial):
    token = Tokens_mercado_livre_correto.objects.get(filial = str(filial).upper()).access_token
    print('token', token)
    return token

def api_busca_pedidos_pendentes():
    endpoint = 'https://www.bling.com.br/Api/v3/pedidos/vendas?idsSituacoes[]=12'
    payload = {}
    headers = {
        'Authorization': f'Bearer {V3_TOKEN}'
    }
    response = requests.get(url= endpoint, headers=headers, data=payload, timeout=30)
    informacoes = response.json()
    print(informacoes)
    return informacoes
    