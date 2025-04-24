from django.shortcuts import render
# Create your views here.
def comprar(valor):

    if valor <= 10:
        return True
    
    return False