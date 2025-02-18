print("----------基本数据结构 start------------")    
import keyword
keyword.kwlist
print(keyword.kwlist)
print("Helle word")

if True:
    print ("True")
else:
    print ("False")
    
print("----------------------")    
num_int = 123
num_float = 1.23

num_new = num_int + num_float

print("num_int 数据类型为:",type(num_int))
print("num_flo 数据类型为:",type(num_float))

print("num_new 值为:",num_new)
print("num_new 数据类型为:",type(num_new))

print("----------基本数据结构 end------------")    

print(ord("a"))

str1="hello world"

print(str1.upper())
print(str1.lower())
print(str1.capitalize())
print(str1[0:3])

print("\a")

print ("h" in str1)    

print("-----------元组 start----------")

tup = ('r', 'u', 'n', 'o', 'o', 'b')

## tup[0] = 'g' 

id(tup)

print("-----------元组 end----------")