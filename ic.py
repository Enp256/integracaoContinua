def saque (valSaque,valorSaldo):
    if valSaque <= valorSaldo:
        return valorSaldo - valSaque 

def deposito (valDepo, valorSaldo):
    return valorSaldo + valDepo 

def desconto(preco,desc):
    return preco - preco*desc/100

def lucro(preco,ganho):
    return preco + preco*ganho/100

def imc(peso,altura):
    imc= peso / altura ** 2
    return '{:.2f}'.format(imc)

def tamanho(palavra):
    return len(palavra)

def TouF(tf):
    if tf == 't':
        return True
    elif tf == 'f':
        return False