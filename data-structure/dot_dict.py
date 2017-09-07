#!/usr/bin/env python
# -*- coding: utf-8 -*-

class DotDict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

def test():
    dd = DotDict()
    dd['test_key'] = 'test_value'
    print(dd.test_key)

if __name__ == '__main__':
    test()
