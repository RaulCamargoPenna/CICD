from django.test import TestCase
from teste.views import soma
# Create your tests here.

def teste_soma():
    resultado_esperado = 8
    
    resultado = soma(4, 4)

    assert resultado_esperado == resultado