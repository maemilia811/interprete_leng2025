import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from comm import *
from intexp import *
from boolexp import *
from type import *
class TestIntexpr(unittest.TestCase): 
    def test_sum(self): 
        state = State({'x':8})
        self.assertEqual(Sum(Var('x'),Num(10)).run(state),18)
    
    def test_subs(self): 
        state = State({'x':8})
        self.assertEqual(Subs(Var('x'),Num(10)).run(state),-2)

    def test_product(self): 
        state = State({'x':8})
        self.assertEqual(Product(Var('x'),Num(10)).run(state),80)

    def test_div(self):
        state = State({'x':8})
        self.assertEqual(Div(Var('x'),Num(3)).run(state),2)
    
    def test_mod(self): 
        state = State({'x':8})
        self.assertEqual(Mod(Var('x'),Num(5)).run(state),3)

class TestBoolexpr(unittest.TestCase): 
    def test_equal(self): 
        state = State({'x':10})
        self.assertEqual(Equal(Num(10),Var('x')).run(state),True)

    def test_LessThan(self): 
        state = State({'x':10}) 
        self.assertEqual(LessThan(Num(5),Var('x')).run(state),True)


    def test_GreaterThan(self):
        state = State({'x':2}) 
        self.assertEqual(GreaterThan(Num(5),Var('x')).run(state),Tr().run(state)) 

    def test_LessEqThan(self): 
        state = State({'x':2}) 
        self.assertEqual(LessEqThan(Num(2),Var('x')).run(state),Tr().run(state)) 
   
    def test_GtEqThan(self): 
        state = State({'x':2}) 
        self.assertEqual(GtEqThan(Num(3),Var('x')).run(state),Tr().run(state)) 
    
    def test_conj(self): 
        state = State({'x':2}) 
        self.assertEqual(Conj(GreaterThan(Num(5),Num(3)),
                              Equal(Var('x'),Num(2))).run(state),True)
    
    def test_disj(self): 
        state = State({'x':2}) 
        self.assertEqual(Disj(GreaterThan(Num(5),Num(10)),
                              Equal(Var('x'),Num(2))).run(state),Tr().run(state))

class TestComm(unittest.TestCase): 
    
    #Skip
    def test_skip(self):
        state = State({})
        self.assertEqual(Skip().run(state),state)
    
    #Assign
    def test_assign(self): 
        state = State({})
        state_aft_comm = State({'x':20})
        self.assertEqual(Assign(Var('x'),Num(20)).run(state),state_aft_comm)
    
    #Seq
    def test_seq_st(self): 
        state = State({})
        state_aft_comm = State({'x':10})
        self.assertEqual(Seq(Assign(Var('x'),Num(20)),Assign(Var('x'),Subs(Var('x'), Num(10)))).run(state),state_aft_comm)

    def test_seq_out(self): 
        state = State({})
        state_aft_comm = Output_type(20,{'x':20})
        self.assertEqual(Seq(Assign(Var('x'),Num(20)),Out(Var('x'))).run(state),state_aft_comm)

    def test_seq_f(self): 
        state = State({})
        state_aft_comm = Fail_type('Fail',{'x':20})
        self.assertEqual(Seq(Assign(Var('x'),Num(20)),Fail()).run(state),state_aft_comm)

    #If
    def test_if(self): 
        state = State({'x':0})
        state_aft_comm = State({'x':1})
        self.assertEqual(If(LessThan(Var('x'),Num(10)),
           Assign(Var('x'),Sum(Var('x'),Num(1))),
           Skip()).run(state),state_aft_comm)

    #While
    def test_while(self): 
        state = State({'x':0})
        state_aft_comm = State({'x':12})
        self.assertEqual(While(LessEqThan(Var('x'),Num(10)),
                            Assign(Var('x'),Sum(Var('x'),Num(2)))).run(state),state_aft_comm)

    #Newvar
    def test_newvar(self): 
        state = State({'x':4})
        state_aft_comm = Output_type(20,{'x':4})
        self.assertEqual(Newvar(Var('y'),Num(20),Out(Var('y'))).run(state),state_aft_comm)

    #Fail
    def test_fail(self): 
        state = State({'x':45})
        state_aft_comm = Fail_type('Fail',{'x':45})
        self.assertEqual(Fail().run(state),state_aft_comm)

    #Catch
    def test_catch(self): 
        state = State({'x':10})
        state_aft_comm = Output_type(10,(10,{'x':20}))
        self.assertEqual(Catch(Seq(Out(Var('x')),Seq(Out(Var('x')),Fail())),
                               Assign(Var('x'),Num(20))).run(state),state_aft_comm)
    
    #Out
    def test_Output_type(self): 
        state = State({'x':50})
        state_aft_comm = Output_type(51,{'x':50})
        self.assertEqual(Out(Sum(Var('x'),Num(1))).run(state),state_aft_comm)

    #Inp
    def test_input(self):
        state = State({'x':50})
        self.assertNotEqual(Inp(Var('y')).run(state),state)
            
