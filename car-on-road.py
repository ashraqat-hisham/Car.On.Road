from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import*

def myInit():
    glMatrixMode(GL_PROJECTION)
    glClearColor(.5, .5, .5, 5)
    glClear(GL_COLOR_BUFFER_BIT)
    gluPerspective(60,1,0.1,50)
    gluLookAt(10, 10, 10 ,0, 0, 0, 0, 1, 0)

x = 0
angle = 0
z=0


#road

#right side
def BLUErightside():
    glColor(0,0,.5)
    glTranslate(1-x,0,-15)
    glScale(60,.5,1.5)
    glutSolidCube(3)


#left side
def BLUEleftside():

    glColor(0,0,.5)
    glTranslate(1-x,0,6)
    glScale(30,.5,1)
    glutSolidCube(3)

#black  right par
def BLACKrightcube():
    glColor(0,0,0)
    glScale(1,.5,1.5)
    glutSolidCube(3)

#black  left par
def BLACKleftcube():
    glColor(0,0,0)
    glScale(1,.5,1)
    glutSolidCube(3)

#righttree

#soil
def soil():
    glColor(.5,.5,.5)
    glScale(.7,0,.9)
    glutSolidCube(3)

def cylinder():

    glColor(.7,.5,0)
    glRotate(-90,1,0,0)
    glutSolidCylinder(.5,5,10,10)


def leaves():

    glColor(0.3,.6,0,1)
    glutSolidCylinder(2.5,0,20,10)

###############################################################

def draw():
 #Drawing

    glClear(GL_COLOR_BUFFER_BIT)
    global z
    global x
    global angle
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glColor3f(1,0,0)
    glTranslate(x,0,0)
    glScale(1,0.25,0.5)
    glLineWidth(8)
    glutWireCube(5)
 ################################
    glLoadIdentity()
    glTranslate(x,.25*5,0)
    glScale(0.5, 0.25, 0.5)
    glutWireCube(5)
#####################################
 #sphere
    #glColor3f(1,1,0)
    #glLoadIdentity()
    #glTranslate(4+x,2,1.5)
    #glRotate(angle,0,0,1)
    #glutSolidSphere(.3,200,200)

    #glColor3f(1,1,0)
    #glLoadIdentity()
    #glTranslate(x+4,2,2.5)
    #glRotate(angle,0,0,1)
    #glutSolidSphere(.3,200,200)

#############################################
    glColor3f(0, 0, 1)
    glLoadIdentity()
    glTranslate(x+2.5,-1.25*0.5,2.5*.5)
    glRotatef(angle,0,0,1)
    glutWireTorus(0.125,.5,12,8)
##############################################
    glColor3f(0, 0, 1)
    glLoadIdentity()
    glTranslate(x-2.5,-1.25*0.5,-2.5*.5)
    glRotatef(angle,0,0,1)
    glutWireTorus(0.125,.5,12,8)
###################################################

    glColor3f(0, 0, 1)
    glLoadIdentity()
    glTranslate(x-2.5,-1.25*0.5,2.5*.5)
    glRotatef(angle,0,0,1)
    glutWireTorus(0.125,.5,12,8)

###########################################

    glColor3f(0, 0, 1)
    glLoadIdentity()
    glTranslate(x+2.5,-1.25*0.5,-2.5*.5)
    glRotatef(angle,0,0,1)
    glutWireTorus(0.125,.5,12,8)

#################################################3
    #x = x+ 0.005
    #angle -= 0.1
  #animaton
    if (x>7):
      z=1
      x-=.03
      angle+=.9

    elif(x > -20 and z!= 0):
      x-=.03
      angle+=.9
    elif(x<-20):
      z=0
      x = x+ 0.03
      angle -= 0.9
    else:
      x+= 0.03
      angle-= 0.9


    glLoadIdentity()
    BLUEleftside()
    glLoadIdentity()
    BLUErightside()

##############################################################

    glLoadIdentity()
    glTranslate(12-x,0,-15)
    BLACKrightcube()

    glLoadIdentity()
    glTranslate(1-x,0,-15)
    BLACKrightcube()

    glLoadIdentity()
    glTranslate(-12-x,0,-15)
    BLACKrightcube()

    glLoadIdentity()
    glTranslate(-23-x,0,-15)
    BLACKrightcube()

    glLoadIdentity()
    glTranslate(-34-x,0,-15)
    BLACKrightcube()

    glLoadIdentity()
    glTranslate(-45-x,0,-15)
    BLACKrightcube()

    glLoadIdentity()
    glTranslate(-56-x,0,-15)
    BLACKrightcube()

