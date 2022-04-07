%%
%rosinit; %Conexión con nodo maestro, correr solo 1 una vez
%%
velSub = rossubscriber('/turtle1/pose','turtlesim/Pose'); %Creación subscriptor
%%
poseMsg = velSub.LatestMessage %Recibe el último mensaje
%poseMsg = receive(velSub); % Otra opción