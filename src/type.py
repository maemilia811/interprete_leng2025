
class State(dict): 
    def __init__(self, state:dict):
        if isinstance(state,dict):
            super().__init__(state)
        else: 
            raise TypeError("Parámetros no validos para State")
    
    def __repr__(self):
        return f"{super().__repr__()}"

class Output_type(tuple): 
    def __new__(cls, e, state: State):
        return super().__new__(cls, (e, state))  
    def __repr__(self):
        return f"{super().__repr__()}"
    
class Fail_type(tuple): 
    def __new__(cls, label: str, state: State):
        return super().__new__(cls, (label, state)) 

    def __repr__(self):
        return f"{super().__repr__()}"