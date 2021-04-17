from collections import Iterable  # drop `.abc` with Python 2.7 or lower
import numpy

def iterable(obj, allow_string=False):
    if type(obj) == 'str' and not allow_string: return False
    return isinstance(obj, Iterable)


def list2text(lst, sep=' '):
    if type(lst) == str: return lst
    text = ''
    for x in lst:
        if type(x) == float: x = '%.2f' % x
        if type(x) == numpy.float64: x = '%.2f' % x
        text = text + sep + str(x)
    text = text.rstrip(sep)
    text = text.lstrip(sep)
    return text
