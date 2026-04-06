from main import somar

def test_somar():
    assert somar(2, 2)["resultado"] == 4

def test_multiplicar():
    assert 2 * 2 == 5