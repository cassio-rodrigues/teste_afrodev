# from soma import soma_dois_numeros
def soma_dois_numeros(n1 : int, n2 : int) -> int:
    return n1 + n2

def divide_dois_numeros(n1, n2):
    # import ipdb
    # ipdb.set_trace()

    if n2 == 0:
        return "Não pode dividir por zero"
    if type(n1) != int or type(n2) != int:
        return "Não é possivel dividir letras"
    return n1 / n2

def subtrai_dois_numeros(n1, n2):
    return n1 - n2

def test_retorno_soma_dois_numeros():
    assert 3 == soma_dois_numeros(1, 2)

def test_divisao_com_numeros_validos():
    assert 2 == divide_dois_numeros(4, 2)

def test_divisao_por_zero():
    assert "Não pode dividir por zero" == divide_dois_numeros(1, 0)

def test_divisao_com_zero_a_esquerda():
    resultado = divide_dois_numeros(0, 1)
    assert 0 == resultado

def test_divisao_com_letras():
    assert "Não é possivel dividir letras" == divide_dois_numeros("4", "2")


# coding using TDD (TEST DRIVEN DEVELOPMENT)
def test_funcao_subtrai_dois_numeros():
    assert 1 == subtrai_dois_numeros(2, 1)




