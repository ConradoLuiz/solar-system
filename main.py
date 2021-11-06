import math
import png
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import time
from esfera import Esfera

a = 0

terra = Esfera(.2, 10, './img/terra.png')
sol = Esfera(.5, 20, './img/sun-low-res.png')
lua = Esfera(.04, 10, './img/moon-low-res.png')

distancia_sol_terra = 2.5
distancia_terra_lua = .4


def draw():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    sol.rotation = [-90, 0, -a]
    sol.position = [0, 0, 0]
    sol.draw()

    # -------------------------------------------------

    terra.rotation = [-90, 0, -a]

    terra.position = [
        math.cos(a/100) * distancia_sol_terra + sol.position[0],
        0, 
        math.sin(a/100) * distancia_sol_terra + sol.position[2]
    ]
    terra.draw()

    # -------------------------------------------------

    lua.rotation = [-90, 0, -a]

    lua.position = [
        math.cos(a/20) * distancia_terra_lua + terra.position[0],
        0, 
        math.sin(a/20) * distancia_terra_lua + terra.position[2]
    ]
    lua.draw()

    # -------------------------------------------------
    glutSwapBuffers()

    a += 1

def InitGL(width, height):
    print('Carregando texturas...')

    terra.setup(width, height)
    sol.setup(width, height)
    lua.setup(width, height)

    glEnable(GL_TEXTURE_2D)
    glEnable(GL_MULTISAMPLE)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glClearColor(0., 0., 0., 1.)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, width/height, 0.1, 100.0)
    glTranslatef(0.0, -0.4, -6)

    print('Done!')

delta_time = 1
last_time = 0
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(0, timer, 1)

    global last_time
    global delta_time

    current_time = time.time()
    delta_time = current_time - last_time
    last_time = current_time

if __name__ == '__main__':
    width = 1280
    height = 720
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA |
                        GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(int(width), int(height))
    window = glutCreateWindow("Sistema Solar")
    glutDisplayFunc(draw)

    InitGL(width, height)
    glutTimerFunc(0, timer, 1)
    glutMainLoop()

