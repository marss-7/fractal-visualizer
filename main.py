import pygame
import numpy as np
from palettes import palette_gen
from datetime import datetime

# Initialise pygame
pygame.init()

#Defnimos unas cosiiitas

# Create the game window
width = 1000
height = 600
screen = pygame.display.set_mode((width, height))

def mandelbrot(c, max_iter):
    zarray = np.zeros(c.shape)
    mask = np.ones(c.shape, dtype=bool)
    z = np.zeros(c.shape, dtype=complex)
    for i in range(max_iter):
        z[mask] = z[mask]*z[mask] + c[mask]
        escape = np.abs(z) > 2
        new_escapes = escape & mask
        zarray[new_escapes] = i
        mask[new_escapes] = False
    zarray[mask] = max_iter   
    zarray = np.array(zarray, dtype=np.int32)
    return(zarray)

def graph_mandelbrot(xmin, xmax, ymin, ymax, pal, max_iter):
    tstart = datetime.now()
    xrange = np.linspace(xmin, xmax, 1000)
    yrange = np.linspace(ymin, ymax, 600)
    x, y = np.meshgrid(xrange, yrange)
    c = x + 1j * y
    colorlist  = np.zeros(c.shape)
    #Getting the numbers and colors
    iterations = (mandelbrot(c, max_iter))
    colorlist = pal[iterations]
    colors_array = np.array(colorlist, dtype=np.uint8)
    pygame.surfarray.blit_array(screen, colors_array.swapaxes(0, 1))
    tend = datetime.now()
    print((tend-tstart).seconds)
    # Blit array to screen
    return()

def zoom(px,py, xmin, xmax, ymin, ymax, zoom_factor):
    x = xmin + (px / width)  * (xmax - xmin)
    y = ymin + (py / height) * (ymax - ymin)
    new_width  = (xmax - xmin) / zoom_factor
    new_height = (ymax - ymin) / zoom_factor
    xmin = x - new_width / 2
    xmax = x + new_width / 2
    ymin = y - new_height / 2
    ymax = y + new_height / 2
    return (xmin, xmax, ymin, ymax)
    
def starter_conditions():
    xmin = -3
    xmax = 2
    ymin = -1.5
    ymax = 1.5
    max_iter = 200
    return xmin, xmax, ymin, ymax, max_iter

def draw_coordinates(xmin, xmax, ymin, ymax):
    coords = f"({np.round(xmin, decimals=4)} , {np.round(xmax, decimals=4)}), ({np.round(ymin, decimals=4)} , {np.round(ymax, decimals=4)})i"
    colour = (255, 233, 214)
    font = pygame.font.Font(None, 30)
    location = (20, 10)
    screen.blit(font.render(coords, True, colour), location)
    return()

#GRAPHIC

colormaps = [((72, 3, 85),(118, 153, 212),(99, 180, 209),(144, 252, 249), (253, 45, 91)), ((60, 55, 68),(9, 12, 155),(61, 82, 213),(180, 197, 228), (251, 255, 241)), ((130, 2, 99),(255, 251, 252),(98, 187, 193),(236, 5, 142))]

def main():
    #Start conditions
    paletteiter = 0
    xmin, xmax, ymin, ymax, max_iter = starter_conditions()
    palette = palette_gen(colormaps[0], max_iter)
    graph_mandelbrot(xmin, xmax, ymin, ymax, palette, max_iter)
    draw_coordinates(xmin, xmax, ymin, ymax)
    run = True
    while run:
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                px,py = pygame.mouse.get_pos()
                if event.button == 1:
                    zoom_factor = 3
                    xmin, xmax, ymin, ymax = zoom(px,py,xmin,xmax,ymin,ymax,zoom_factor)
                    graph_mandelbrot(xmin, xmax, ymin, ymax, palette, max_iter)
                    draw_coordinates(xmin, xmax, ymin, ymax)
                elif event.button == 3:
                    zoom_factor = 1/3
                    xmin, xmax, ymin, ymax = zoom(px,py,xmin,xmax,ymin,ymax,zoom_factor)
                    graph_mandelbrot(xmin, xmax, ymin, ymax, palette, max_iter)
                    draw_coordinates(xmin, xmax, ymin, ymax)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    xmin, xmax, ymin, ymax, max_iter = starter_conditions()
                    graph_mandelbrot(xmin, xmax, ymin, ymax, palette, max_iter)
                    draw_coordinates(xmin, xmax, ymin, ymax)
                if event.key == pygame.K_s:
                    pygame.image.save(screen,"screenshot.png")
                if event.key == pygame.K_c:
                    if paletteiter < len(colormaps)-1:
                        paletteiter += 1
                        palette = palette_gen(colormaps[paletteiter], max_iter)
                        graph_mandelbrot(xmin, xmax, ymin, ymax, palette, max_iter)
                        draw_coordinates(xmin, xmax, ymin, ymax)
                    else:
                        paletteiter = 0
                        palette = palette_gen(colormaps[paletteiter], max_iter)
                        graph_mandelbrot(xmin, xmax, ymin, ymax, palette, max_iter)
                        draw_coordinates(xmin, xmax, ymin, ymax)
                if event.key == pygame.K_i:
                    max_iter = int(input("New iterations: "))
                    palette = palette_gen(colormaps[paletteiter], max_iter)
                    graph_mandelbrot(xmin, xmax, ymin, ymax, palette, max_iter)
            pygame.display.update()

main()