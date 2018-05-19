# GTS and Parsing Problem

成员：向东伟、林天梁

## Graph Transformation System

### 组成

根目录下

- `Graph.py`
- `Rule.py`
- `Transformer.py`
- `Maper.py`
- `Reader.py`
- `Writer.py`

### Demo

运行`python3 Solve.py`，可以查看调用**GTS**解决推箱子、过河问题、句法分析的结果：

1. 对于推箱子、过河问题，将会按照顺序输出为了解决问题，每一步所应用的rule
2. 对于句法分析问题，还会自动在`examples/parsing/`目录下生成`result.json`，自动在`visualize/parsing/`目录下生成`result.png`。

详情可见`Solve.py`源代码

## Parsing Problem 句法分析

### 说明

我们试图采用GTS模型来解决中文句法分析的问题。

利用分词工具，对给定句子进行分词，得到的词语列表看作是语义模块的列表。

应用汉语语法的基本规则可以确定不同语义模块之间的关系：例如并列关系（表现为图模型中的并列关系），修饰关系（表现为图模型中的从属关系，修饰成分从属于被修饰成分），主谓关系等等。

初始情况下，句子的图模型成链状。经过多次Transform之后，如果能够匹配某一种汉语句式（SVO主谓宾，SV主谓，SVOO主谓双宾等），则目标达成，输出匹配目标的图模型对应的JSON文件。

在实践中，我们发现自然语言处理的问题实在是博大精生。对于正式化的、符合我们预设的标准汉语句法结构的句子在实际中是少之又少的。因此，**本模型的精确程度高度依赖于设定的rules是否完备**，以及分词的准确性。作为试验，我们仅仅加入了十余条rule，这是远远不够的。

### 三个例子

我们选取了三个难度不同的例子，对句法分析模型作一展示。

#### “我爱北京天安门” 7字

输出为：

![天安门（结果）](tiananmen(result).png)



#### “他 试图 传授 一点 人生 的 经验” 12字

简化后的输出为：

![人生经验（简化）](jingyan(result_simplified).png)

原始输出为：

![人生经验（结果）](jingyan(result).png)

#### “他 在 记者会 上 表示 按照 香港 的 基本法 支持 特首 董先生 的 连任” 26字

简化后的输出为：

![基本法（结果简化）](jibenfa(result_simplified).png)

原始输出为（**高能预警**）：

![基本法（结果）](jiebenfa(result).png)