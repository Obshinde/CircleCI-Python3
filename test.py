import unittest
from main import to_upper

class MyTestCase(unittest.TestCase):
    def test_to_upper(self):
        name="OMKARSHINDE"
        up=to_upper(name)
        self.assertEqual(up, "OMKARSHINDE")

if __name__=='__main__':
    unittest.main()
