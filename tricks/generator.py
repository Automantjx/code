def square_numbers(nums):
    for i in nums:
        yield i*i

my_nums = square_numbers([1,2,3,4,5])
print(my_nums)
print(next(my_nums))
print("==========")
for num in my_nums:
    print(num)
    
my_gen = (i*i for i in range(5))
print(my_gen)