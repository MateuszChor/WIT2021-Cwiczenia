import unittest

def warp(height,width,length):
    wynik=20+(height*2)+(width*2)+(length*4)
    return wynik

class Test_wrap(unittest.TestCase):
    def setUp(self):
        self.wynik=warp(17,32,11)
        self.wynik1=warp(13,13,13)
        self.wynik2=warp(1,3,1)
            
    def test_case_Equal(self):
        self.assertEqual(self.wynik,162)
        self.assertEqual(self.wynik1,124)
        self.assertEqual(self.wynik2,32)


    def test_More_case(self):
        tab=[]
        for i in range(1000): # zbior liczb od 0 do 99
            tab.append(i)

        self.assertIn(self.wynik2,tab) # czy nasze rozwiazanie znajduje sie w tym zbiorze
        self.assertNotEqual(self.wynik2,tab) # wynik2 nie jest rowny zbiorowi od 0 do 99 
        self.assertIsInstance(self.wynik1,int)
    

if __name__ == '__main__':
    unittest.main()
    