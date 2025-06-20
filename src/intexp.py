from type import * 
#from output import * 
""" Función semántica para cada comando, 
run :: State -> Z """

class IntExp: 
    def __repr__(self):
        pass
    def run(): 
        pass

class Var(IntExp):    
    def __init__(self, var:str):
        if isinstance(var, str): 
            self.var = var
        else: 
            raise TypeError("Variable debe ser un string")

    def __repr__(self):
        return f"{self.var}"
    
    def run(self, state):
        if isinstance(state, State):
            if str(self.var) in state.keys():
                return state[str(self.var)]
            else: 
                return 0
        elif isinstance(state, Output_type) or isinstance(state,Fail_type):
            return self.run(state[1])
        else:
            raise TypeError(f"Estado no reconocible: {state!r}")

class Num(IntExp):
    def __init__(self, number:int):
        if isinstance(number, int):
            self.n = number
        else:
            raise TypeError(f"Num solo acepta enteros de tipo int, pero recibió {type(number).__name__}")
   
    def __repr__(self):
        return f"Num({self.n})"

    def run(self,state:State): 
        return self.n 

class Sum(IntExp): 
    def __init__(self, expr1:IntExp, expr2:IntExp): 
        if (isinstance(expr1,IntExp) and isinstance(expr2, IntExp)): 
            self.sum1 = expr1
            self.sum2 = expr2
        else: 
            raise TypeError(f"Sum solo acepta expresiones de tipo Intexp")
        
    def __repr__(self):
        return f"Sum({self.sum1},{self.sum2})"
    
    def run(self, state:State):         
        return self.sum1.run(state) + self.sum2.run(state) 
    
class Product (IntExp): 
    def __init__(self, expr1:IntExp, expr2:IntExp):
        if (isinstance(expr1,IntExp) and isinstance(expr2, IntExp)): 
            self.expr1 = expr1
            self.expr2 = expr2
        else: 
            raise TypeError(f"Product solo acepta expresiones de tipo Intexp")
        
    def __repr__(self):
        return f"Product({self.expr1},{self.expr2})"

    def run(self, state:State): 
        return self.expr1.run(state) * self.expr2.run(state)

class Subs(IntExp): 
    def __init__(self, expr1:IntExp, expr2:IntExp):
        if (isinstance(expr1,IntExp) and isinstance(expr2, IntExp)): 
            self.expr1 = expr1
            self.expr2 = expr2
        else: 
            raise TypeError(f"Subs solo acepta expresiones de tipo Intexp")
        
    def __repr__(self):
        return f"Subs({self.expr1},{self.expr2})"
    
    def run(self, state:State): 
        return self.expr1.run(state) - self.expr2.run(state)     

class Div(IntExp): 
    def __init__(self, expr1:IntExp, expr2:IntExp):
        if (isinstance(expr1,IntExp) and isinstance(expr2, IntExp)): 
            self.expr1 = expr1
            self.expr2 = expr2
        else: 
            raise TypeError(f"Div solo acepta expresiones de tipo Intexp")
    
    def __repr__(self):
        return f"Div({self.expr1},{self.expr2})"
    
    def run(self, state:State): 
        return self.expr1.run(state) // self.expr2.run(state)  

class Mod(IntExp): 
    def __init__(self, expr1:IntExp, expr2:IntExp ):
        if (isinstance(expr1,IntExp) and isinstance(expr2, IntExp)): 
            self.expr1 = expr1
            self.expr2 = expr2
        else: 
            raise TypeError(f"Mod solo acepta expresiones de tipo Intexp")
    
    def __repr__(self):
        return f"Mod({self.expr1},{self.expr2})"
    
    def run(self, state:State): 
        return self.expr1.run(state) % self.expr2.run(state)  

class Neg(IntExp): 
    def __init__(self, expr1:IntExp):
        if isinstance(expr1, IntExp): 
            self.expr1 = expr1
        else: 
            raise TypeError("Neg sólo acepta expresiones tipo Intexp")
    def __repr__(self):
        return f"Neg({self.expr1})"
    
    def run(self, state:State): 
        return - self.expr1.run(state)
