from unittest import TestCase
import konwerte
import pytest

def test_for_upper():
    assert konwerte.kon("alA") == "AlA"
    assert konwerte.kon("bedzie dobrze")=="bEdzIE dObrzE"

def test_for_lowwer():
    assert konwerte.kon("BEDZIE DOBRZE")=="bEdzIE dObrzE"

@pytest.fixture
def Test_case():
    napis1="Ala ma Kota"
    return konwerte.kon(napis1)

def test_method1(Test_case):
    x="AlA mA kOtA"
    assert x == Test_case
    assert isinstance(Test_case,str)
    
    
def test_method2(Test_case):
    x="ala ma kot"
    assert x != Test_case
    