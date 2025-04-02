from django.test import TestCase
from teste.views import soma
# Create your tests here.

def teste_soma():
    resultado_esperado = 10
    
    resultado = soma(5, 5)

    assert resultado_esperado == resultado