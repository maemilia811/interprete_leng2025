from state import *  
from intexp import *
from boolexp import * 
from output import * 
from fail import *

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
        return State(new_state)
            
class Seq(Comm): 
    def __init__(self,comm1:Comm, comm2:Comm): 
        self.comm1 = comm1
        self.comm2 = comm2 
    
    def __repr__(self):
        return f"Seq({self.comm1}, {self.comm2})"
    
    # def run(self, state:State): 
    #     state1 = self.comm1.run(state) 
    #     return self.comm2.run(state1)
    def run(self, state:State):
        return star(self.comm2, self.comm1.run(state))

class If(Comm):
    def __init__(self,b,comm1:Comm,comm2:Comm):
        self.guard = b 
        self.comm1 = comm1
        self.comm2 = comm2 

    def __repr__(self): 
        return f"If {self.guard} then {self.comm1} else {self.comm2}"
    
    def run(self, state:State): 
        if (self.guard.run(state)): 
            return self.comm1.run(state)
        else:
            return self.comm2.run(state)

class While(Comm):   #adaptar con la extensión
    def __init__(self, b:Boolexp, comm:Comm): 
        self.comm = comm
        self.guard = b
    
    def __repr__(self):
        return f"While {self.guard} do {self.comm}"
    
    def run(self, state:State): 
        #Ver si la variable está definida en el conjunto de estados
        st_modified = State(state.copy())
        while self.guard.run(st_modified): 
            st_modified = self.comm.run(st_modified)        
        return st_modified

class Newvar(Comm):
    def __init__(self, var, expr:IntExp, comm:Comm): 
        self.var = var 
        self.expr = expr
        self.comm = comm
        self.local = Assign(var, expr)
    
    def __repr__(self):
        return f"Newvar {self.local} in {self.comm}"

    def run(self, state:State): 
        if (str(self.var) in state.keys()): 
            old_state = Nat(state[str(self.var)])
            st_modified = self.comm.run(Assign(self.var, self.expr).run(state))
            return ext_newvar(Assign(self.var, old_state), st_modified)
        else: 
            st_modified = self.comm.run(Assign(self.var, self.expr).run(state))
            if isinstance(st_modified,Fail_type):
                del st_modified[1][str(self.var)]
                return st_modified
            elif isinstance(st_modified, Output):
                del st_modified[1][str(self.var)]
                return st_modified
            else:
                del st_modified[str(self.var)] 
                return st_modified
                
            
        

#FAILURES 
class Fail(Comm): 
    def __init__(self):
        self.fail = 'Fail'
    
    def __repr__(self):
        return f"Fail"
    
    def run(self, state:State):
        return Fail_type(self.fail,state)   
              

class Catch(Comm): 
    def __init__(self, comm1:Comm, comm2:Comm):
        self.comm1 = comm1
        self.comm2 = comm2 
    def __repr__(self):
        return f"Catch {self.comm1} with {self.comm2}"
    def run(self, state:State):
        return ext_catch(self.comm2, self.comm1.run(state))

#IO
class Out(Comm): 
    def __init__(self, expr:IntExp): 
        self.expr = expr
    
    def __repr__(self):
        return f"Out({self.expr})"
    
    def run(self, state:State): 
        return Output(self.expr.run(state), state)

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
            
#EXTENSIONES           
#--- (_)*
def star(comm:Comm, x): 
    if isinstance(x,Fail_type): #si x fuera un output, entra por acá y se hace lio 
        return x 
    elif isinstance(x,Output): 
        return Output(x[0], comm.run(x[1]))
    else: 
        return comm.run(x)

#--- (_)+
def  ext_catch(comm:Comm, x): 
    if isinstance(x,Fail_type): #si x fuera un output, entra por acá y se hace lio 
        return comm.run(x[1])
    elif isinstance(x,Output): 
        return Output(x[0], comm.run(x[1]))
    else: 
        return x
    
def ext_newvar(comm:Comm, x):  
    if isinstance(x,Fail_type): 
        return Fail_type(x[0],comm.run(x[1]))
    elif isinstance(x,Output): 
        return Output(x[0], comm.run(x[1]))
    else: 
        return comm.run(x)
