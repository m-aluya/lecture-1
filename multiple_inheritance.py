class OpsA:
    def interest(self,P):
        return (P * 3.92 * 10)/100
    
    
class OpsB:
    def interest(self,P):
        return (P * 2.92 * 10)/100
            
            
            
class finalOps(OpsB,OpsA):
    def x(self):
        print("This is X")            
    
    
v = finalOps()
print(v.interest(4000))    