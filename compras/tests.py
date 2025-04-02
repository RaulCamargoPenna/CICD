from django.test import TestCase
from compras.views import comprar

# def teste_comprar():

#     valor_produto = 9

#     resultado_esperado = True

#     resultado = comprar(valor=valor_produto)

#     assert resultado == resultado_esperado

class SampleTestCase(TestCase):
    def test_example(self):

        valor_produto = 11

        resultado_esperado = True

        resultado = comprar(valor=valor_produto)

        self.assertEqual(resultado_esperado, resultado)