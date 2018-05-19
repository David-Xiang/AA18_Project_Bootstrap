# coding: utf-8

from Transformer import Transformer

class Rule:
    def __init__(self, name, lhs, rhs, nacs):
        self.name = name
        self.lhs = lhs
        self.rhs = rhs
        self.nacs = nacs
        self.transRules = Transformer.generateTransRules(lhs, rhs)


    def print(self):
        print(self.name)
        print("----lhs----")
        self.lhs.print()
        print("----rhs----")
        self.rhs.print()
        print("----nacs----")
        for nac in self.nacs:
            nac.print()

