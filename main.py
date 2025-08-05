import pygame
import numpy as np

# Initialise pygame

#Defnimos unas cosiiitas

# Create the game window
width = 800
height = 800
screen = pygame.display.set_mode((width, height))

xmin = -2
xmax = 1
ymin = -1.5
ymax = 1.5
max_iter = 150
z0 = 0

xrange = np.linspace(xmin, xmax, 800)
yrange = np.linspace(ymin, ymax, 800)
palette = [(247, 241, 250),(248, 232, 255),(224, 170, 255), (248, 232, 255), (229, 207, 237), (209, 184, 218), (187, 156, 202), (165, 127, 185), (143, 99, 168),(120, 76, 146), (97, 52, 124), (85, 42, 111), (72, 31, 98),(65, 28, 89),(59, 25, 81),(54, 23, 74),(45, 19, 61),(41, 17, 55),(37, 15, 50),(31, 13, 42),(25, 10, 33),(19, 8, 25),(12, 5, 16)]

def mandelbrot(x, y):
    iter = 0
    z = 0
    c = complex(x, y)
    while iter < max_iter:
        if abs(z) > 2:
            index = int(iter / max_iter * (len(palette)-1))
            return(palette[index])
        else:
            z = z*z + c
            iter+=1
    black = (0,0,0)
    return(black)

#Getting the numbers and colors
colorlist = []
for x in xrange:
    for y in yrange:
        colorss = (mandelbrot(x, y))
        colorlist.append(colorss)

colorlist = np.array(colorlist)
colors_array = np.array(colorlist, dtype=np.uint8)
arr= colors_array.reshape((800, 800, 3))
#GRAPHIC

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            pygame.display.update()

# Blit array to screen
pygame.surfarray.blit_array(screen, arr)

main()