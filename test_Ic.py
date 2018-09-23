import unittest
import ic 


def test_saque():
    assert ic.saque(200 ,1000) == 800  

def test_deposito():
    assert ic.deposito(50, 1000) == 4050

def test_verSaldo():
    assert ic.verSaldo(1000) == print(10400)