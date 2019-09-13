import unittest
from app.models import Source
class SourceTest(unittest.TestCase):
    '''
    test class to test the source class
    '''
    def setUp(self):
        '''
        setup method always runs after every test
        '''
        self.sources = Sources(12,'BBC','best source')
    def test_for_instance(self):
        self.assertTrue(isinstance(self.sources,Sources))

if __name__=='__main__':
    unittest.main()