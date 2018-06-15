# Graph Transformation System

成员：向东伟、林天梁

### 组成

根目录下

- `Graph.py`
- `Rule.py`
- `Transformer.py`
- `Maper.py`
- `Reader.py`
- `Writer.py`
- `SolveBFS.py`
- `SolveAStar.py`

### Demo

运行`python3 SolveAstar.py`，可以查看调用**GTS**解决推箱子、过河问题、句法分析问题的结果：

1. 对于推箱子、过河问题，将会按照顺序输出为了解决问题，每一步所应用的rule。
2. 对于句法分析问题，还会自动在`examples/parsing/`目录下生成`result.json`，自动在`visualize/parsing/`目录下生成`result.png`。

详情可见`SolveAstar.py`源代码。