import pytest
# pytest is a python test runner, with a few very nice features.
# for example, there is a mode that intragrates well with emacs
# one of the more interesting features for me is that it encourages to only use
# pythons plain assert. It does its magic to make sure that failing assert calls are 
# informative. 

# To call pytest from python, use
pytest.main()

# To check if an exception is thrown, use pytest.raises



def test_divide_by_null():
    with pytest.raises(ZeroDivisionError):
        print ("divide 10 by zeor, and you get %s " % 10/0)


