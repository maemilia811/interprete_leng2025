class IntExp: 
    pass


class Var (IntExp): 
    def __init__(self, var):
        self.var = var


class Sum(IntExp): 
    def __init__(self,sum1, sum2):
        self.sum1 = sum1
        self.sum2 = sum2

    def __repr__(self):
        return f"{self.sum1} + {self.sum2}"
    
    def run(self): 
        return self.sum1 + self.sum2


#Es necesario definir estas cosas? 