class TestTypes(unittest.TestCase): 
    def test_return_types(self):
        state = State({})
        
        # Expresiones booleanas siempre retornan Tr o Fal
        self.assertEqual(Equal(Num(5), Num(5)).run(state), True)
        self.assertEqual(LessThan(Num(5), Num(10)).run(state), True)
        self.assertEqual(GreaterThan(Num(5), Num(3)).run(state), True)
        
        # Expresiones enteras siempre retornan int
        self.assertIsInstance(Num(5).run(state), int)
        self.assertIsInstance(Sum(Num(5), Num(3)).run(state), int)
        self.assertIsInstance(Var('x').run(state), int)

        #Comandos retornan tipos correctos
        self.assertIsInstance(Skip().run(state),State)
        self.assertIsInstance(Seq(Assign(Var('x'),Sum(Var('x'),Num(1))),
                                  Assign(Var('x'),Sum(Var('x'),Num(1)))).run(state),State)
        self.assertIsInstance(Seq(Assign(Var('x'),Sum(Var('x'),Num(1))),
                                  Out(Var('x'))).run(state),Output_type)
        self.assertIsInstance(Seq(Fail(),Out(Var('x'))).run(state),Fail_type)


    def test_input_types(self):
        #Chequear que las expresiones lancen error al intentar crearlas con tipos erroneos.
        #intexp
        with self.assertRaises(TypeError):
            Num('hola')
        
        with self.assertRaises(TypeError): 
            Sum((LessThan(Var('x'),Num(10))),Num(4))
        
        #boolexp
        with self.assertRaises(TypeError): 
            Equal(Num(4))
        
        with self.assertRaises(TypeError): 
            GreaterThan(Num(4), Equal(Num(4),Num(2)))

        #comm
        with self.assertRaises(TypeError): 
            Assign(Num(0),Num(1))

        with self.assertRaises(TypeError):
            Skip('x', Num(5))  

        with self.assertRaises(TypeError): 
            Seq(Skip())
        
        with self.assertRaises(TypeError): 
            state = State({})
            Newvar(Var('x'), Inp(Var('x')), Out(Var('x'))).run(state)
        
