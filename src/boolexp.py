from intexp import IntExp, Sum
class Boolexp: 
    pass 

class Equal(Boolexp):

    def __init__(self, expr1:IntExp, expr2: IntExp): 
        self.expr1 = expr1
        self.expr2 = expr2

    def __repr__(self):
        return f"Equal({self.expr1},{self.expr2})"
    
    def eval(self): 
        return self.expr1.run() == self.expr2.run() #ver acá y tener cuidado con los tipos de self.expr y cómo comparar las cosas 
    

def main(): 
    print(Equal(Sum(2,3),Sum(3,2)).eval())

main()