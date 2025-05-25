from intexp import *
from state import * 

"""
Función semántica run

run :: State -> {True, False}
"""
class Boolexp: 
    def __init__(self):
        pass
    def run(): 
        pass  

class Tr(Boolexp): 
    def __init__(self):
        self.true = True
    
    def __repr__(self):
        return f"True"
    
    def run(self, state:State): 
        return self.true

class Fal(Boolexp): 
    def __init__(self):
        self.false = False
    
    def __repr__(self):
        return f"False"
    
    def run(self, state:State): 
        return self.false
class Equal(Boolexp):
    def __init__(self, expr1:IntExp, expr2: IntExp): 
        self.expr1 = expr1
        self.expr2 = expr2

    def __repr__(self):
        return f"Equal({self.expr1},{self.expr2})"
    
    def run(self, state:State): 
        return self.expr1.run(state) == self.expr2.run(state) 
    
# < 
class MinThan(Boolexp): 
    def __init__(self, expr1:IntExp, expr2: IntExp): 
        self.expr1 = expr1
        self.expr2 = expr2

    def __repr__(self):
        return f"MinThan({self.expr1},{self.expr2})"
    
    def run(self, state:State): 
        return self.expr1.run(state) < self.expr2.run(state) 

# > 
class MaxThan(Boolexp): 
    def __init__(self, expr1:IntExp, expr2: IntExp): 
        self.expr1 = expr1
        self.expr2 = expr2

    def __repr__(self):
        return f"MaxThan({self.expr1},{self.expr2})"
    
    def run(self, state:State): 
        return self.expr1.run(state) > self.expr2.run(state) 

# =< 
class MinEqThan(Boolexp): 
    def __init__(self, expr1:IntExp, expr2: IntExp): 
        self.expr1 = expr1
        self.expr2 = expr2

    def __repr__(self):
        return f"MaxThan({self.expr1},{self.expr2})"
    
    def run(self, state:State): 
        return self.expr1.run(state) <= self.expr2.run(state) 

# >= 
class MaxEqThan(Boolexp): 
    def __init__(self, expr1:IntExp, expr2: IntExp): 
        self.expr1 = expr1
        self.expr2 = expr2

    def __repr__(self):
        return f"MaxThan({self.expr1},{self.expr2})"
    
    def run(self, state:State): 
        return self.expr1.run(state) >= self.expr2.run(state) 


class NegBool(Boolexp): 
    def __init__(self, expr1:Boolexp): 
        self.expr1 = expr1

    def __repr__(self):
        return f"NegBool({self.expr1})"
    
    def run(self, state:State): 
        return not self.expr1.run(state) 

class Conj(Boolexp): 
    def __init__(self, expr1:Boolexp, expr2: Boolexp): 
        self.expr1 = expr1
        self.expr2 = expr2

    def __repr__(self):
        return f"Conj({self.expr1}, {self.expr2})"
    
    def run(self, state:State): 
        return  self.expr1.run(state) and self.expr2.run(state)

class Disj(Boolexp): 
    def __init__(self, expr1:Boolexp, expr2: Boolexp): 
        self.expr1 = expr1
        self.expr2 = expr2

    def __repr__(self):
        return f"Disj({self.expr1}, {self.expr2})"
    
    def run(self, state:State): 
        return  self.expr1.run(state) or self.expr2.run(state)
