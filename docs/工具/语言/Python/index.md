# Python

## 升级版本（Windows）

从 3.9.5 升级到 3.9.6，安装程序会自动升级。从 3.9 升级到 3.10，不会升级 3.9，而是另外安装 3.10，两个版本同时存在。

## 冷知识

1. `for`、`while` 和 `try` 都可以接 `else`，详见 [Python 文档](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)。
1. 拆包 `*xs` 和 `**d`，`xs` 可以是 list 或 tuple，`d` 可以是 dict。
1. 在 expression 中赋值用 `:=`，叫 walrus operator，例子：
    ```python
    if (a := 1) > 0:
      print(a)
    ```
