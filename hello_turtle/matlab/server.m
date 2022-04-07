%%
%rosinit; %Conexión con nodo maestro, correr solo 1 una vez
%%
client = rossvcclient('/turtle1/teleport_absolute'); %Creación subscriptor
%%
request = rosmessage(client);
request.X = 5; %insertar posición en x
request.Y = 5; %insertar posición en y
request.Theta = pi; %insertar orientación
if isServerAvailable(client)
    resp = call(client,request,"Timeout",3);
else
    error("Service server not available on network")
end
%%
%Para finalizar el nodo maestro
rosshutdown
