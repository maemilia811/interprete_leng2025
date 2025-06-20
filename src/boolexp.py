from intexp import *
from type import *

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
        if isinstance(expr1,IntExp) and isinstance(expr2, IntExp): 
            self.expr1 = expr1
            self.expr2 = expr2
        else: 
            raise TypeError("Expresiones mal tipadas")

    def __repr__(self):
        return f"Equal({self.expr1},{self.expr2})"
    
    def run(self, state:State):
        if(self.expr1.run(state) == self.expr2.run(state)):
            return Tr().run(state)
        else:
            return Fal().run(state)
    
# < 
class LessThan(Boolexp): 
    def __init__(self, expr1:IntExp, expr2: IntExp): 
        if isinstance(expr1,IntExp) and isinstance(expr2, IntExp): 
            self.expr1 = expr1
            self.expr2 = expr2
        else: 
            raise TypeError("Expresiones mal tipadas")

    def __repr__(self):
        return f"LessThan({self.expr1},{self.expr2})"
    
    def run(self, state:State): 
        if self.expr1.run(state) < self.expr2.run(state): 
            return Tr().run(state)
        else: 
            return Fal().run(state)
# > 
class GreaterThan(Boolexp): 
    def __init__(self, expr1:IntExp, expr2: IntExp): 
        if isinstance(expr1,IntExp) and isinstance(expr2, IntExp): 
            self.expr1 = expr1
            self.expr2 = expr2
        else: 
            raise TypeError("Expresiones mal tipadas")
        
    def __repr__(self):
        return f"MaxThan({self.expr1},{self.expr2})"
    
    def run(self, state:State): 
        if self.expr1.run(state) > self.expr2.run(state): 
            return Tr().run(state)
        else: 
            return Fal().run(state)

# =< 
class LessEqThan(Boolexp): 
    def __init__(self, expr1:IntExp, expr2: IntExp): 
        if isinstance(expr1,IntExp) and isinstance(expr2, IntExp): 
            self.expr1 = expr1
            self.expr2 = expr2
        else: 
            raise TypeError("Expresiones mal tipadas")

    def __repr__(self):
        return f"MaxThan({self.expr1},{self.expr2})"
    
    def run(self, state:State): 
        if self.expr1.run(state) <= self.expr2.run(state): 
            return Tr().run(state)
        else: 
            return Fal().run(state)

# >= 
class GtEqThan(Boolexp): 
    def __init__(self, expr1:IntExp, expr2: IntExp): 
        if isinstance(expr1,IntExp) and isinstance(expr2, IntExp): 
            self.expr1 = expr1
            self.expr2 = expr2
        else: 
            raise TypeError("Expresiones mal tipadas")
        
    def __repr__(self):
        return f"MaxThan({self.expr1},{self.expr2})"
    
    def run(self, state:State): 
        if self.expr1.run(state) >= self.expr2.run(state): 
            return Tr().run(state)
        else: 
            return Fal().run(state)

#¬
class NegBool(Boolexp): 
    def __init__(self, expr1:Boolexp): 
        if isinstance(expr1, Boolexp): 
            self.expr1 = expr1
        else: 
            raise TypeError("Expresión mal tipada")

    def __repr__(self):
        return f"NegBool({self.expr1})"
    
    def run(self, state:State): 
        if self.expr1.run(state): 
            return Fal().run(state)
        else: 
            return Tr().run(state)
    
class Conj(Boolexp): 
    def __init__(self, expr1:Boolexp, expr2: Boolexp): 
        if isinstance(expr1,Boolexp) and isinstance(expr2, Boolexp): 
            self.expr1 = expr1
            self.expr2 = expr2
        else: 
            raise TypeError("Expresión mal tipada")

    def __repr__(self):
        return f"Conj({self.expr1}, {self.expr2})"
    
    def run(self, state:State): 
        if self.expr1.run(state) and self.expr2.run(state): 
            return Tr().run(state)
        else: 
            return Fal().run(state)

class Disj(Boolexp): 
    def __init__(self, expr1:Boolexp, expr2: Boolexp): 
        if isinstance(expr1,Boolexp) and isinstance(expr2, Boolexp): 
            self.expr1 = expr1
            self.expr2 = expr2
        else: 
            raise TypeError("Expresión mal tipada")
        
    def __repr__(self):
        return f"Disj({self.expr1}, {self.expr2})"
    
    def run(self, state:State): 
        if self.expr1.run(state) or self.expr2.run(state): 
            return Tr().run(state)
        else: 
            return Fal().run(state)
