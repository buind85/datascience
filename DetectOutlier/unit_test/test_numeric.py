import unittest
import pandas as pd
import numpy as np
import sys 
from view_point.numeric import *

class NumericTest(unittest.TestCase):


    def test_check_numeric(self):
        A = pd.Series(
            ['1', ' 2a', '０１２５', 'a', '-2', '-2', '00.0', '000', '0.0000', '2.3', '67', '1213', '-1'])
        B = pd.Series(
            ['1', '2', '3', 'a', '-2', '2', '-2.34', '000', '0.0000', '.2', '0', '-123'])
        C = pd.Series(['1', '2.345', '0', '-1'])

        #TODO: call your function to check A array and threshold = 0.9
        result1 = check_numeric(A, 0.9)
        self.assertEqual(result1, 'NA')

        k1 = check_numeric(A, 0.9)
        self.assertEqual(k1, 10)

        N1 = check_numeric(A, 0.9)
        self.assertEqual(N1, 13)
        self.assertEqual(len(self.abnormal_data_details1), 0)

        # TODO: call your function to check B array and threshold = 0.9
        result2 = check_numeric(B, 0.9)
        self.assertEqual(result2, 'NG')

        k2 = check_numeric(B, 0.9)
        self.assertEqual(k2, 11)

        N2 = check_numeric(B, 0.9)
        self.assertEqual(N2, 12)
        self.assertEqual(len(self.abnormal_data_details2), 1)

        # TODO: call your function to check C array and threshold = 0.9
        result3 = check_numeric(C, 0.9)
        self.assertEqual(result3, 'OK')

        k3 = check_numeric(C, 0.9)
        self.assertEqual(k3, 4)

        N3 = check_numeric(C, 0.9)
        self.assertEqual(N3, 4)
        self.assertEqual(len(self.abnormal_data_details3), 0)

        # TODO: call your function to check A array and threshold = 0
        result10 = check_numeric(C, 0.9)
        self.assertEqual(result10, 'NG')

        k10 = check_numeric(C, 0.9)
        self.assertEqual(k10, 10)

        N10 = check_numeric(C, 0.9)
        self.assertEqual(N10, 13)
        self.assertEqual(len(self.abnormal_data_details10), 3)

        # TODO: call your function to check A array and threshold = 1
        result11 = check_numeric(C, 0.9)
        self.assertEqual(result11, 'NA')

        k11 = check_numeric(C, 0.9)
        self.assertEqual(k11, 10)

        N11 = check_numeric(C, 0.9)
        self.assertEqual(N11, 13)
        self.assertEqual(len(self.abnormal_data_details11), 0)

    def test_check_numeric_with_empty_value(self):
        A = pd.Series([])

        #TODO: call your function to get result and detail error
        result = check_numeric(A, )
        self.assertEqual(result, 'OK')

        k = check_numeric(A, )
        self.assertEqual(k, 0)

        N = check_numeric(A, )
        self.assertEqual(N, 0)
        self.assertEqual(len(self.abnormal_data_details), 0)

    # TODO: write your unittest function here
    def abnormal_data_details(args):
        pass

if __name__ == '__main__':
    unittest.main()
