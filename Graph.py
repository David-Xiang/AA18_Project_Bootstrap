# coding: utf-8

class Graph:
    '''允许重复边的有向图模型'''

    class Vertex:
        '''connList为字典：键为本顶点对应的ToVertex的id，值为确定fromVertex和toVertex的出边列表'''

        def __init__(self, id, vertexType):
            self.__id = id
            self.__type = vertexType
            self.__connList = {}

        def addEdge(self, id, edgeType):
            if id in self.__connList:
                self.__connList[id].append(edgeType)
            else:
                self.__connList[id] = [edgeType]

        def delEdges(self, id):
            if id in self.__connList:
                del self.__connList[id]

        def delEdge(self, id, edgeType):
            if id in self.__connList and edgeType in self.__connList[id]:
                self.__connList[id].remove(edgeType)
            else:
                raise IndexError("delEdge: toVertex or edgeType does not match!")

        def getEdges(self, id):
            if id not in self.__connList:
                return []
            else:
                return list(self.__connList[id])

        def getToVertex(self):
            return self.__connList.keys()

        def getId(self):
            return self.__id

        def getType(self):
            return self.__type

        def printToEdge(self):
            for id in self.__connList.keys():
                for type in self.__connList[id]:
                    print("{}  ({})  {}".format(self.__id, type, id))



    def __init__(self, name):
        self.__vertexList = {} # 映射：id -> Vertex对象
        self.vertexNum = 0
        self.name = name

    def __contains__(self, id):
        for i in self.__vertexList.keys():
            if i == id:
                return True
        return False

    def __getVertex(self, id):
        if id in self.__vertexList.keys():
            return self.__vertexList[id]
        else:
            return None

    def addVertex(self, id, type):
        if self.__getVertex(id) is not None:
            raise IndexError("addVertex: Repeat adding vertex!")

        #print("Add vertex id = {} type = {}.".format(id, type))
        self.__vertexList[id] = self.Vertex(id, type)
        self.vertexNum += 1

    def delVertex(self, id):
        if self.__getVertex(id) is None:
            raise IndexError("delVertex: Delete a non-existent vertex!")
        else:
            del self.__vertexList[id]
            self.vertexNum -= 1
            for i in self.__vertexList.keys():
                self.__getVertex(i).delEdges(id)

    def delEdge(self, fromVertex, toVertex, Edgetype):
        if self.__getVertex(fromVertex) is None:
            raise IndexError("delEdge: Delete on non-existent vertex!")
        else:
            self.__getVertex(fromVertex).delEdge(toVertex, Edgetype)

    def getVertexType(self, id):
        if self.__getVertex(id) is None:
            raise IndexError("getVertexType: Query a non-existent vertex!")
        else:
            return self.__getVertex(id).getType()

    def getEdges(self, fromVertex, toVertex):
        # 输入都是id，给定fromVertex和toVertex对应的所有边的列表
        if self.__getVertex(fromVertex) is None or self.__getVertex(toVertex) is None:
            raise IndexError("getEdgeType: Query a non-existent vertex!")
        else:
            return self.__vertexList[fromVertex].getEdges(toVertex)

    def getAllEdges(self, fromVertex):
        '''返回字典一个，键是toVertex的id，值是对应所有边的列表'''
        if self.__getVertex(fromVertex) is None:
            raise IndexError("getToVertex: Query a non-existent vertex!")
        else:
            rtnDict = {}

            for toVertex in self.__vertexList[fromVertex].getToVertex():
                rtnDict[toVertex] = self.__vertexList[fromVertex].getEdges(toVertex)

            return rtnDict

    def getAllVertex(self):
        '''返回所有vertex的id'''
        return self.__vertexList.keys()

    def getType(self, id):
        if self.__getVertex(id) is None:
            raise IndexError("getType: Query a non-existent vertex!")
        return self.__getVertex(id).getType()

    def addEdge(self, fromVertex, toVertex, type):
        if self.__getVertex(fromVertex) is None:
            raise IndexError("addEdge: Add edge on a non-existent vertex {}!".format(fromVertex))
        else:
            self.__vertexList[fromVertex].addEdge(toVertex, type)

    def print(self):
        for v in self.__vertexList.keys():
            self.__vertexList[v].printToEdge()


if __name__ == "__main__":
    '''test Vertex and Graph'''
    v = Graph.Vertex(0, "src")
    v.addEdge(1, "is")
    v.addEdge(2, "has")
    v.addEdge(1, "has")
    v.printToEdge()

    print("--------------")

    g = Graph("metamodel")
    g.addVertex("Farmer", "Farmer")
    g.addVertex("Wolf", "Wolf")
    g.addVertex("Goat", "Goat")
    g.addVertex("Vegetable", "Vegetable")
    g.addVertex("Side", "Side")
    g.addVertex("Goal", "Goal")
    g.addVertex("StartingPoint", "StartingPoint")

    if "Farmer" in g:
        print("in")

    g.addEdge("Farmer", "Side", "on")
    g.addEdge("Wolf", "Side", "on")
    g.addEdge("Goat", "Side", "on")
    g.addEdge("Vegetable", "Side", "on")
    g.addEdge("Side", "Side", "next to")
    g.addEdge("Side", "Goal", "is")
    g.addEdge("Side", "StartingPoint", "is")
    g.print()
    print(g.getAllVertex())
