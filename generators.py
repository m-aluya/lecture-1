# def gen_func():
#     for i in range(10):
#         yield i

# for item in gen_func():
#     print(item)      
    
    
def fib(n):
    a= b =1
    for i in range(n):
        yield a 
        a,b= b,a+b
      
for x in fib(10):
    print(x)      