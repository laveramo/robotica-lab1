import termios, sys, os
TERMIOS = termios
import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute, TeleportRelative

def getKey():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
    new[6][TERMIOS.VMIN] = 1
    new[6][TERMIOS.VTIME] = 0
    termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
    c = None
    try:
        c = os.read(fd, 1)
    finally:
        termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
    return c
    
def pubVel(vel_x, ang_z, t):
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('velPub', anonymous=False)
    vel = Twist()
    vel.linear.x = vel_x
    vel.angular.z = ang_z
    endTime = rospy.Time.now() + rospy.Duration(t)
    while rospy.Time.now() < endTime:
        pub.publish(vel)

def teleport_absolute(x, y, ang):
    rospy.wait_for_service('/turtle1/teleport_absolute')
    try:
        teleportA = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)
        resp1 = teleportA(x, y, ang)
    except rospy.ServiceException as e:
        print(str(e))

def teleport_relative(linear, angular):
    rospy.wait_for_service('/turtle1/teleport_relative')
    try:
        teleportA = rospy.ServiceProxy('/turtle1/teleport_relative', TeleportRelative)
        resp1 = teleportA(linear, angular)
    except rospy.ServiceException as e:
        print(str(e))

def check(tecla):
    if tecla == b'w':
        pubVel(2,0,0.5)
    elif tecla == b's':
        pubVel(-2,0,0.5)
    elif tecla == b'a':
        pubVel(0,1,0.5)
    elif tecla == b'd':
        pubVel(0,-1,0.5)
    elif tecla == b'r':
        teleport_absolute(5,5,0)
    elif tecla == b' ':
        teleport_relative(0,3.14)
    else:
        pubVel(0,0,0)
    

if __name__ == '__main__':
    print("Press q for quit")
    while(1):
        pubVel(0,0,0.1)
        tecla = getKey()
        check(tecla)
        if tecla == b'q':
            break