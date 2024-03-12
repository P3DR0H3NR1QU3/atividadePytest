def soma(a,b):
    return a + b

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / y
# resultado = soma(1,2)
# print("Soma", resultado)

# testsoma

def test_soma():
    assert soma(1,2) == 3
    
def test_soma():
    assert soma(1,1) == 2
    
def test_soma():
    assert soma(1,2) == 4
    

# testsubtracao


def test_subtracao():
    assert subtracao(8,2) == 6
    
def test_subtracao():
    assert subtracao(2,1) == 1
    
def test_subtracao():
    assert subtracao(8,4) == 3
    
# testmultiplicacao

def test_multiplicacao():
    assert multiplicacao(2,2) == 4
    
def test_multiplicacao():
    assert multiplicacao(2,3) == 5
    
def test_multiplicacao():
    assert multiplicacao(4,2) == 16
    
# testdivisao

def test_divisao():
    assert divisao(4,2) == 1
    
def test_divisao():
    assert divisao(6,2) == 3

def test_divisao():
    assert divisao(16,2) == 8
    
