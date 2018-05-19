# coding: utf-8

from Reader import Reader
from Writer import Writer
from Maper import Maper
from Transformer import Transformer
import os
import json

class QueueElem:
    def __init__(self, graph, path):
        self.graph = graph
        self.path = path

def bfs(question, rules, goal):
    queue = [QueueElem(question, [])]
    while len(queue) > 0:
        temp = queue[0]
        graph = temp.graph
        path = temp.path

        if len(Maper.getMaps(graph, goal)) != 0:
            return (graph, path)

        for rule in rules:
            maps = Maper.getMaps(graph, rule)
            for map in maps:
                ng = Transformer.transform(rule.transRules, graph, map)
                np = list(path)
                np.append(rules.index(rule))
                queue.append(QueueElem(ng, np))

        queue.remove(temp)

    return []


if __name__ == "__main__":
    # 解过河问题，并输出步骤
    print("------------")
    print("Solution for 过河问题")
    question = Reader.questionToGraph("examples/cross_river/instances/question.json")
    rules = Reader.rulesToRules("examples/cross_river/rules.json")
    goal = Reader.goalToRule("examples/cross_river/goal.json")  # goal其实是一个rule
    (goalGraph, path) = bfs(question, rules, goal)

    if len(path) > 0:
        print("rules applied are (in order):")
        for i in path:
            print(rules[i].name) # 输出transform的步骤（依次应用了哪些规则）

    # 解推箱子，并输出步骤
    print("------------")
    print("Solution for 推箱子")
    question = Reader.questionToGraph("examples/sokoban_game/instances/trivial.json")
    rules = Reader.rulesToRules("examples/sokoban_game/rules.json")
    goal = Reader.goalToRule("examples/sokoban_game/goal.json")
    (goalGraph, path) = bfs(question, rules, goal)

    if len(path) > 0:
        print("rules applied are (in order):")
        for i in path:
            print(rules[i].name)

    # 解句法分析问题，输出match goal.json的图（可视化成图片）
    print("------------")
    print("Solution for 句法分析")
    question = Reader.questionToGraph("examples/parsing/instances/trivial.json")
    rules = Reader.rulesToRules("examples/parsing/rules.json")
    goal = Reader.goalToRule("examples/parsing/goal.json")
    (goalGraph, path) = bfs(question, rules, goal)

    if len(path) > 0: # 搜索到了match goal.json 的图
        print("rules applied are (in order):")
        for i in path:
            print(rules[i].name)

        print("调用Writer将结果保存至examples/parsing/result.json")
        print("使用check_and_visualize.py可得可视化结果")

        # 使用check_and_visualize.py生成结果的图片
        Writer.graphToJson(goalGraph, "examples/parsing/instances/result.json")
        os.system("python3 utils/check_and_visualize.py parsing --instance instances/result.json")

        # 为了比较，使用check_and_visualize.py生成问题的图片
        os.system("python3 utils/check_and_visualize.py parsing --instance instances/trivial.json")