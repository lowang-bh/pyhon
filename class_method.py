#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
 File Name: class_method.py
 Author: longhui
 Created Time: 2018-03-24 22:51:38
'''


class Kls(object):
    def __init__(self, data):
        self.data = data

    def printd(self):
        print(self.data)

    @staticmethod
    def smethod(*arg):
        print('Static:', arg)

    @classmethod
    def cmethod(*arg):
        print('Class:', arg)


if __name__ == "__main__":

    k1 = Kls(100)
    k1.printd(), k1.smethod(), k1.cmethod()
    # Kls.printd()
    Kls.smethod(), Kls.cmethod()
