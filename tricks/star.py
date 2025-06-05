# 重复
print('ha'*3)

# 打包  *-list turple **-dict
numbers = [1,2,3,4,5]
first, *rest = numbers
print(first)
print(rest)

def print_value(*args):
    for arg in args:
        print(arg)
print_value(1,2,3,4)

def example(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}={value}')
example(a=1, b=2, c=3)

# 解包
def greet(name, age):
    print(f'hello {name}, you are {age} years old')

person = ('alice', 13)
greet(*person)

list1 = [1,2,3]
tuple1 = (4,5,6)
merged = [*list1, *tuple1]
print(merged)

def create_profile(name, age, email):
    print(f'name:{name}, age:{age}, email:{email}')
option = {
    "name":"tony",
    "age":18,
    "email":"tony@qq.com"
}
create_profile(**option)

dict1 = {"a":1, "b":2}
dict2 = {"c":3, "d":4}
merged = {**dict1, **dict2}
print(merged)

def print_arguments(*args, **kwargs):
    print(args)
    print(kwargs)
print_arguments(1,2,3,name='john',age=30)