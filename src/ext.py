from state import * 
from comm import Comm, Fail

def star(comm:Comm, x:State): 
    print("aca", comm, x)
    if isinstance(x,Fail): 
        return x 
    else: 
        return comm.run(x)


# def cruz(f, x):
#     if (isinstance(x,Fail)): 
#         return f(x) 
#     else: 
#         return x
    
# def daga(f, x): 
#     if (isinstance(x, Fail)): 
#         (Fail, f x )
#     else:  
#         return f x 
