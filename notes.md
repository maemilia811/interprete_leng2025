# Decisión de diseño:
Si una variable no está definida en el estado, se agrega con valor 0. Esto permite que las operaciones sobre variables no definidas no generen errores, sino que simplemente asuman un valor por defecto.

Si se pide input y se ingresa un valor no entero, se vuelve a pedir el input. Esto asegura que el programa no se detenga por un error de tipo, sino que siga pidiendo un valor válido.


El el caso de la asignación, retorna otro estado nuevo o es el mismo modificado? Sería como declarativo porque no se modifica el estado original, sino que se crea uno nuevo. 

El input se implementa recursivamente para evitar retornar una funcion


# TODO
asignación de Nat al estado
cambiar nombre del comando Nat por algo entero y cambiar output por out_type
revisar el fail_type
Chequear el comando ese con fail 
Testing de los comandos 
Que pasa con la división por cero?
ver que pasa con expresiones booleanas, si hay que agregar => y eso. 