class TestPrograms(unittest.TestCase): 
    def test_programs(self):
        state = State({}) 

        self.assertEqual(Seq(
        Assign(Var('x'), Num(3)),
        Seq(
            While(
                GreaterThan(Var('x'), Num(0)),
                Seq(
                    Out(Var('x')),
                    Assign(Var('x'), Subs(Var('x'), Num(1)))
                )
            ),
            Out(Num(0))
        )).run(state),Output_type(3,(2,(1,(0,{'x':0})))))

        self.assertEqual(
            Seq(
            Assign(Var('a'), Num(5)),
            If(
                Equal(Var('a'), Num(5)),
                If(
                    GreaterThan(Var('a'), Num(3)),
                    Assign(Var('b'), Num(1)),
                    Assign(Var('b'), Num(2))
                ),
                Assign(Var('b'), Num(3)))
            ).run(state)
        ,State({'a':5, 'b':1}))

        self.assertEqual(Seq(
                        Assign(Var('x'), Num(100)),
                        Newvar(
                            Var('x'),
                            Num(1),
                            Seq(
                                Assign(Var('x'), Num(2)),
                                Out(Var('x'))
                            )
                        )
                    ).run(state), Output_type(2,{'x':100}))

        self.assertEqual(Catch(
                        Seq(
                            Assign(Var('x'), Num(1)),
                            Seq(
                                Fail(),
                                Out(Num(999))
                            )
                        ),
                        Out(Num(42))
                        ).run(state),Output_type(42,{'x':1}))
        
        self.assertEqual(Seq(
                        Assign(Var('x'), Num(0)),
                        While(
                            Fal(),
                            Assign(Var('x'), Num(1))
                        )
                        ).run(state),State({'x':0}))

        self.assertNotEqual(Seq(
                        Inp(Var('a')),
                        Seq(
                            Inp(Var('b')),
                            Out(Sum(Var('a'), Var('b')))
                        )
                        ).run(state),state)      
        
        self.assertEqual(Seq(
                        Assign(Var('x'), Num(1)),
                        While(
                            GtEqThan(Var('x'), Num(1)),
                            Seq(
                                Out(Var('x')),
                                If(
                                    Equal(Var('x'), Num(2)),
                                    Fail(),
                                    Assign(Var('x'), Sum(Var('x'), Num(1)))
                                )
                            )
                            )
                        ).run(state),Output_type(1,(2,('Fail',{'x':2}))))
        
        self.assertEqual(Seq(
                        Assign(Var('x'), Num(0)),
                        While(
                            LessThan(Var('x'), Num(5)),
                            Seq(
                                Out(Var('x')),
                                Assign(Var('x'), Sum(Var('x'), Num(1)))
                            )
                        )
                        ).run(state), Output_type(0,(1,(2,(3,(4,{'x':5}))))))
        
        self.assertEqual(Newvar(Var('x'), Num(5), 
                        Seq(
                            Out(Var('x')),
                            Seq(
                            Assign(Var('x'), Num(10)),
                            Out(Var('x')))
                        )).run(state), Output_type(5,(10,{})))

        self.assertEqual(Seq(
                        Assign(Var('x'), Num(5)),
                        Catch(
                            Seq(
                                Fail(),
                                Out(Var('x'))
                            ),
                            Out(Num(42))
                        )
                    ).run(state), Output_type(42,{'x':5})) 

        self.assertEqual(Seq(
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
                        ).run(state), Output_type(15,{'x':10,'y':5}))               


        self.assertEqual(Newvar(
                        Var('n'),
                        Num(4),
                        Newvar(
                            Var('resultado'),
                            Num(1),
                            Seq(
                                While(
                                    GreaterThan(Var('n'), Num(0)),
                                    Seq(
                                        Assign(Var('resultado'), Product(Var('resultado'), Var('n'))),
                                        Assign(Var('n'), Subs(Var('n'), Num(1)))
                                    )
                                ),
                                Out(Var('resultado')) # Debería imprimir 24
                            )
                        )
                    ).run(state), Output_type(24,{}))
        
        self.assertEqual(Seq(
                        Assign(Var('x'), Num(100)), # x global = 100
                        Seq(
                        Newvar(
                            Var('x'), # x de nivel intermedio = 10
                            Num(10),
                            Seq(
                                Assign(Var('i'), Num(2)), # Contador del bucle
                                While(
                                    GreaterThan(Var('i'), Num(0)),
                                    Seq(
                                        # Imprime la 'x' del nivel intermedio
                                        Out(Var('x')),
                                        Seq(
                                        # Se crea una nueva 'x' (la más interna)
                                        Newvar(
                                            Var('x'),
                                            Var('i'), # La x más interna toma el valor de i
                                            Out(Var('x')) # Imprime la x más interna
                                        ),
                                        Assign(Var('i'), Subs(Var('i'), Num(1))))
                                    )
                                )
                            )
                        ),
                        Out(Var('x'))) # Imprime la x global
                    ).run(state), Output_type(10,(2,(10,(1,(100,{'x':100, 'i':0}))))))
        

if __name__ == '__main__':
    print("-----------------Ejecutando batería de tests---------------\n" \
        "Contenido: \n" \
        " - TestComm\n" \
        " - TestTypes\n" \
        " - TestIntexpr\n" \
        " - TestBoolexpr\n" \
        " - TestPrograms\n")

    unittest.main()