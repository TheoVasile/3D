import pygame as pg
import D3

#initialize pygame module
pg.init()

#initialize screen variables
w = 500
h = 500
screen = pg.display.set_mode((w, h))
pg.display.set_caption("3D")
clock = pg.time.Clock()
fps = 60

object = D3.add.Cube(0,0,0,0,0,0)

#start loop
running = True
while running:
    #go through user inputs
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    #set background color
    screen.fill((0, 0, 0))

    object.display()

    #update screen
    pg.display.update()
    clock.tick(fps)