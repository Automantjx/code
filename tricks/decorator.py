# 提升代码复用 将装饰器应用在这些函数上，而不是在这些函数内加上一样的代码
# 保证函数逻辑清晰 
# 拓展别人的函数 不用修改源码

# 函数是一等对象 即 函数可以作为参数传递到函数中

def square(x):
    return x*x

def print_running(f, x):
    print(f'{f.__name__} is running.')
    return f(x)

result = print_running(square, 2)
print(result)


import time

def decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'{func.__name__} is running, execution time is {end_time-start_time}.')
        return result
    return wrapper
decorated_square = decorator(square)
decorated_square(10)

@decorator
def square(x):
    return x*x

square(10)

import functools
# 定义一个定义装饰器的函数，即装饰器生成器，根据参数生成不同的装饰器
def timer(threshold):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            if end_time-start_time>threshold:
                print(f'{func.__name__} tooker longer than {threshold}.')
            return result
        return wrapper
    return decorator

@timer(0.2)
def sleep_04():
    time.sleep(0.4)
# 等价于 timer(0.2)(sleep_04)

sleep_04()
print(sleep_04.__name__)  # 不加functools是wrapper  加了是sleep_04