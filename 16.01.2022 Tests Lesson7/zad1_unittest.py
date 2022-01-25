import konwerte as k
import unittest

class Test_Konwerter(unittest.TestCase):

    def test_Equal(self):
        napis="aLa Ma Kota"
        self.assertEqual(k.kon("Napis Testowy"),"nApIs tEstOwY")
        self.assertEqual(k.kon(napis),"AlA mA kOtA")
        self.assertEqual(k.kon("a"),"A") 
      
    def test_Not_Equal(self):
        self.assertNotEqual(k.kon('BBB'),"BBB")
        self.assertNotEqual(k.kon('aaa'),"aaa")

    def test_True(self):
        self.assertTrue(k.kon("aaa"),"AAA")
        self.assertTrue(k.kon("BBB"),"bbb")
        self.assertTrue(k.kon("AAA"),"aaa")
        self.assertTrue(k.kon("bbb"),"BBB")
        
if __name__ == '__main__':
    unittest.main()
    
    