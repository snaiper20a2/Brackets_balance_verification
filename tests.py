import unittest
from BalanceVerificator import BalanceVerificator


class MyTestCase(unittest.TestCase):

    def test_1(self):
        balance_verificator = BalanceVerificator()
        self.assertEqual(balance_verificator.verify('{[(())]}'), -1)

    def test_2(self):
        balance_verificator = BalanceVerificator()
        self.assertEqual(balance_verificator.verify('{[(]}'), 3)

    def test_3(self):
        balance_verificator = BalanceVerificator()
        self.assertEqual(balance_verificator.verify('{{[[[[[(())]]]]]}}'), -1)

    def test_4(self):
        balance_verificator = BalanceVerificator()
        self.assertEqual(balance_verificator.verify('{{()]}}'), 2)

    def test_5(self):
        balance_verificator = BalanceVerificator()
        self.assertRaises(ValueError, balance_verificator.verify, '{[()]};')

    def test_6(self):
        balance_verificator = BalanceVerificator()
        self.assertRaises(ValueError, balance_verificator.verify, '')



if __name__ == '__main__':
    unittest.main()
