print(f'{1 + 2 = }')
print(f'{'a' + 'b' = }')

# __add__   dunder method   dunder -- double under
print((x:=1).__add__(2))  # := 对中间变量赋值
print('a'.__add__('b'))

from typing import Any, List
class ShoppingCart:
    def __init__(self, items: List[str]) -> None:
        self.items = items
        
    def __add__(self, another_cart):
        new_cart = ShoppingCart(self.items + another_cart.items)
        return new_cart

    def __str__(self) -> str:
        return f'{self.items}'
    
    def __len__(self):
        return len(self.items)
    
    def __call__(self,item, *args: Any, **kwds: Any) -> Any:
        self.items.append(item)

cart1 = ShoppingCart(["apple", "banana"])
cart2 = ShoppingCart(["orange", "pear"])
new_cart = cart1 + cart2
print(new_cart.items)

cart = ShoppingCart(["apple", "banana"])
print(cart)  # 打印出来的是类对象 __str__
cart('orange')  # __call__ 让实例像函数一样调用
print(cart)
print(len(cart))