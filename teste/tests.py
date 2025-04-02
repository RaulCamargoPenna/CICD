from django.test import TestCase
from teste.views import soma
# Create your tests here.

def teste_soma():
    resultado_esperado = 6
    
    
    resultado = soma(3, 3)
    
    assert resultado_esperado == resultado