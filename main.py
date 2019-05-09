import pygame as pg
import D3

#initialize pygame module
pg.init()

#initialize screen variables
w = D3.WIDTH
h = D3.HEIGHT
screen = D3.SCREEN
pg.display.set_caption("3D")
clock = pg.time.Clock()
fps = 60

object = D3.add.Cube(0, 0, 0, 0, 0, 0)
camera = D3.add.Camera(0, 0, 0, 0, 0, 0, w, h)

#start loop
running = True
while running:
    #go through user inputs
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    #set background color
    screen.fill((0, 0, 0))

    object.display(camera)

    #update screen
    pg.display.update()
    clock.tick(fps)