# Since Python 3.3, mock is a part of the standard unittest package. 
# The paradigm is:
# 1. to 'patch' a object or method reference 
# 2. every call on the mocked object will return a new mocked object
# 3. These mocked ojects can be configured for return values, 
# 4. and assertions can be made about the calling of these objects

from unittest import mock, TestCase


class SomeClass(object):
    def this_methods_has_sideeffect(self, arg1, arg2):
        result = arg1 + arg2 
        print('Sum = %s' % result)

        return result

    def __str__(self):
        return "test class" 

class TestMyMock(TestCase):
    def test_mock(self):
        
        some_class = SomeClass()
        some_class.this_methods_has_sideeffect = mock.MagicMock(name='mymock')
        
        print('calling the method here should not print, as the method is \'patched\'')
        result = some_class.this_methods_has_sideeffect(1,2)
        assert isinstance(result, mock.MagicMock)
        
        print('now I can assert that the method was called!')
    
        assert 1 == some_class.this_methods_has_sideeffect.call_count 
        some_class.this_methods_has_sideeffect.assert_called_with(1, 2)


