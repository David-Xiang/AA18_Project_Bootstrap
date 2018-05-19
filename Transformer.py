# coding: utf-8

import copy
class Transformer:
    class TransRules:
        def __init__(self, delVertex, addVertex, delEdge, addEdge):
            self.delVertex = delVertex
            self.addVertex = addVertex
            self.delEdge = delEdge
            self.addEdge = addEdge
        def print(self):
            print("delVertex = ", end="")
            print(self.delVertex)
            print("addVertex = ", end="")
            print(self.addVertex)
            print("delEdge = ", end="")
            print(self.delEdge)
            print("addEdge = ", end="")
            print(self.addEdge)

    @staticmethod
    def generateTransRules(lhs, rhs):
        '''返回{"delVertex": [], "delEdge": [(fromVertex, toVertex, edgeType)],
                "addVertex": [(id, type)], "addEdge": [(fromVertex, toVertex, edgeType)]}'''
        delVertex = Transformer.diff(lhs.getAllVertex(), rhs.getAllVertex())  # 执行删点时，要删除所有的关联边


        addVertex = []
        arr = Transformer.diff(rhs.getAllVertex(), lhs.getAllVertex())
        for vertex in arr:
            addVertex.append((vertex, rhs.getType(vertex)))

        remainVertex = lhs.getAllVertex() - delVertex

        delEdge = []
        # print(remainVertex)
        for fromVertex in remainVertex:
            for toVertex in remainVertex:
                arr = Transformer.diff(lhs.getEdges(fromVertex, toVertex), rhs.getEdges(fromVertex, toVertex))
                if len(arr) > 0:
                    for edgeType in arr:
                        delEdge.append((fromVertex, toVertex, edgeType))

        addEdge = []  # 这里比较麻烦，添加的边分为三类，

        for fromVertex in remainVertex:
            for toVertex in remainVertex:
                arr = Transformer.diff(rhs.getEdges(fromVertex, toVertex), lhs.getEdges(fromVertex, toVertex))
                if len(arr) > 0:
                    for edgeType in arr:
                        addEdge.append((fromVertex, toVertex, edgeType))

        for fromVertex in remainVertex:
            for (toVertex, vType) in addVertex:
                arr = rhs.getEdges(fromVertex, toVertex)
                if len(arr) > 0:
                    for edgeType in arr:
                        addEdge.append((fromVertex, toVertex, edgeType))

        for (fromVertex, vType) in addVertex:
            for toVertex in rhs.getAllVertex():
                arr = rhs.getEdges(fromVertex, toVertex)
                if len(arr) > 0:
                    for edgeType in arr:
                        addEdge.append((fromVertex, toVertex, edgeType))

        return Transformer.TransRules(delVertex, addVertex, delEdge, addEdge)

    @staticmethod
    def transform(transRules, graph, map):
        #transRules.print()
        for (vertex, vType) in transRules.addVertex:
            map[vertex] = vertex
        #print(map)

        newGraph = copy.deepcopy(graph)

        for vertex in transRules.delVertex:
            newGraph.delVertex(map[vertex])

        for (vertex, vType) in transRules.addVertex:
            newGraph.addVertex(map[vertex], vType)

        for (fromVertex, toVertex, edgeType) in transRules.delEdge:
            #print("delEdge" + map[fromVertex] + map[toVertex] + edgeType)
            newGraph.delEdge(map[fromVertex], map[toVertex], edgeType)

        for (fromVertex, toVertex, edgeType) in transRules.addEdge:
            newGraph.addEdge(map[fromVertex], map[toVertex], edgeType)

        return newGraph

    @staticmethod
    def diff(a, b):

        la = list(a)
        for i in b:
            for j in la:
                if i == j:
                    la.remove(j)
                    break
        return la
