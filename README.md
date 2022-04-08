# Laboratorio 1 - Robótica: Introducción a ROS
## 1. Comandos de mayor uso en la consola de Linux
#### pwd: print working directory
Imprime el directorio donde se está trabajando.
![![image.png](https://i.postimg.cc/Y0mHHpN4/image.png)](https://postimg.cc/q60YcH50)
#### ls: list
Imprime todos los archivos y carpetas contenidos dentro de la carpeta (directorio) actual. También puede imprimir el contenido de una carpeta donde no se está actualmente escribiendo la dirección de la misma.
![![image.png](https://i.postimg.cc/BnPMBjSP/image.png)](https://postimg.cc/4YZ6JNhX)
#### cd: change directory
Cambia el directorio actual al directorio que se le especifique.
![![image.png](https://i.postimg.cc/4NDzZBGn/image.png)](https://postimg.cc/56mHS56M)
#### touch
Crea un archivo en el directorio de trabajo
![![image.png](https://i.postimg.cc/t4m7pgWk/image.png)](https://postimg.cc/xXM9PnsN)
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
Luego, a través de la función `rosmessage()` se crea un mensaje vacío determinado por el objeto publicador que se creó anteriormente. Este contiene
#### Subscriber
#### Server

## 3. Conexión de ROS con Python
### Procedimiento
#### Resultados y análisis

## Referencias
[1] [Laboratorio 1 - Parte 2: Introducción ROS](https://drive.google.com/file/d/19UOE_eI-ob2ZymNHWFrYgrxLQfgOon43/view) 
[2] [Connect to ROS Network - MATLAB rosinit](https://www.mathworks.com/help/ros/ref/rosinit.html)
[3] [Create ROS messages - MATLAB rosmessage](https://www.mathworks.com/help/ros/ref/rosmessage.html)
