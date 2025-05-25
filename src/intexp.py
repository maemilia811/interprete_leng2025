from state import * 
class IntExp: 
    def __repr__(self):
        pass
    def run(): 
        pass

class Var(IntExp): 
    def __init__(self, var:str):
        self.var = var

    def __repr__(self):
        return f"{self.var}"
    
    def run(self,state:State): 
        if str(self.var) in state.keys():
            return state[self.var]
        else: # attention
            return 0  
        
class Nat(IntExp): 
    def __init__(self, number:int):
        self.n = number
    
    def __repr__(self):
        return f"Nat({self.n})"

    def run(self,state:State): 
        return self.n 

class Sum(IntExp): 
    def __init__(self, expr1:IntExp, expr2:IntExp): 
        self.sum1 = expr1
        self.sum2 = expr2

    def __repr__(self):
        return f"Sum({self.sum1},{self.sum2})"
    
    def run(self, state:State): 
        sum1 = self.sum1.run(state)
        sum2 = self.sum2.run(state)        
        return sum1 + sum2 
    

         
class Product (IntExp): 
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2
    
    def __repr__(self):
        return f"Product({self.expr1},{self.expr2})"

    def run(self): 
        return self.expr1 * self.expr2


    
#Corrrgit todas con el estado 


#Las funciones semánticas en intexpr tienen distinto tipo de las de comandos 