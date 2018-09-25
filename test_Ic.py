import unittest
import ic 


def test_saque():
    assert ic.saque(200 ,1000) == 800  

def test_deposito():
    assert ic.deposito(50, 1000) == 1050

def test_desc():
    assert ic.desconto(1000.00,15) == 850.0

def test_lucro():
    assert ic.lucro(200.50,30) == 260.65

def test_imc():
    assert ic.imc(60.2,1.75) == '19.66'

def test_tamanho():
    assert ic.tamanho('olha só que bonito') == 18

def test_TouF():
    assert ic.TouF('t') == True