from django.test import TestCase
from teste.views import soma
# Create your tests here.

def teste_soma():
    resultado_esperado = 5
    
    
    resultado = soma(3, 2)
    
    assert resultado_esperado == resultado