from intexp import *

class Output(tuple): 
    def __new__(cls, e: IntExp, state: State):
        return super().__new__(cls, (e, state))  # pasás una tupla con los valores

    def __repr__(self):
        return f"{super().__repr__()}"