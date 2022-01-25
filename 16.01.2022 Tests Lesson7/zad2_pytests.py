import pytest

def warp(height,width,length):
    wynik=20+(height*2)+(width*2)+(length*4)
    return wynik

@pytest.mark.parametrize("x,y,z,wynik",[(1,3,1,32),(13,13,13,124)])
def test_method(x,y,z,wynik):
    assert warp(x,y,z)==wynik
    assert isinstance(wynik,int or float)
    test=[32,124,13]
    assert warp(x,y,z) in test

@pytest.fixture
def Test_case():
    wynik=warp(1,3,1)
    return wynik

def test_method1(Test_case):
    test=32
    assert  test==Test_case

def test_method2(Test_case):
    assert isinstance(Test_case,int or float)
    