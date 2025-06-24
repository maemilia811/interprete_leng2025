from type import Output_type, Fail_type, State
from intexp import *
from boolexp import * 

"""
Función semántica de cada comando 
run :: State -> State 
"""

class Comm:
    def run(self,state):
        pass 

#SIMPLE COMMANDS 
class Skip(Comm):
    def __init__ (self):
        pass

    def __repr__(self):
        return "Skip()"
    
    def run(self,state:State):
        return state 
    
class Assign(Comm):  
    def __init__(self, var:Var, expr:IntExp):
        if isinstance(var,Var) and isinstance(expr,IntExp):
            self.var = var
            self.expr = expr
        else: 
            raise TypeError("Parámetros no validos para Assign")
    
    def __repr__(self):
        return f"Assign({self.var}, {self.expr})"
    
    def run(self, state:State):
        new_state = State(state.copy())
        new_state[str(self.var)] = self.expr.run(state) 
        return new_state
            
class Seq(Comm):
    def __init__(self,comm1:Comm, comm2:Comm): 
        if isinstance(comm1,Comm) and isinstance(comm2, Comm): 
            self.comm1 = comm1
            self.comm2 = comm2 
        else: 
            raise TypeError("Parámetros no validos para Seq")
    
    def __repr__(self):
        return f"Seq({self.comm1}, {self.comm2})"
    
    def _star(self, comm:Comm, x): 
        if isinstance(x,Fail_type): 
            return x 
        elif isinstance(x,Output_type): 
            return Output_type(x[0], self._star(comm,x[1]))  
        else: 
            return comm.run(x)
        
    def run(self, state:State):
        return self._star(self.comm2, self.comm1.run(state))

class If(Comm):  
    def __init__(self,condition,comm1:Comm,comm2:Comm):
        if isinstance(condition, Boolexp) and isinstance(comm1,Comm) and isinstance(comm2, Comm):
            self.guard = condition
            self.comm1 = comm1
            self.comm2 = comm2 
        else: 
            raise TypeError("Parámetros no validos para If")

    def __repr__(self): 
        return f"If {self.guard} then {self.comm1} else {self.comm2}"
    
    def run(self, state:State): 
        if self.guard.run(state):    
            return self.comm1.run(state)
        else:
            return self.comm2.run(state)

class While(Comm):  
    def __init__(self, condition:Boolexp, comm:Comm): 
        if isinstance(condition, Boolexp) and isinstance(comm,Comm):
            self.comm = comm
            self.guard = condition
        else: 
            raise TypeError(f"Parámetros no validos para While{type(condition), type(comm)}")
    
    def __repr__(self):
        return f"While {self.guard} do {self.comm}"
    
    def _detected_failure(self, state): 
        if isinstance(state,State): 
            return False
        elif isinstance(state,Output_type): 
            return self._detected_failure(state[1])
        elif isinstance(state, Fail_type):
            return True 
        
    def _star(self, comm:Comm, x): 
        if isinstance(x,Fail_type): 
            return x 
        elif isinstance(x,Output_type): 
            return Output_type(x[0], self._star(comm,x[1]))  
        else: 
            return comm.run(x)

    def run(self, state:State): 
        st_modified = State(state.copy())
        while self.guard.run(st_modified): 
            st_modified = self._star(self.comm, st_modified)   
            if self._detected_failure(st_modified):
                return st_modified
        return st_modified

class Newvar(Comm):
    def __init__(self, var, expr:IntExp, comm:Comm): 
        if isinstance(var,Var) and isinstance(expr,IntExp) and isinstance(comm,Comm):
            self.var = var 
            self.expr = expr
            self.comm = comm
        else:
            raise TypeError("Parámetros no validos para Newvar")

    def __repr__(self):
        return f"Newvar {self.var}:= {self.expr} in {self.comm}"
    
    def _delete_var(self, var, state): 
        if isinstance(state, Output_type): 
            return Output_type(state[0], self._delete_var(var,state[1]))
        elif isinstance(state, Fail_type): 
            return Fail_type(state[0], self._delete_var(var,state[1]))
        else: 
            del state[str(var)]
            return state
    
    def _get_old_value(self, var, state): 
        if isinstance(state, Output_type) or isinstance(state,Fail_type): 
            return self._get_old_value(var,state[1])
        else: 
            if str(var) in state.keys():
                return state[str(var)]
            else:
                return {}

    def _daga(self, comm:Comm, x): 
        if isinstance(x,Fail_type): 
            return Fail_type(x[0], comm.run(x[1])) 
        elif isinstance(x, Output_type): 
            return Output_type(x[0], self._daga(comm, x[1]))
        else: 
            return comm.run(x)
    
    def run(self, state:State): 
        old_value = self._get_old_value(self.var, state)
        if old_value != {}: 
            st_modified = self.comm.run(Assign(self.var, self.expr).run(state))
            return self._daga(Assign(self.var, Num(old_value)), st_modified)
        else: 
            st_modified = self.comm.run(Assign(self.var, self.expr).run(state))
            return self._delete_var(self.var, st_modified)
        
#FAILURES 
class Fail(Comm):      
    def __init__(self):
        self.fail = 'Fail'
    
    def __repr__(self):
        return f"Fail"
    
    def run(self, state:State):
        if isinstance(state,Fail_type): 
            return state
        else: 
            return Fail_type(self.fail,state)   
              
class Catch(Comm):  
    def __init__(self, comm1:Comm, comm2:Comm):
        if isinstance(comm1, Comm) and isinstance(comm2, Comm):   
            self.comm1 = comm1
            self.comm2 = comm2 
        else: 
            raise TypeError("Parámetros no validos para Catch")
        
    def __repr__(self):
        return f"Catch {self.comm1} with {self.comm2}"
    
    def  _ext_catch(self, comm:Comm, x): 
        if isinstance(x,Fail_type): 
            return comm.run(x[1])
        elif isinstance(x,Output_type):  
            return Output_type(x[0], self._ext_catch(comm,x[1]))  
        else: 
            return x
    
    def run(self, state:State):
        return self._ext_catch(self.comm2, self.comm1.run(state))

#IO
class Out(Comm): 
    def __init__(self, expr:IntExp): 
        if isinstance(expr,IntExp): 
            self.expr = expr
        else: 
            raise TypeError("Parámetros no validos para Out")
        
    def __repr__(self):
        return f"Out({self.expr})"
    
    def run(self, state:State): 
        return Output_type(self.expr.run(state), state)

class Inp(Comm):
    def __init__(self, var:Var): 
        if isinstance(var,Var): 
            self.var = var
        else: 
            raise TypeError("Parámetros no validos para Inp")

    def _update_recursive(self, state, value): 
        if isinstance(state, State):
            new_state = State(state.copy())
            new_state[str(self.var)] = value
            return new_state
        elif isinstance(state, Output_type):
            head, tail = state
            return Output_type(head, self._update_recursive(tail, value))
        else: 
            raise TypeError(f"Estado no reconocible: {state!r}")

    def run(self, state):
        while True:
            num = input("Ingrese número entero\n")
            try:
                value = int(num)
                return self._update_recursive(state, value)
            except ValueError:
                print(f"«{num}» no es un entero válido. Intenta de nuevo\n")

