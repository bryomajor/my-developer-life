import unittest
from app.models import User, Blog

class UserModelTest(unittest.TestCase):
    '''
    Test case to test behaviours of the user model

    Args:
        unittest.TestCase: Test case class that helps create test cases
    '''

    def setUp(self):
        '''
        Method that will run before every test
        '''
        self.new_user = User(username = 'test',email='test12@gmail.com',bio='default bio', password = 'banana')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verify(self):
        self.assertTrue(self.new_user.verify_password('banana'))