import unittest
import some_app

# run from terminal
# to run multiple tests: python3 -m unittest
# to make test execution verbose: python3 -m unittest -v
# test functions must be named test_[name]

class TestApp(unittest.TestCase):
    def setUp(self):
        # virtual method that can be overriden to set things before each test, e.g. set default values
        print('about to test a function')

    def test_do_stuff(self):
        test_param = 10
        result = some_app.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'alsdf'
        result = some_app.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = some_app.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')

    def test_do_stuff4(self):
        test_param = ''
        result = some_app.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')

    def tearDown(self):
        # virtual method that can be overriden to set things after each test
        print('cleaning up')


if __name__ == '__main__':
    unittest.main()