################################################################

    glLoadIdentity()
    glTranslate(34-x,0,6)
    BLACKleftcube()

    glLoadIdentity()
    glTranslate(23-x,0,6)
    BLACKleftcube()


    glLoadIdentity()
    glTranslate(12-x,0,6)
    BLACKleftcube()

    glLoadIdentity()
    glTranslate(1-x,0,6)
    BLACKleftcube()


    glLoadIdentity()
    glTranslate(-12-x,0,6)
    BLACKleftcube()



    glLoadIdentity()
    glTranslate(-23-x,0,6)
    BLACKleftcube()



    glLoadIdentity()
    glTranslate(-34-x,0,6)
    BLACKleftcube()

###################################################
 #right trees


    glLoadIdentity()
    glTranslate(7-x,0,-15.5)
    soil()

    glLoadIdentity()
    glTranslate(7-x,0,-15.5)
    cylinder()

    glLoadIdentity()
    glTranslate(7-x,4.6,-15.5)
    leaves()
#########################################

    glLoadIdentity()
    glTranslate(-4.5-x,0,-15.5)
    soil()

    glLoadIdentity()
    glTranslate(-4.5-x,0,-15.5)
    cylinder()

    glLoadIdentity()
    glTranslate(-4.5-x,4.6,-15.5)
    leaves()
##########################################
    glLoadIdentity()
    glTranslate(-17-x,0,-15.5)
    soil()

    glLoadIdentity()
    glTranslate(-17-x,0,-15.5)
    cylinder()

    glLoadIdentity()
    glTranslate(-17-x,4.6,-15.5)
    leaves()

#################################################

    glLoadIdentity()
    glTranslate(-29-x,0,-15.5)
    soil()

    glLoadIdentity()
    glTranslate(-29-x,0,-15.5)
    cylinder()

    glLoadIdentity()
    glTranslate(-29-x,4.6,-15.5)
    leaves()
 ####################################################

    glLoadIdentity()
    glTranslate(-43-x,0,-15.5)
    soil()

    glLoadIdentity()
    glTranslate(-43-x,0,-15.5)
    cylinder()

    glLoadIdentity()
    glTranslate(-43-x,4.6,-15.5)
    leaves()
##############################################
    glLoadIdentity()
    glTranslate(-56-x,0,-15.5)
    soil()

    glLoadIdentity()
    glTranslate(-56-x,0,-15.5)
    cylinder()

    glLoadIdentity()
    glTranslate(-56-x,4.6,-15.5)
    leaves()





 ###############################################################

 #left trees


    glLoadIdentity()
    glTranslate(7-x,0,6)
    soil()

    glLoadIdentity()
    glTranslate(7-x,0,6)
    cylinder()

    glLoadIdentity()
    glTranslate(7-x,4.6,6)
    leaves()
#########################################

    glLoadIdentity()
    glTranslate(-4.5-x,0,6)
    soil()

    glLoadIdentity()
    glTranslate(-4.5-x,0,6)
    cylinder()

    glLoadIdentity()
    glTranslate(-4.5-x,4.6,6)
    leaves()
##########################################
    glLoadIdentity()
    glTranslate(-17-x,0,6)
    soil()

    glLoadIdentity()
    glTranslate(-17-x,0,6)
    cylinder()

    glLoadIdentity()
    glTranslate(-17-x,4.6,6)
    leaves()

#################################################

    glLoadIdentity()
    glTranslate(-29-x,0,6)
    soil()

    glLoadIdentity()
    glTranslate(-29-x,0,6)
    cylinder()

    glLoadIdentity()
    glTranslate(-29-x,4.6,6)
    leaves()
 ####################################################

    glLoadIdentity()
    glLineWidth(4)
    glColor(1,1,1)
    glBegin(GL_LINES)
    glVertex3f(15-x, 0,-5)
    glVertex3f(-50-x, 0,-5)
    glEnd()

    glFlush()

#####################################################










glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow(b"program")
glutIdleFunc(draw)
glutDisplayFunc(draw)
myInit()
glutMainLoop()
