# coding: utf-8

from Reader import Reader


class Maper:
    @staticmethod
    def getMaps(graph, rule):
        '''参数分别为Graph和Rule对象，已经固定的部分顶点映射（用于匹配nac），
        定义映射map:rule.lhs->f[Graph]，返回值为所有映射map的列表，或者 None(找不到满足条件的映射)'''

        mapList = Maper.searchMap(rule.lhs, graph, {})
        # print(rule.lhs)
        # print(graph)
        # print(mapList)

        for mp in mapList:
            foundNac = False
            for nac in rule.nacs:
                mapPartial = {}
                for i in [i for i in mp.keys() if i in nac]:
                    mapPartial[i] = mp[i]
                # 既在lhs中出现，又在nac中出现的元素

                searchResult = Maper.searchMap(nac, graph, mapPartial)
                if searchResult is not None and len(searchResult) != 0:  # 能够找到nac在graph中的映射
                    foundNac = True
                    break
            if foundNac is True:
                mapList.remove(mp)

        return mapList

    @staticmethod
    def searchMap(graph1, graph2, mapPartial):
        # 在g2中寻找同构与g1的子图, fPartial表示已经固定的部分顶点映射

        #if len([i for i in mapPartial.keys() if i not in graph1]) != 0:
            # 出错
            #raise IndexError("searchMap: fPartial keys are wrong!")
        #if len([i for i in mapPartial.values() if i not in graph2]) != 0:
            #raise IndexError("searchMap: fPartial values are wrong!")

        mapList = []
        mp = dict().fromkeys(graph1.getAllVertex(), None)
        mp.update(mapPartial)

        Maper.backtrack(
            graph1,
            graph2,
            mp,
            mapList,
            [i for i in graph1.getAllVertex() if mp[i] is None],
            [j for j in graph2.getAllVertex() if j not in mp.values()])
        # graph.getAllVertex返回的是所有顶点的id
        # 在mapList中生成所有可能的映射（对应顶点类型相同）

        #print("possible map: ", end="")
        #print(mapList)
        for mp in mapList[:]:
            if Maper.checkMap(graph1, graph2, mp) is False:  # 边的对应不满足
                mapList.remove(mp)
        return mapList

    @staticmethod
    def backtrack(graph1, graph2, mapPartial, rtnList, remain1, remain2):
        '''回溯法生成所有可能映射，rtnList'''
        if len(remain1) == 0:
            rtnList.append(dict(mapPartial))
            return
        elif len(remain2) == 0:
            return
        else:
            i = remain1.pop()
            for j in [j for j in remain2 if graph1.getVertexType(i) == graph2.getVertexType(j)]:
                mapPartial[i] = j
                remain2.remove(j)
                Maper.backtrack(graph1, graph2, mapPartial, rtnList, remain1, remain2)
                mapPartial[i] = None
                remain2.append(j)

            remain1.append(i)

    @staticmethod
    def checkMap(graph1, graph2, mp):
        for i in mp.keys():
            for j in mp.keys():
                fi = mp[i]
                fj = mp[j]
                g1toEdges = graph1.getEdges(i, j)
                g2toEdges = graph2.getEdges(fi, fj)

                if g1toEdges is not None and g2toEdges is None:
                    return False
                elif g1toEdges is None:
                    continue

                if (len(Maper.diff(g1toEdges, g2toEdges)) != 0):
                    return False
        return True

    @staticmethod
    def diff(a, b):
        if len(a) == 0:
            return []

        la = list(a)
        for i in b:
            for j in la:
                if i == j:
                    la.remove(j)
                    break
        return la

if __name__ == "__main__":
    question = Reader.questionToGraph("trival.json")
    rules = Reader.rulesToRules("rules.json")

    print("TEST Map")
    maps = Maper.getMaps(question, rules[2])
    print("map.getMaps(question, rule) = ", end="")
    print(maps)
