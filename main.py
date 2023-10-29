# Ethan Eichelberger

import sys
import pygame
from pygame.locals import *
from OpenGL.GL import *

colors = (
    (0.0, 0.0, 1.0),  # blue
    (0.0, 1.0, 0.0),  # green
    (1.0, 0.0, 0.0),  # red
    (0.0, 1.0, 1.0),  # cyan
    (0.5, 0.0, 1.0),  # purple
    (1.0, 1.0, 0.0),  # yellow
    (1.0, 0.0, 0.43),  # pink?
    (1.0, 1.0, 1.0)  # white
)

def box():
    # glBegin(GL_POLYGON)
    # glLoadIdentity()
    # glColor3f(0.0,0.0,1.0)
    # glVertex2f(-0.5,-0.5)
    # glVertex2f(-0.5,0.5)
    # glVertex2f(0.5,0.5)
    # glVertex2f(0.5, -0.5)
    # glEnd()
    glBegin(GL_QUADS)
    glColor3f(0.5, 0.0, 1.0) #purple
    glVertex2f(-0.75, 0.75)
    glColor3f(1.0, 0.0, 0.0) # make this vertex red
    glVertex2f(-0.75, -0.75)
    glColor3f(0.0, 1.0, 0.0) #/ make this  vertex green
    glVertex2f(0.75, -0.75)
    glColor3f(1.0, 1.0, 0.0) #/ make this  vertex   yellow
    glVertex2f(0.75, 0.75)
    glEnd()


def main():
    pygame.init()
    display = (800, 600)

    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()

        glClear(GL_COLOR_BUFFER_BIT)
        box()
        pygame.display.flip()
        pygame.time.wait(10)


main()
