from intexp import *

class Fail_type(tuple): 
    def __new__(cls, label: str, state: State):
        return super().__new__(cls, (label, state)) 

    def __repr__(self):
        return f"{super().__repr__()}"