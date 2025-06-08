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
    print(Assign(Var("z"), Nat(32)), Assign(Var("z"), Nat(32)).run(state))
    print(Skip(),Skip().run(state))
    print(Seq(Assign(Var('x'),Nat(9)), Assign(Var('y'),Var('x'))), Seq(Assign(Var('x'),Nat(9)), Assign(Var('y'),Var('x'))).run(state))
    print(If(Equal(Nat(3),Nat(3)), Assign(Var("z"), Nat(64)), Assign(Var("z"), Nat(0))), If(Equal(Nat(3),Nat(3)), Assign(Var("z"), Nat(64)), Assign(Var("z"), Nat(0))).run(state))
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
   
    print("--------Newvar")
    state2 = State({'x': 5})
    print(Newvar(Var('x'),Sum(Var('x'), Nat(5)), Seq(Skip(), Assign(Var('y'), Var('x')))).run(state2))
    print(Newvar(Var('x'),Sum(Var('x'), Nat(5)), Seq(Skip(), Fail())).run(state))  
    print(Newvar(Var('x'),Sum(Var('x'), Nat(5)), Seq(Skip(), Assign(Var('y'), Var('x')))).run(state))


    print("--------Output")
    print(Seq(Out(Var("x")), Fail()).run(state2))
    print(Seq(Fail(), Out(Var("x"))).run(state2))
    print(Seq(Assign(Var("x"), Nat(20)), Out(Var("x"))).run(state))
    print(Seq(Out(Var("x")),Assign(Var("x"), Nat(20))).run(state))

    print("--------Input")
    print(Seq(Out(Var("x")), Inp(Var("x"))).run(state))
    
    #CORREGIR ESTE
    print(Seq(Out(Var("x")), Seq(Assign(Var("y"), Nat(9)), Seq(Fail(), Inp(Var("z"))))).run(state))
    
    #print(Assign(Var('d'), Nat(-0.3)).run(state))
    #print(Sum(Nat(00), Tr()).run(state))

    #not valid program
    # print(Newvar(Var('x'), Inp(Var('x')), Out(Var('x'))).run(state))

    #print(While(MinThan(Var('x'),Nat(10)), Seq(Seq(Inp(Var('y')), Out(Var('y'))), Assign(Var('x'),Sum(Var('x'), Nat(1))))).run(state))
    #print(Seq(Seq(Inp(Var('x')), Out(Var('x'))), Seq(Seq(Inp(Var('x')), Out(Var('x'))),Seq(Inp(Var('x')), Out(Var('x'))))).run(state))
    # print(Seq(Out(Var('x')),Newvar(Var('y'), Nat(8),Out(Var('y')))).run(state))
    
    # #chequear bien si ertorna los outpout en orden correctos
    # print(While(MinThan(Var('x'),Nat(10)), 
    #       Seq(Seq(Seq(Out(Var('x')), Newvar(Var('y'), Nat(811), Out(Var('y')))), Out(Var('y'))), Assign(Var('x'),Sum(Var('x'), Nat(1))))).run(state))

    print(Assign(Var('y'), Tr()).run(state))

main()