import unittest
from app.models import Articles


class ArticlesTest(unittest.TestCase):
    '''
    testcase class
    '''
    def setUp(self):
        '''
        testcase that runs after every test
        '''
        self.articles= Articles ()
    def test_for_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))
if __name__=='__main__':
    unittest.main()