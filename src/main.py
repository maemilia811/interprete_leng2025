from intexp import * 
from comm import Seq, Assign, Catch, Inp, Out, Skip, While, Newvar, Fail, If
from boolexp import *  

def main(): 
    """Interfaz para probar propios programas
        Debajo se muestran ejemplos:"""

    state = State({})   
    print("--------Imperativo Comun")
    print(Seq(Assign(Var('x'),Num(9)), Assign(Var('y'),Var('x'))), Seq(Assign(Var('x'),Num(9)), Assign(Var('y'),Var('x'))).run(state))
    print(If(Equal(Num(3),Num(3)), Assign(Var("z"), Num(64)), Assign(Var("z"), Num(0))), If(Equal(Num(3),Num(3)), Assign(Var("z"), Num(64)), Assign(Var("z"), Num(0))).run(state))
    print(While(LessThan(Var("x"),Num(10)), 
                Assign (Var("x"),  Sum(Var("x"),
                                    Num(1)))).run(state))
    print(Newvar(Var('x'), Sum(Var('x'), Num(10)), Assign(Var('y'),Var('x'))).run(state))
    
    print("--------Fallas")
    print(Seq(Fail(), Assign(Var('x'),Num(9))).run(state))
    print(Seq(Assign(Var('x'),Num(9)),Fail()).run(state))
    print(Seq(Fail(),While(Tr(), Skip())).run(state))
    print(Catch(Fail(), Assign(Var('f'),Num(40))).run(state))
    print(Catch(Fail(), Fail()).run(state))
    print(Catch(Seq(Out(Var('x')), Fail()), Seq(Assign(Var('f'),Num(40)), Out(Var('f')))).run(state))
   
    print("--------Newvar")
    state2 = State({'x': 5})
    print(Newvar(Var('x'),Sum(Var('x'), Num(5)), Seq(Skip(), Assign(Var('y'), Var('x')))).run(state2))
    print(Newvar(Var('x'),Sum(Var('x'), Num(5)), Seq(Skip(), Fail())).run(state))  
    print(Newvar(Var('x'),Sum(Var('x'), Num(5)), Seq(Skip(), Assign(Var('y'), Var('x')))).run(state))


    print("--------Output")
    print(Seq(Out(Var("x")), Fail()).run(state2))
    print(Seq(Fail(), Out(Var("x"))).run(state2))
    print(Seq(Assign(Var("x"), Num(20)), Out(Var("x"))).run(state))
    print(Seq(Out(Var("x")),Assign(Var("x"), Num(20))).run(state))

    print("--------Input")
    print(Seq(Out(Var("x")), Inp(Var("x"))).run(state))
    print(Seq(Out(Var("x")), Seq(Assign(Var("y"), Num(9)), Seq(Fail(), Inp(Var("z"))))).run(state))
   

    print("--------Programas")
    print(While(LessThan(Var('x'),Num(10)), Seq(Seq(Inp(Var('y')), Out(Var('y'))), Assign(Var('x'),Sum(Var('x'), Num(1))))).run(state))
    print(Seq(Seq(Inp(Var('x')), Out(Var('x'))), Seq(Seq(Inp(Var('x')), Out(Var('x'))),Seq(Inp(Var('x')), Out(Var('x'))))).run(state))
    print(Seq(Out(Var('x')),Newvar(Var('y'), Num(8),Out(Var('y')))).run(state))
    print(Seq(Out(Var('x')), Newvar(Var('x'), Num(8),Out(Var('x')))).run(state))
    print(While(LessThan(Var('x'), Num(2)), 
                If(Equal(Var('x'), Num(0)),   
                    Seq(Out(Var('x')), Assign(Var('x'),Sum(Var('x'), Num(1)))), 
                Seq(Assign(Var('x'),Sum(Var('x'), Num(1))), 
                    Assign(Var('x'),Sum(Var('x'), Num(1)))))).run(state))
    
    print(While(LessThan(Var('x'), Num(2)), 
                    If(Equal(Var('x'), Num(0)),   
                        Seq(Out(Var('x')), Assign(Var('x'),Sum(Var('x'), Num(1)))), 
                    Seq(Newvar(Var('x'), Num(10), Out(Var('x'))), 
                        Assign(Var('x'),Sum(Var('x'), Num(1)))))).run(state))
    
    print(Seq(Fail(), Fail()).run(state))

    print(Newvar(Var('x'), Num(5), 
    Seq(
        Out(Var('x')),
        Seq(
        Assign(Var('x'), Num(10)),
        Out(Var('x')))
    )).run(state))

    print(Seq(
    Assign(Var('x'), Num(0)),
    While(
        LessThan(Var('x'), Num(5)),
        Seq(
            Out(Var('x')),
            Assign(Var('x'), Sum(Var('x'), Num(1)))
        )
    )
    ).run(state))

    print(Seq(
    Assign(Var('x'), Num(10)),
    Seq(Assign(Var('y'), Num(5)),
    If(
        Conj(
            GreaterThan(Var('x'), Num(5)),
            LessThan(Var('y'), Num(10))
        ),
        Out(Sum(Var('x'), Var('y'))),
        Out(Subs(Var('x'), Var('y')))
        ))
    ).run(state))
    
    print(Seq(
    Assign(Var('x'), Num(5)),
    Catch(
        Seq(
            Fail(),
            Out(Var('x'))
        ),
        Out(Num(42))
    )
    ).run(state))
    print(While(Tr(),Fail()).run(state))

    print(Catch(
            Seq(
                Assign(Var('contador'), Num(4)),
                While(
                    GreaterThan(Var('contador'), Num(0)),
                    Seq(
                        Out(Var('contador')),
                        If(
                            Equal(Var('contador'), Num(2)),
                            Fail(),
                            Assign(Var('contador'), Subs(Var('contador'), Num(1)))
                        )
                    )
                )
            ),
            Out(Num(999)) 
    ).run(state))

    print(Seq(
            Assign(Var('x'), Num(100)), 
            Catch(
                Newvar(
                    Var('x'), 
                    Num(5),
                    Seq(
                        Out(Var('x')), 
                        Fail()         
                    )
                ),
                Seq(
                    Out(Num(888)), 
                    Out(Var('x'))  
                )
            )
        ).run(state))

main()