import pygame
import numpy as np
from palettes import palette_gen

# Initialise pygame

pygame.init()

#Defnimos unas cosiiitas

zoom_factor = 3

def mandelbrot(x, y):
    iter = 0
    z = 0
    c = complex(x, y)
    while iter < max_iter:
        if abs(z) > 2:
            return(palette[iter])
        else:
            z = z*z + c
            iter+=1
    return((0,0,0))

# Create the game window
width = 1000
height = 600
screen = pygame.display.set_mode((width, height))

max_iter = 100

colors = [(72, 3, 85),(118, 153, 212),(99, 180, 209),(144, 252, 249)]
palette = palette_gen(colors, max_iter)

def graph_mandelbrot(xmin, xmax, ymin, ymax):
    xrange = np.linspace(xmin, xmax, 1000)
    yrange = np.linspace(ymin, ymax, 600)
    colorlist = []
    #Getting the numbers and colors
    for x in xrange:
        for y in yrange:
            colorss = (mandelbrot(x, y))
            colorlist.append(colorss)
    colorlist = np.array(colorlist)
    colors_array = np.array(colorlist, dtype=np.uint8)
    arr= colors_array.reshape((1000, 600, 3))
    # Blit array to screen
    pygame.surfarray.blit_array(screen, arr)

def zoom_in(px,py, xmin, xmax, ymin, ymax):
    x = xmin + (px / width)  * (xmax - xmin)
    y = ymin + (py / height) * (ymax - ymin)
    new_width  = (xmax - xmin) / zoom_factor
    new_height = (ymax - ymin) / zoom_factor
    xmin = x - new_width / 2
    xmax = x + new_width / 2
    ymin = y - new_height / 2
    ymax = y + new_height / 2
    return (xmin, xmax, ymin, ymax)
    
#GRAPHIC

def main():
    #Start conditions
    xmin = -3
    xmax = 2
    ymin = -1.5
    ymax = 1.5
    graph_mandelbrot(xmin, xmax, ymin, ymax)
    run = True
    while run:
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                px,py = pygame.mouse.get_pos()
                xmin, xmax, ymin, ymax = zoom_in(px,py,xmin,xmax,ymin,ymax)
                graph_mandelbrot(xmin, xmax, ymin, ymax)
            pygame.display.update()
    
main()