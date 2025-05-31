#Main para testear casos de uso del programa 
from intexp import * 
from comm import Seq, Assign, Catch, Inp, Out, Skip, While, Newvar, Fail, If
from boolexp import *  


def main(): 
    # state = {}
    # st_modified = Seq(Assign(Var("x"), Nat(5)),
    #                  Assign(Var("x"), 
    #                         Product(Var("x"),
    #                             Nat(5)))).run(state) #tiene que recibir un estado para modificar eso

    # print(state)
    # st2 = Assign(Var("z"), Var("y")).run(state)
    # print(st_modified) 
    # print(st2)
    # print(NegBool(Fal()).run(state))
    # #print(Seq(Seq(Inp(Var("x")), Inp(Var("y"))), Out(Var("x"))).run(state))
    # print(Catch(Skip(), Assign(Var("x"),Nat(80000))).run(state))
    # print(While(MinThan(Var("x"),Nat(10)), 
    #             Assign (Var("x"),  Sum(Var("x"),
    #                                 Nat(1)))).run(state))
    
    state = State({})

    print("--------Imperativo Comun")
    print(Assign(Var("z"), Nat(32)).run(state))
    print(Skip().run(state))
    print(Seq(Assign(Var('x'),Nat(9)), Assign(Var('y'),Var('x'))).run(state))
    print(If(Equal(Nat(3),Nat(3)), Assign(Var("z"), Nat(64)), Assign(Var("z"), Nat(0))).run(state))
    print(While(MinThan(Var("x"),Nat(10)), 
                Assign (Var("x"),  Sum(Var("x"),
                                    Nat(1)))).run(state))
    print(Newvar(Var('x'), Sum(Var('x'), Nat(10)), Assign(Var('y'),Var('x'))).run(state))
    
    print("--------Fallas")
    print(Seq(Fail(), Assign(Var('x'),Nat(9))).run(state))
    print(Seq(Assign(Var('x'),Nat(9)),Fail()).run(state))
    #$print(Seq(While(Tr(), Skip()),Fail()).run(state))
    print(Seq(Fail(),While(Tr(), Skip())).run(state))
    print(Catch(Fail(), Assign(Var('f'),Nat(40))).run(state))
    print(Catch(Fail(), Fail()).run(state))
    state2 = {'x': 5}
    print(Newvar(Var('x'),Sum(Var('x'), Nat(5)), Seq(Skip(), Assign(Var('y'), Var('x')))).run(state2))
    print(Newvar(Var('x'),Sum(Var('x'), Nat(5)), Seq(Skip(), Fail())).run(state))
    print(Newvar(Var('x'),Sum(Var('x'), Nat(5)), Seq(Skip(), Assign(Var('y'), Var('x')))).run(state))


main()