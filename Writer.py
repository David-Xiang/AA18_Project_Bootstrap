# coding: utf-8

from Graph import Graph
import json

class Writer:
    '''将match goal.json的Graph对象储存为json文件'''
    @staticmethod
    def graphToJson(graph, path):
        newdict = {}
        newdict["relations"] = []
        newdict["objects"] = [{"id": i, "type": graph.getVertexType(i)} for i in graph.getAllVertex()]
    
        for fromVertex in graph.getAllVertex():
            for toVertex in graph.getAllVertex():
                arr = graph.getEdges(fromVertex, toVertex)
                if len(arr) > 0:
                    for edgeType in arr:
                        newdict["relations"].append({"type": edgeType, "source": fromVertex, "target": toVertex})

        with open(path, "w") as f:
            json.dump(newdict, f)