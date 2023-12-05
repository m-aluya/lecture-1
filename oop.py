class Person:
    name = ""
    email =""
    race =""
    gender = ""
        
        
    def run(self,name):
        print(name + "  can run")  
        
    def sleep(self):
        print("Yes i can sleep")    
        
        
    def read(self):
        print("I can read")
     
    def eat(self):
        print("I can eat")
    
    def drive(self):
        print("I can drive")
        
obj = Person()
obj.name = "Mason"
obj.run(obj.name)