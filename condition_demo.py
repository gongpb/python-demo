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
print("------列表推导式 end--------")

