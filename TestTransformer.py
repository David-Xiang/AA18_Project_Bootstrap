# coding: utf-8

from Reader import Reader
from Maper import Maper
from Transformer import Transformer

if __name__ == "__main__":
    '''test Transformer'''
    print("------------")
    print("TEST Rule")
    rules = Reader.rulesToRules("rules.json")
    for rule in rules:
        print("------------")
        print(rule.name)
        rule.transRules.print()

    question = Reader.questionToGraph("trival.json")
    rules = Reader.rulesToRules("rules.json")

    print("------------")
    print("TEST Maper")
    rule = rules[3]
    maps = Maper.getMaps(question, rule)
    print("------------")
    print(rule.name)
    #rule.transRules.print()
    #print("map.getMaps(question, rule) = ", end="")
    print(maps)

    print("------------")
    print("TEST Transformer")
    g =  question
    question.print()
    print("------------>")
    rule = rules[2]
    print(rule.name)
    maps = Maper.getMaps(g, rule)
    g = Transformer.transform(rule.transRules, g, maps[0])
    g.print()
    print("------------>")
    rule = rules[3]
    maps = Maper.getMaps(g, rule)
    g = Transformer.transform(rule.transRules, g, maps[0])
    g.print()
    print("------------>")
    rule = rules[0]
    print(rule.name)
    maps = Maper.getMaps(g, rule)
    g = Transformer.transform(rule.transRules, g, maps[0])
    g.print()
    print("------------>")
    rule = rules[2]
    print(rule.name)
    maps = Maper.getMaps(g, rule)
    g = Transformer.transform(rule.transRules, g, maps[0])
    g.print()
    print("------------>")
    rule = rules[1]
    print(rule.name)
    maps = Maper.getMaps(g, rule)
    g = Transformer.transform(rule.transRules, g, maps[0])
    g.print()
    print("------------>")
    rule = rules[3]
    print(rule.name)
    maps = Maper.getMaps(g, rule)
    g = Transformer.transform(rule.transRules, g, maps[0])
    g.print()
    print("------------>")
    rule = rules[2]
    print(rule.name)
    maps = Maper.getMaps(g, rule)
    g = Transformer.transform(rule.transRules, g, maps[0])
    g.print()

    print(Maper.getMaps(g, Reader.goalToRule("goal.json")))

    print(list([]))
