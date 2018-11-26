from calcuator import Count
import unittest

class TestAdd(unittest.TestCase):

    def setUp(self):
        print("test start")

    def test_add(self):
        j = Count(2,3)
        self.assertEqual(j.add(),5)

    def test_add2(self):
        j = Count(42,55)
        self.assertEqual(j.add(),97)

    def tearDown(self):
        print("test end")

class TestSub(unittest.TestCase):
    def setUp(self):
        print("test sub start")

    def test_sub(self):
        j= Count(2,3)
        self.assertEqual(j.sub(),-1)

    def test_sub2(self):
        j = Count(11,10)
        self.assertEqual(j.sub(),1)

    def tearDown(self):
        print("test sub end")

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestAdd("test_add"))
    suite.addTest(TestAdd("test_add2"))
    suite.addTest(TestSub("test_sub"))
    suite.addTest(TestSub("test_sub2"))
    
    runner = unittest.TextTestRunner()
    runner.run(suite)    