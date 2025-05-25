# Decisión de diseño:
Si una variable no está definida en el estado, se agrega con valor 0. Esto permite que las operaciones sobre variables no definidas no generen errores, sino que simplemente asuman un valor por defecto.

Si se pide input y se ingresa un valor no entero, se vuelve a pedir el input. Esto asegura que el programa no se detenga por un error de tipo, sino que siga pidiendo un valor válido.


El el caso de la asignación, retorna otro estado nuevo o es el mismo modificado? Sería como declarativo porque no se modifica el estado original, sino que se crea uno nuevo. 

# TODO
Que pasa con la división por cero?
Adaptar los comandos con las extensiones f*, f+, etc. 
Testing de los comandos