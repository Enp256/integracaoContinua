import unittest
import ic 


def test_saque():
    assert ic.saque(200 ,1000) == 800  

def test_deposito():
    assert ic.deposito(50, 1000) == 1050

def test_Saldo():
    assert ic.Saldo(1000) == 1000