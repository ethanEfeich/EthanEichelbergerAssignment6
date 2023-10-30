# Ethan Eichelberger

import sys
import pygame
from pygame.locals import *
from OpenGL.GL import *


blue = (0.0, 0.0, 1.0)
green = (0.0, 1.0, 0.0)
red = (1.0, 0.0, 0.0)
cyan = (0.0, 1.0, 1.0)
purple = (0.5, 0.0, 1.0)
yellow = (1.0, 1.0, 0.0)
white = (1.0, 1.0, 1.0)

vertices = (
    (-0.5, -0.5, -0.5),
    (-0.5, 0.5, -0.5),
    (0.5, 0.5, -0.5),
    (0.5, -0.5, -0.5),
    (-0.5, -0.5, 0.5),
    (-0.5, 0.5, 0.5),
    (0.5, 0.5, 0.5),
    (0.5, -0.5, 0.5),
)


def cube():
    # blue face
    # glLoadIdentity()
    glBegin(GL_QUADS)
    glColor3fv(green)
    glVertex3fv(vertices[0])
    glVertex3fv(vertices[1])
    glVertex3fv(vertices[2])
    glVertex3fv(vertices[3])
    # green face
    glColor3fv(blue)
    glVertex3fv(vertices[4])
    glVertex3fv(vertices[5])
    glVertex3fv(vertices[6])
    glVertex3fv(vertices[7])
    # red
    glColor3fv(red)
    glVertex3fv(vertices[0])
    glVertex3fv(vertices[1])
    glVertex3fv(vertices[5])
    glVertex3fv(vertices[4])
    # # cyan
    glColor3fv(cyan)
    glVertex3fv(vertices[2])
    glVertex3fv(vertices[6])
    glVertex3fv(vertices[7])
    glVertex3fv(vertices[3])
    # # purple
    glColor3fv(purple)
    glVertex3fv(vertices[0])
    glVertex3fv(vertices[3])
    glVertex3fv(vertices[7])
    glVertex3fv(vertices[4])
    # white
    glColor3fv(white)
    glVertex3fv(vertices[1])
    glVertex3fv(vertices[2])
    glVertex3fv(vertices[6])
    glVertex3fv(vertices[5])

    glEnd()


def main():
    pygame.init()
    display = (800, 600)

    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    up = 0
    down = 0
    left_z = 0
    right_z = 0
    left_y = 0
    right_y = 0
    while True:

        if left_z:
            right_y, right_z, down, up = 0, 0, 0, 0
            glRotatef(5, 0, 0, .5)
        if left_y:
            right, down, up = 0, 0, 0
            glRotatef(5, 0, .5, 0)
        if right_z:
            left, down, up = 0, 0, 0
            glRotatef(-5, 0, 0, .5)
        if right_y:
            left, down, up = 0, 0, 0
            glRotatef(-5, 0, .5, 0)
        if up:
            left, down, right = 0, 0, 0
            glRotatef(5, .5, 0, 0)
        if down:
            left, up, right = 0, 0, 0
            glRotatef(-5, .5, 0, 0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    right_z = 1
                if event.key == pygame.K_l:
                    left_z = 1
                if event.key == pygame.K_u:
                    up = 1
                if event.key == pygame.K_d:
                    down = 1
                if event.key == pygame.K_s:
                    left_y = 1
                if event.key == pygame.K_a:
                    right_y = 1
            if event.type == pygame.KEYUP:
                left_y = 0
                left_z = 0
                right_y = 0
                right_z = 0
                up = 0
                down = 0
        glDepthFunc(GL_LESS)  # this is default
        glEnable(GL_DEPTH_TEST)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()

