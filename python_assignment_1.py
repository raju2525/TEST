#use builtin methods (str,list) two activities

print(dir(str))
a  = "hello"
b=a.title()
print(b)
a = 'hello world'
b = a.upper()
print(b)
a = 'hello world'
b=a.replace('hello','Hi')
print(b)
C=b.split(' ')
print(C)
C='12345'
print(C.isdigit())
a = range(10)
b=list(a)
print(list(a)) 
my_list  = list(range(5,10,2))
my_list

#user defined function


def my_function(a, b):
    result = a-b
    return result

result = my_function(5, 3)
print(result)
