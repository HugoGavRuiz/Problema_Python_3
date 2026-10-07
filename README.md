# Problema_Python_3

Jorge Oliver
Hugo Gavilán
Carlos Gutiérrez

Demuestra que los inputs son strings, que si quieres ejercer operaciones matemáticas tienes que convertirlos al tipo esperado y que el round redondea el primer argumento con los decimales que le digas en el segundo argumento.

El resultado esperado en el problema es, en primer lugar, la petición al usuario de inputs. En segundo lugar, devolverá el tipo de los inputs dados. Después, se comprueba que la conversión ha sido correcta y se realiza el redondeo del precio total a 2 decimales.

La pregunta para la clase será: ¿Qué pasa si intentamos convertir "Hola" a int?. El resultado es que el programa da un value error.

Error típico es intentar multiplicar un entero o un float con un string o directamente multiplicar dos strings entre ellos. Si no fuese multiplicación y fuese suma, habría que andar con más cuidado pues no daría error si no que concatenaría los strings.