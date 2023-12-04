def pay(f_arg,*argv):
    print("The argument passed is is",f_arg)
    
    for arg in argv:
        print("Another argument is ", arg)

pay("Monday","Wale","Saturday","Stanley","Amaka","Amos") 

def test_args_kwargs(arg1,arg2,arg3):
    print("arg1",arg1)
    print("arg2",arg2)
    print("arg3",arg3)
    
args =("two",3,6)
test_args_kwargs(*args)    

kwargs = {"arg3":3,"arg2":2,"arg1":1}
test_args_kwargs(**kwargs)