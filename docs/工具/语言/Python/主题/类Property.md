# 类 Property

例子来自《Learning Python》。

```python
class Person:
    def __init__(self, name):
        # 通常用带下划线的名字作为实际值
        self._name = name

    @property
    def name(self):  # name = property(name)
        """name property docs"""
        print('fetch...')
        return self._name

    # setter 和 deleter 的名字也都是 name
    @name.setter
    def name(self, value):  # name = name.setter(name)
        print('change...')
        self._name = value

    @name.deleter
    def name(self):  # name = name.deleter(name)
        print('remove...')
        del self._name
```
