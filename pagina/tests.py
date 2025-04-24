from django.test import TestCase
from .views import retornar_token, api_busca_pedidos_pendentes
from .models import Tokens_mercado_livre_correto
from unittest.mock import patch

# Create your tests here.
class SampleTestCase(TestCase):
        
    def test_token(self):
        
        token = 'token_teste'
        
        filial_teste = 'sc'
        resultado_esperado = token
        
        Tokens_mercado_livre_correto.objects.create(
            filial = filial_teste,
            access_token = token,
            refresh_token = 'teste'
        )
        
        
        resultado = retornar_token(filial=filial_teste)

        self.assertEqual(resultado_esperado, resultado)
        
    @patch('pagina.views.requests.get')
    def test_api_function(self, mock_get):
        pedidos_fake = [
            {'id': 22735080780, 'numero': 333145, 'numeroLoja': '2000011407161834', 'data': '2025-04-24', 'dataSaida': '2025-04-24', 'dataPrevista': '0000-00-00', 'totalProdutos': 224.91, 'total': 224.91, 'contato': {'id': 17377674653, 'nome': 'Aristephany Gabrieli Duarte Lopes', 'tipoPessoa': 'F', 'numeroDocumento': '151.397.926-48'}, 'situacao': {'id': 12, 'valor': 2}, 'loja': {'id': 204699216}}, 
            {'id': 22734846895, 'numero': 333129, 'numeroLoja': '2000011406756138', 'data': '2025-04-24', 'dataSaida': '2025-04-24', 'dataPrevista': '0000-00-00', 'totalProdutos': 459.9, 'total': 459.9, 'contato': {'id': 17377628453, 'nome': 'André Cruz (cruzandré20230604164249)', 'tipoPessoa': 'F', 'numeroDocumento': '118.190.259-26'}, 'situacao': {'id': 12, 'valor': 2}, 'loja': {'id': 203872965}}
        ]
        
        mock_response = mock_get.return_value
        mock_response.json.return_value = {'data': pedidos_fake}
        
        resultado = api_busca_pedidos_pendentes()
        
        self.assertEqual(len(resultado['data']), 2)
        self.assertEqual(resultado['data'][0]['id'], 22735080780)