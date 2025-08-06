import pygame
import numpy as np
import sympy as sp
x = sp.symbols('x')

# Initialise pygame

def mylagrange(xlist, ylist):
    Pn = 0
    s = 0
    for i in xlist:
      Ln = 1
      for m in xlist:
          if m != i:
              L = ((x-m))/((i- m))
              Ln = Ln * L
      Pn = Pn + Ln*ylist[s]
      s +=1
    return sp.simplify(Pn)




#Defnimos unas cosiiitas

# Create the game window
width = 800
height = 800
screen = pygame.display.set_mode((width, height))

xmin = -2
xmax = 1
ymin = -1.5
ymax = 1.5
max_iter = 100
z0 = 0

xrange = np.linspace(xmin, xmax, 800)
yrange = np.linspace(ymin, ymax, 800)

colores = [(122, 156, 210),(133, 113, 200),(141, 93, 194),(148, 72, 188),(72, 3, 85),(0,0,0)]
R = []
G = []
B = []
for i in colores:
  R.append(i[0])
  G.append(i[1])
  B.append(i[2])

minindex = 0
xlista = np.linspace(minindex, max_iter, 6)

Rf = mylagrange(xlista, R)
Gf = mylagrange(xlista, G)
Bf = mylagrange(xlista, B)

functR = sp.lambdify(x, Rf, 'numpy')
functG = sp.lambdify(x, Gf, 'numpy')
functB = sp.lambdify(x, Bf, 'numpy')

rangex = np.linspace( 0, max_iter, max_iter)
goodR = functR(rangex)
goodG = functG(rangex)
goodB = functB(rangex)

palette = []
for i in range(len(goodR)):
  palette.append([goodR[i], goodG[i], goodB[i]])

palette = np.clip(palette, 0, 255).astype(np.uint8)

def mandelbrot(x, y):
    iter = 0
    z = 0
    c = complex(x, y)
    while iter < max_iter:
        if abs(z) > 2:
            return(palette[iter-1])
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