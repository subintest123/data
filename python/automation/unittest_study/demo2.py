import unittest


class Ecshop(unittest.TestCase):

    def setUp(self):
        print('开始了')

    def tearDown(self):
        print('结束了')

    def test_2_one(self):
        print('二')

    def test_3_tow(self):
        print('三')

    @unittest.skip
    def test_5_four(self):
        print('五')

    @unittest.expectedFailure
    def test_6_six(self):
        print('六')


if __name__ == '__main__':
    unittest.main(verbosity=2)