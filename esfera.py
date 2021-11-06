from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

from textures import create_texture
from util import defineSphere

class Esfera():
    def __init__(self, radius, resolution, texture_name) -> None:
        self.position = [0, 0, 0]
        self.rotation = [0, 0, 0]
        self.scale = [1, 1, 1]
        
        self.radius = radius
        self.texture_name = texture_name
        self.resolution = resolution


    def setup(self, width, height):
        self.texture = create_texture(self.texture_name)
        self.vertexList = defineSphere(self.radius, self.resolution)

    def draw(self):
        glPushMatrix()
        
        glTranslatef(*self.position)

        glRotatef(self.rotation[0], 1, 0, 0)
        glRotatef(self.rotation[1], 0, 1, 0)
        glRotatef(self.rotation[2], 0, 0, 1)


        glBindTexture(GL_TEXTURE_2D, self.texture)
        glBegin(GL_TRIANGLES)

        for vertex in self.vertexList:
            glTexCoord2f(*vertex.uv)
            glVertex3f(*vertex.position)

        glEnd()

        glPopMatrix()
    

    

