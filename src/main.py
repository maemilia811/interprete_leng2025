#Main para testear casos de uso del programa 

from intexp import * 
from comm import * 
def main(): 
    state = {}
    
    st_modified = Seq(Assign(Var("x"), Nat(1)),
                     Assign(Var("x"), 
                            Sum(Var("x"),
                                Nat(2)))).run(state) #tiene que recibir un estado para modificar eso

    print(state)
    st2 = Assign(Var("z"), Var("y")).run(state)
    print(st_modified) 
    print(st2)


main()