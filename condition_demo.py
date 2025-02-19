#!/usr/bin/python3
 
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    print(site)

print("------斐波纳契数列 start--------")
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b
    
print("------斐波纳契数列 end--------")

print("------列表推导式 start--------")
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names = [name for name in names if len(name)>3]
print(new_names)

multiples = [i for i in range(50) if i % 3 == 0]
print(multiples)

setnew = {i**2 for i in (1,2,3,4,5)}
print(setnew)

setnew = {i*2 for i in (1,2,3,4,5)}
print(setnew)

t1=range(1,10)
a=(i for i in t1)
a1 = tuple(a)
print("a1：", a1)


list1 = ['python', 'test1', 'test2']
list2 = [word.title() if word.startswith('p') else word.upper() for word in list1]
print(list2)

print("------列表推导式 end--------")

print("------生成器表达式 start--------")

def countdown(n):
    while n > 0:
        yield n
        n -= 1
 
# 创建生成器对象
generator = countdown(5)
 
# 通过迭代生成器获取值
#print(next(generator))  # 输出: 5
#print(next(generator))  # 输出: 4
print("next",next(generator))  # 输出: 3
    
# 使用 for 循环迭代生成器
for value in generator:
    print(value)  # 输出: 2 1
 
print("------生成器表达式 end--------")


print ("------装饰器 start--------")
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

print ("------装饰器 end--------")


# 九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()
