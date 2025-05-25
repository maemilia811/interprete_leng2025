from state import *  
from intexp import *
from boolexp import * 
"""
Función semántica de cada comando 
run :: State -> State 
"""

class Comm:
    def run():
        pass 


#SIMPLE COMMANDS 
class Skip(Comm):
    def __init__ (self):
        pass

    def __repr__():
        return "Skip()"
    
    def run(self,state:State):
        return state 
    
class Assign(Comm):
    def __init__(self, var:Var, expr:IntExp):
        self.var = var
        self.expr = expr
    
    def __repr__(self):
        return f"Assign({self.var}, {self.expr})"
    
    def run(self, state:State):
        new_state = state.copy()
        new_state[str(self.var)] = self.expr.run(state)
        return new_state
            
class Seq(Comm): 
    def __init__(self,comm1:Comm, comm2:Comm): 
        self.comm1 = comm1
        self.comm2 = comm2 
    
    def __repr__(self):
        return f"Seq({self.comm1}, {self.comm2})"
    
    def run(self, state:State): 
        state1 = self.comm1.run(state) 
        return self.comm2.run(state1)

class If(Comm):
    def __init__(self,b,comm1:Comm,comm2:Comm):
        self.guard = b 
        self.comm1 = comm1
        self.comm2 = comm2 

    def __repr__(self): 
        return f"If {self.guard} then {self.comm1} else {self.comm2}"
    
    def run(self, state:State): 
        if (self.guard): 
            return self.comm1.run(state)
        else:
            return self.comm2.run(state)

class While(Comm): 
    def __init__(self, b:Boolexp, comm:Comm): 
        self.comm = comm
        self.guard = b
    
    def __repr__(self):
        return f"While {self.guard} do {self.comm}"
    
    def run(self, state:State): 
        #Ver si la variable está definida en el conjunto de estados
        st_modified = state.copy()
        while self.guard.run(st_modified): 
            st_modified = self.comm.run(st_modified)
        
        return st_modified

class Newvar(Comm):
    def __init__(self, var, expr, comm:Comm): 
        self.var = var 
        self.expr = expr
        self.comm = comm
        self.local = Assign(var, expr)
    
    def __repr__(self):
        return f"Newvar {self.local} in {self.comm}"

    def run(self, state:State): 
        if (self.var in state.keys()): 
            old_state = state[str(self.var)]
            st_modified = Assign(self.var, self.expr).run(state)
            st_modified = self.comm.run(st_modified)
            return Assign(self.var, old_state).run(st_modified)
        else: 
            old_state = {}
            state[str(self.var)] = {}
            st_modified = Assign(self.var, self.expr).run(state)
            st_modified = self.comm.run(st_modified)
            st_modified = Assign(self.var, old_state).run(st_modified)
            del state[str(self.var)]
            return st_modified


#FAILURES 
class Fail(Comm): 
    def __init__(self):
        self.fail = "Fail"
    
    def __repr__(self):
        return f"Fail"
    
    def run(self, state:State):
        return ("Fail", state)             

class Catch(Comm): 
    def __init__(self, comm1:Comm, comm2:Comm):
        self.comm1 = comm1
        self.comm2 = comm2 
    def __repr__(self):
        return f"Catch {self.comm1} with {self.comm2}"
    def run(self, state:State):
        st_modified = self.comm1.run(state)
        
        if (isinstance(st_modified,tuple) ): #Caso que retorne tupla, adaptar para el output  
            return self.comm2.run(st_modified[1])
        else: 
            return st_modified

#IO
class Out(Comm): 
    def __init__(self, expr:IntExp): 
        self.expr = expr
    
    def __repr__(self):
        return f"Out({self.expr})"
    
    def run(self, state:State): 
        return (self.expr.run(state), state)

class Inp(Comm): 
    def __init__(self, var:Var): 
        self.var = var
    
    def __repr__(self):
        return f"Inp({self.var})"
    
    def run(self, state:State): 
        while True:
            num = input("Ingrese número entero\n")
            try:
                value = int(num)
                state[str(self.var)] = value
                return state 
            except ValueError:
                print(f"«{num}» no es un entero válido. Intenta de nuevo\n")
            

