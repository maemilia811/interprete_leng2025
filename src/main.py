#Main para testear casos de uso del programa 
from intexp import * 
from comm import * 
from boolexp import * 


def main(): 
    state = {}
    
    st_modified = Seq(Assign(Var("x"), Nat(5)),
                     Assign(Var("x"), 
                            Product(Var("x"),
                                Nat(5)))).run(state) #tiene que recibir un estado para modificar eso

    print(state)
    st2 = Assign(Var("z"), Var("y")).run(state)
    print(st_modified) 
    print(st2)
    print(NegBool(Fal()).run(state))
    print(Seq(Seq(Inp(Var("x")), Inp(Var("y"))), Out(Var("x"))).run(state))
    print(Catch(Skip(), Assign(Var("x"),Nat(80000))).run(state))
    print(While(MinThan(Var("x"),Nat(10)), 
                Assign (Var("x"),  Sum(Var("x"),
                                    Nat(1)))).run(state))

main()