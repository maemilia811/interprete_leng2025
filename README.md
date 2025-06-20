# Interprete de Lenguaje LIS 
Intérprete de lenguaje LIS visto en la materia Lenguajes y Compiladores de FaMAF, UNC. 
En este proyecto se define la sintaxis y semántica del lenguaje, tomando los conceptos vistos en el teórico de la materia y tratando de mantener en lo más posible la implementación utilizada en el teórico.
Dado un programa en LIS, el intérprete lo ejecuta y retorna un estado modificado. Hay tres tipos de estados posibles: 
- State: modela un estado sin error con un diccionario. 
- Output_type: tipo _(exp,estado)_ donde _exp_ es la expresión que se imprime. 
- Fail_type: _('Fail',estado)_ para indicar que hubo error. 

Se mantiene la misma idea de dominio semántico recursivo, de manera tal que si se realizan varios outputs, se anidan tuplas. 

## Comandos del lenguaje LIS
Los siguientes comandos se implementan mediante una clase en Python, cada uno de los cuales representa una instrucción del lenguaje LIS:
- Assign: asignación de una valor entero a una variable.
- Out: imprime el valor de una expresión entera. 
- Inp: solicita al usuario un valor entero y lo asigna a una variable.
- If: evalúa una condición booleana y ejecuta un bloque de código si la condición es verdadera.
- While: ejecuta un bloque de código mientras una condición booleana sea verdadera.
- Fail: lanza un error y retorna un estado de tipo Fail.
- Catch: maneja un error lanzado por el comando Fail y retorna un estado modificado.
- Newvar: Crea variable con alcance local y restaura el valor de la variable al salir del bloque.
- Seq: ejecuta una secuencia de comandos en orden, modificando el estado actual.

La semántica de cada comando está definida como un método de la clase que recibe el esado actual y retorna un nuevo estado modificado.
Además, se implementan clases para expresiones enteras y booleanas, siguiendo la misma lógica. 

## Decisión de diseño:
Se tomaron las siguientes decisiones de diseño para la implementación del intérprete:
- Los estados se modelan como diccionarios, de manera que si se quiere acceder a una variable que no está definida, se asume que su valor es 0.

- Los programas se ejecutan utilizando un estado, y retorna un nuevo estado modificado.

- El comando Inp para input de una variable se implementa recursivamente para evitar retornar una funcion

## Test
Se implementaron tests unitarios para cada comando del lenguaje LIS, verificando que el estado se modifique correctamente y que se manejen los errores de manera adecuada. Los tests se encuentran en la carpeta `tests` y se pueden ejecutar utilizando `python3 tests/test.py`. 