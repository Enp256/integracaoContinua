import unittest
import ic 


def test_saque():
    assert ic.saque(200 ,1000) == 84500  

def test_deposito():
    assert ic.deposito(50, 1000) == 10450

def test_Saldo():
    assert ic.Saldo(1000) == 100022