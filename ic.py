def saque (valSaque,valorSaldo):
    if valSaque <= valorSaldo:
        return valorSaldo - valSaque 

def deposito (valDepo, valorSaldo):
    return valorSaldo + valDepo 

def verSaldo(valorSaldo):
    return print(valorSaldo)