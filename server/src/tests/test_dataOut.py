from src import process_data
from src.process_data import script_calc
import unittest

class MyTest(unittest.TestCase):
    def test(self):
        #test to see if the data is processed correctly and correct inputs are being read
        #  (do a for loop to test it) do all possible solutions
        res = script_calc('Duke Select', 'Prostate Cancer', 'IV')
        self.assertEqual(res[0], '1,Initial,6550')
        
        
        # Tests to see that error checking was implemented correctly
        # test to see if not giving certain inputs would fail
        res1 = script_calc('Duke Basic','', 'IV')
        self.assertEqual(res1, '')
       
       # test to see if not providing the correct input would fail
        res2 = script_calc('Duke','Prostate Cancer', 'IV')
        self.assertEqual(res2, '')
       
# if __name__ == '__main__':
#     unittest.main()