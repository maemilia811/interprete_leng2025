
class State(dict): 
    def __init__(self, state:dict):
        super().__init__(state)
    
    def __repr__(self):
        return f"{super().__repr__()}"

class Output(tuple): 
    def __new__(cls, e, state: State):
        return super().__new__(cls, (e, state))  # pasás una tupla con los valores

    def __repr__(self):
        return f"{super().__repr__()}"
    
class Fail_type(tuple): 
    def __new__(cls, label: str, state: State):
        return super().__new__(cls, (label, state)) 

    def __repr__(self):
        return f"{super().__repr__()}"