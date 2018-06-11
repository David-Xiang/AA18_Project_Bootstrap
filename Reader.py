# coding: utf-8

from Graph import Graph
from Rule import Rule
import json

class Reader:
    @staticmethod
    def metamodelToGraph(path):
        g = Graph("metamodel")
        with open(path) as f:
            jsonFile = json.load(f)
        if "classes" in jsonFile:
            for classes in jsonFile["classes"]:
                g.addVertex(classes["id"], classes["id"])
        if "relations" in jsonFile:
            for relations in jsonFile["relations"]:
                g.addEdge(relations["source"], relations["target"], relations["id"])
        return g

    @staticmethod
    def questionToGraph(path):
        g = Graph("question")
        with open(path) as f:
            jsonFile = json.load(f)
        if "objects" in jsonFile:
            for objects in jsonFile["objects"]:
                g.addVertex(objects["id"], objects["type"])
        if "relations" in jsonFile:
            for relations in jsonFile["relations"]:
                g.addEdge(relations["source"], relations["target"], relations["type"])
        return g

    @staticmethod
    def rulesToRules(path):
        rules = []
        with open(path) as f:
            jsonFile = json.load(f)
        for rule in jsonFile:
            lhs = Graph(rule["id"])
            if "objects" in rule["lhs"]:
                for objects in rule["lhs"]["objects"]:
                    lhs.addVertex(objects["id"], objects["type"])
            if "relations" in rule["lhs"]:
                for relations in rule["lhs"]["relations"]:
                    lhs.addEdge(relations["source"], relations["target"], relations["type"])

            rhs = Graph(rule["id"])
            if "objects" in rule["rhs"]:
                for objects in rule["rhs"]["objects"]:
                    rhs.addVertex(objects["id"], objects["type"])
            if "relations" in rule["rhs"]:
                for relations in rule["rhs"]["relations"]:
                    rhs.addEdge(relations["source"], relations["target"], relations["type"])

            nacs = []
            cnt = 0
            if "nacs" in rule:
                for nac in rule["nacs"]:
                    str = "nac {}".format(cnt)
                    cnt += 1
                    g = Graph(str)
                    if "objects" in nac:
                        for objects in nac["objects"]:
                            g.addVertex(objects["id"], objects["type"])
                    if "relations" in nac:
                        for relations in nac["relations"]:
                            g.addEdge(relations["source"], relations["target"], relations["type"])
                    nacs.append(g)

            rules.append(Rule(rule["id"], lhs, rhs, nacs))

        return rules

    @staticmethod
    def goalToRule(path):
        with open(path) as f:
            jsonFile = json.load(f)
        lhs = Graph("lhs")
        if "objects" in jsonFile["graph"]:
            for objects in jsonFile["graph"]["objects"]:
                lhs.addVertex(objects["id"], objects["type"])
        if "relations" in jsonFile["graph"]:
            for relations in jsonFile["graph"]["relations"]:
                lhs.addEdge(relations["source"], relations["target"], relations["type"])

        rhs = Graph("rhs")

        nacs = []
        cnt = 0
        if "nacs" in jsonFile:
            for nac in jsonFile["nacs"]:
                str = "nac {}".format(cnt)
                cnt += 1
                g = Graph(str)
                if "objects" in nac:
                    for objects in nac["objects"]:
                        g.addVertex(objects["id"], objects["type"])
                if "relations" in nac:
                    for relations in nac["relations"]:
                        g.addEdge(relations["source"], relations["target"], relations["type"])
                nacs.append(g)

        return Rule("goal", lhs, rhs, nacs)


if __name__ == "__main__":
    '''test Reader'''
    #print("------------")
    #print("TEST metamodelToGraph")
    #g = Reader.metamodelToGraph("metamodel.json")
    #g.print()

    print("------------")
    print("TEST quesionToGraph")
    g1 = Reader.questionToGraph("./examples/parsing/instances/trivialHard.json")
    import sys
    print(sys.getsizeof(g1))
    g1.print()

    #print("------------")
    #print("TEST rulesToMatches")
    #rules = Reader.rulesToRules("rules.json")
    #for rule in rules:
    #    print("------------")
    #    rule.print()

    #print("------------")
    #print("TEST goalToRule")
    #goal = Reader.goalToRule("goal.json")
    #goal.print()
