from type import * 
#from output import * 
""" Función semántica para cada comando, 
run :: State -> Z """

class IntExp: 
    def __repr__(self):
        pass
    def run(): 
        pass

class Var(IntExp):     #corregida 
    def __init__(self, var:str):
        self.var = var

    def __repr__(self):
        return f"{self.var}"
    
    def run(self, state):
        if isinstance(state, State):
            if str(self.var) in state.keys():
                return state[str(self.var)]
            else: 
                return 0
        elif isinstance(state, Output):
            head, tail = state
            return self.run(tail)
        else:
            raise TypeError(f"Estado no reconocible: {state!r}")

class Nat(IntExp):    #corregida
    def __init__(self, number:int):
        if not isinstance(number, int):
            raise TypeError(f"Nat solo acepta enteros de tipo int, pero recibió {type(number).__name__}")
        self.n = number
    def __repr__(self):
        return f"Nat({self.n})"

    def run(self,state:State): 
        return self.n 

class Sum(IntExp): 
    def __init__(self, expr1:IntExp, expr2:IntExp): 
        if (not isinstance(expr1,IntExp) or not isinstance(expr2, IntExp)): 
                    raise TypeError(f"Sum solo acepta expresiones de tipo Intexp")
        self.sum1 = expr1
        self.sum2 = expr2
        
    def __repr__(self):
        return f"Sum({self.sum1},{self.sum2})"
    
    def run(self, state:State):         
        return self.sum1.run(state) + self.sum2.run(state) 
    
class Product (IntExp): 
    def __init__(self, expr1:IntExp, expr2:IntExp):
        self.expr1 = expr1
        self.expr2 = expr2
    
    def __repr__(self):
        return f"Product({self.expr1},{self.expr2})"

    def run(self, state:State): 
        return self.expr1.run(state) * self.expr2.run(state)


class Subs(IntExp): 
    def __init__(self, expr1:IntExp, expr2:IntExp ):
        self.expr1 = expr1
        self.expr2 = expr2
    
    def __repr__(self):
        return f"Subs({self.expr1},{self.expr2})"
    
    def run(self, state:State): 
        return self.expr1.run(state) - self.expr2.run(state)     


class Div(IntExp): 
    def __init__(self, expr1:IntExp, expr2:IntExp ):
        self.expr1 = expr1
        self.expr2 = expr2
    
    def __repr__(self):
        return f"Div({self.expr1},{self.expr2})"
    
    def run(self, state:State): 
        return self.expr1.run(state) // self.expr2.run(state)    #división entera

class Mod(IntExp): 
    def __init__(self, expr1:IntExp, expr2:IntExp ):
        self.expr1 = expr1
        self.expr2 = expr2
    
    def __repr__(self):
        return f"Mod({self.expr1},{self.expr2})"
    
    def run(self, state:State): 
        return self.expr1.run(state) % self.expr2.run(state)  

class Neg(IntExp): 
    def __init__(self, expr1:IntExp):
        self.expr1 = expr1
    
    def __repr__(self):
        return f"Neg({self.expr1})"
    
    def run(self, state:State): 
        return - self.expr1.run(state)
