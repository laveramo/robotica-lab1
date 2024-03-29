# Laboratorio 1 - Robótica: Introducción a ROS
## 1. Comandos de mayor uso en la consola de Linux
#### pwd: print working directory
Imprime el directorio donde se está trabajando.

[![image.png](https://i.postimg.cc/Y0mHHpN4/image.png)](https://postimg.cc/q60YcH50)

#### ls: list
Imprime todos los archivos y carpetas contenidos dentro de la carpeta (directorio) actual. También puede imprimir el contenido de una carpeta donde no se está actualmente escribiendo la dirección de la misma.

[![image.png](https://i.postimg.cc/BnPMBjSP/image.png)](https://postimg.cc/4YZ6JNhX)

#### cd: change directory
Cambia el directorio actual al directorio que se le especifique.

[![image.png](https://i.postimg.cc/4NDzZBGn/image.png)](https://postimg.cc/56mHS56M)

#### touch
Crea un archivo en el directorio de trabajo.

[![image.png](https://i.postimg.cc/t4m7pgWk/image.png)](https://postimg.cc/xXM9PnsN)

#### rm: remove
Borra un archivo.

#### mkdir: make directory
Crea un nuevo directorio (carpeta).

[![image.png](https://i.postimg.cc/zGgYLjYL/image.png)](https://postimg.cc/v4bNk5BM)

#### rmdir: remove directory
Borrar un directorio.

#### mv: move
Mueve un archivo o directorio que especifiques a una ubicación deseada.

#### cp: copy
Copia un archivo o directorio en una nueva ubicación deseada.

### man: manual
Muestra el manual de ayuda para un comando que se le especifique.

## 2. Conexión de ROS con MATLAB
### Procedimiento
1. Iniciamos el nodo maestro de ROS escribiendo el comando `roscore` en una terminal.
2. Iniciamos el nodo turtlesim con el comando `rosrun turtlesim turtlesim_node` el cual corre la simulación de la  tortuga.

[![image.png](https://i.postimg.cc/J7NfWncX/image.png)](https://postimg.cc/qg7bspFB)

3. En Matlab, se crea el script *publisher.m* (contenido en la carpeta *matlab*) el cual es tomado de la guía de laboratorio[1]. Este script crea una conexión de MATLAB con el nodo maestro de ROS, además de crear un publicador para enviar un mensaje que permite modificar la velocidad de la tortuga.
4. En la misma carpeta *matlab* se crea el script *subscriber.m* el cual permite suscribirse al tópico de pose de la simulación turtle1.
5. En esta misma carpeta se crea el script *server.m* el cual permite enviar todos los valores asociados a la pose de turtle1 (posición en x, en y, ángulo theta) a través del servicio *teleport_absolute*.

### Resultados y análisis
#### Publisher
Como mencionamos anteriormente, el script *publisher.m* crea un publicador a través de la función `rospublisher()` la cual recibe como parámetros: el tópico en el que publicará y el tipo de mensaje.
Luego, a través de la función `rosmessage()` se crea un mensaje vacío determinado por el objeto publicador que se creó anteriormente. Este contiene los datos de la velocidad lineal y angular relativa. Así, se cambian los valores del mensaje, en este caso con `velMsg.Linear.X=1` y se envía el mensaje con la función `send()`. Al correr repetidas veces la última sección de este script, vemos que la tortuga se mueve en dirección horizontal.

[![image.png](https://i.postimg.cc/7LMT1Sr9/image.png)](https://postimg.cc/WDz3TF3q)

#### Subscriber
El script *subscriber.m* crea un suscriptor a través de la función `rossubscriber()` la cual recibe como parámetros el tópico de la pose de turtle1 y su tipo de mensaje. Luego, a través del método `.LatestMessage` del suscriptor se recibe el último mensaje enviado. Aquí podemos ver la información de la pose de la tortuga.

[![image.png](https://i.postimg.cc/Yqz9sMs2/image.png)](https://postimg.cc/PPNTLsH0)

#### Server y finalización del nodo maestro
El archivo *server.m* permite enviar todos los valores de la pose de turtle1 a través del servicio *teleport_absolute*. Para ello, se crea un objeto tipo cliente con la función `rossvcclient()` la cual recibe como parámetro el nombre del servicio. Luego, con la función `rosmessage()` se crea un mensaje al que se le cambiarán los valores de la pose, para finalmente llamar al servicio con la función `call()`. En la imagen podemos observar como se teleporta la tortuga a la posición x=5, y=5, theta=pi.

[![image.png](https://i.postimg.cc/V6Z9MXXT/image.png)](https://postimg.cc/2bvBNbcF)

Finalmente, se finaliza el nodo maestro de ROS con el comando `rosshutdown`.

## 3. Conexión de ROS con Python
### Procedimiento
1. Iniciamos el nodo maestro de ROS y el nodo turtle_sim (pasos 1 y 2 de la sección anterior). 
2. Creamos el archivo *myTeleopKey.py* en la carpeta *scripts* el cual permite que la tortuga:
	- Se mueva hacia adelante y hacia atrás con las teclas W y S.
	- Gire en sentido horario y antihorario con las teclas D y A.
	- Retorne a su posición y orientación centrales con la tecla R.
	- De un giro de 180° con la tecla espacio.
3. Primero, para lograr la lectura de las teclas se crea la función `getKey()` tomada de [5].
4. Para lograr el movimiento hacia adelante, atrás y el giro horario y antihorario se crea la función `PubVel()` la cual recibe como parámetros la velocidad lineal y angular (relativa). Esta función permite publicar en el tópico *turtle1/cmd_vel* 
5. Para lograr el retorno a la posición se crea la función `teleport_absolute()` la cual usa el servicio *turtle1/teleport_absolute*. Esta función recibe las coordenadas x,y y el ángulo theta que conforman la pose de la tortuga. Así, si se desea retornar a la posición central, se llamará esta función con x=5, y=5 y theta=0.
6. Para lograr el giro de 180° se crea la función `teleport_relative()` la cual usa el servicio *turtle1/teleport_relative*. Esta función recibe el movimiento relativo lineal y angular, de esta forma si se quiere dar un giro de 180° se llamará esta función con linear=0 y angular=pi.
7. Finalmente, para definir las diferentes tareas que realizará cada tecla se crea la función `check()` que llamará las funciones anteriores dependiendo de la tecla oprimida. Por otro lado, en el main del script se tiene un ciclo infinito (se sale del mismo oprimiendo la tecla q) que se mantiene leyendo el teclado.
### Resultados y análisis
La función`PubVel()` que permite el movimiento hacia adelante, atrás y los giros incluye como parámetro el tiempo, por lo cual, modificar esta variable hará que el movimiento de la tortuga sea más o menos suave o brusco. En la siguiente imagen se muestra una secuencia de movimientos donde se usó un tiempo de 0.5 s:

[![image.png](https://i.postimg.cc/y8c8ZRMN/image.png)](https://postimg.cc/BjZ3WjQW)

En cambio en esta, se usó un tiempo de 1 s:

[![image.png](https://i.postimg.cc/4NC6k6Qf/image.png)](https://postimg.cc/hhrzV7Y6)

El movimiento de la tortuga no solo se ve afectado por este tiempo sino también por los valores de las velocidades. En este caso usamos una velocidad de magnitud 2 en todos los casos ya que con valores menores la tortuga no avanza tanto por cada vez que se oprime una tecla.

También es importante mencionar que `PubVel()` utiliza la velocidad lineal en x de la tortuga ya que se refiere al eje x relativo de ella, es decir, el que está alineado con su cabeza. Si el código se cambiara para que usara la velocidad en y el comportamiento no sería el deseado.

Finalmente, en el ciclo while se vuelve a llamar constantemente a esta función con velocidades iguales a cero, para que pare cuando no se esté detectando ninguna tecla.

## Referencias
[1] [Laboratorio 1 - Parte 2: Introducción ROS](https://drive.google.com/file/d/19UOE_eI-ob2ZymNHWFrYgrxLQfgOon43/view)
 
[2] [Connect to ROS Network - MATLAB rosinit](https://www.mathworks.com/help/ros/ref/rosinit.html)

[3] [Create ROS messages - MATLAB rosmessage](https://www.mathworks.com/help/ros/ref/rosmessage.html)

[4] [Connect to ROS service server - MATLAB rossvcclient](https://www.mathworks.com/help/ros/ref/serviceclient.html	)

[5] [Python for fun: Get Key Pressed in Python](http://python4fun.blogspot.com/2008/06/get-key-press-in-python.html)
