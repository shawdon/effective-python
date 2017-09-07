#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
toml==0.9.2
"""
import os
import sys

print(sys.path)
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import toml
from data_structure.dot_dict import DotDict


def load_config(filename):
    try:
        config = toml.load(filename, DotDict)
        return config
    except Exception as e:
        print('load config error: %s' % e)
        exit(1)


def test():
    config = load_config(os.path.join(os.path.dirname(__file__), 'example.toml'))
    print(config)


if __name__ == '__main__':
    test()
