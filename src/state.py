class State(dict): 
    def __init__(self, state:dict):
        super().__init__(state)
    
    def __repr__(self):
        return f"{super().__repr__()}"
