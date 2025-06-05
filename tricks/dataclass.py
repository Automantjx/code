class Student:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        pass
    
    def __repr__(self) -> str:
        pass


from dataclasses import dataclass,field

@dataclass
class Student:
    name:str
    age:int = 10 # 默认值

s_1 = Student("yun", 33)
print(s_1)

s_2 = Student("aaa", 33)
print(s_2)

print(s_1 == s_2)

s_3 = Student("ddd")
print(s_3)


# 对象创建完成后不能修改属性的值
@dataclass(frozen=True) 
class Student:
    name:str
    age:int
student = Student("Jack", 20)
# student.age = 22  # error


# annoation

# 希望某个属性存在，但又不希望他出现在构造函数里
@dataclass(order=True)  # 排序 先比较第一个属性，一样则比较第二个
class Student:
    sort_index: int = field(init=False, repr=False)  # 先比较age
    
    name:str
    age:int = 19
    independent:bool = field(default=False, init=False, repr=True)  # 默认值 不出现在构造函数里 打印出来

    def __post_init__(self):
        self.independent = self.age > 18
        self.sort_index = self.age
    
s1 = Student("xixi")
print(s1)
s2 = Student("xingxing", 15)
print(s2)
students = [s1, s2]
sorted_students = sorted(students)
print(sorted_students)


import operator
students.sort(key = operator.attrgetter('age')) # 先比较age
print(students)