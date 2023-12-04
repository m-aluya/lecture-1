class A:
    def a(self):
        print("Method from class A")

class B:
    def b(self):
        print("Method from class B")

class C(A,B):
    def c(self):
        print("Method from class C")
        
        

obj = C()
obj.a()                        