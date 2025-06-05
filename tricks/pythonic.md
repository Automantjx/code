## 命名约定

Function/Method:小写单词，下划线分割  
Variable:小写单词，下划线分割  
Constant:大写单词，下划线分割  
Class:大写单词，驼峰  
**Module:小写单词，下划线分割**  
**Package:小写单词，不用下划线分割**

## 布局
**空行**  
函数内不同的步骤用空行分割  
类和函数之间两个空行  
类中方法一个空行  
**每行最大的字符长度与分行符**  
\ 显示分割 space隐式分割  
二元运算符前分段  
**缩进**  
4 spaces / tab  
**换行后缩进**  
**定位闭合括号**  
**表达式和语句中的空格**  

## python的控制结构
1.复杂的列表推导  
2.lambda的使用  
3.我们可以在循环中使用else吗  
4.生成器or列表推导  
5.在python3中使用增强的范围 --> range()

## 整洁的python代码
1.自由使用断言  
2.逗号应该放在哪里  
3.上下文管理器的with语句  
4.魔术方法、下划线和其他功能  
5.关于格式化字符串的秘密



## \_\_anonation\_\_
```python
class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius
        self.area = 0
    
def area(radius:float) -> float:
    "compute area of a circle with given radius"
    pass

print(area.__annotations__)
# {'para':'para type', 'return':'return type'}
```



