from django.test import TestCase
from teste.views import soma
# Create your tests here.

def teste_soma():
    resultado_esperado = 7
    
    resultado = soma(4, 3)

    assert resultado_esperado == resultado