# Categorias sintácticas
# Constructor para escribir mejor el lenguaje 
# Funcion de evaluacion 
# 

from state import *  
from intexp import *
"""Quiero evaluar un programa, entonces le voy a pasar el input el texto que quiero evaluar 
En este caso, no voy a darle input y leerlo sino que ya le paso como input el arbol o el programa bien escrito
y voy a ponerle 

AGREGAR TYPE HINITNG 

"""

class Comm:
    def run():
        pass 

class Skip(Comm):
    def __init__ (self):
        pass

    def __repr__():
        return "Skip()"
    
    def run(self,state:State):
        return state 
    

#Assing x:= intexp. Dado un estado, retorna un nuevo estado con la variable x modificada 
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
    def __init__(self,b,comm1:Comm,comm2:Comm, state:State):
        self.guard = b 
        self.comm1 = comm1
        self.comm2 = comm2 
        self.state = state

    def __repr__(self): 
        return f"If {self.guard} then {self.comm1} else {self.comm2}"
    
    def run(self): 
        if (self.guard): 
            self.comm1.run()
        else:
            self.comm2.run()

class While(Comm): 
    def __init__(self, b, comm:Comm, state:State): 
        self.comm = comm
        self.guard = b 
        self.state = state 
    
    def __repr__(self):
        return f"While {self.guard} do {self.comm}"
    
    def run(self): 
        #Ver si la variable está definida en el conjunto de estados
        while self.guard:    #DEFINIR INTEXP 
            self.comm.run()

class Newvar(Comm):
    def __init__(self, var, expr, comm:Comm, state:State): 
        self.var = var 
        self.expr = expr
        self.comm = comm
        self.local = Assign(var, expr)
        self.state = state 
    
    def __repr__(self):
        return f"Newvar {print(self.local)} in {print(self.comm)}" #modficiar acá

    def run(self): 
        if (self.var in state.keys()): 
            old_state = state[self.var]
            Assign(self.var, self.expr)
            self.comm.run()
            Assign(self.var, old_state)
        else: 
            old_state = {}
            state[self.var] = {}
            Assign(self.var, self.expr)
            self.comm.run()
            Assign(self.var, old_state)
            del state[self.var]




