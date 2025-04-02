from django.test import TestCase
from teste.views import soma
# Create your tests here.

def teste_soma():
    resultado_esperado = 7
    
    
    resultado = soma(3, 4)
    #fiz cagada
    assert resultado_esperado == resultado