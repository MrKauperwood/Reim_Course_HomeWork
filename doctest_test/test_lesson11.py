import unittest
import lesson11


class test_lesson11(unittest.TestCase):
    def setUp(self):
        print("Set-Up")

    def tearDown(self):
        print("TeatDown")

    def test_fact0(self):
        print("fact_0")
        # assert lesson11.factorial(0) == 1
        self.assertEqual(lesson11.factorial(0), 1)

    def test_fact1(self):
        print("fact_1")
        self.assertEqual(lesson11.factorial(1), 1)

    def test_fact5(self):
        print("fact_5")
        self.assertEqual(lesson11.factorial(5), 120)

    def test_fact_none(self):
        print("fact_none")
        # self.assertEqual(lesson11.factorial("none"))
        self.assertRaises((TypeError, IndexError), lesson11.factorial, "none")

if __name__=='__main__':
    unittest.main()