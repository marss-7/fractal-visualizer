import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

x = sp.symbols('x')

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

def palette_gen(colors, max_iterations):
    palette = []
    R = []
    G = []
    B = []
    for i in colors:
        R.append(i[0])
        G.append(i[1])
        B.append(i[2])

    points = np.linspace(0,max_iterations, len(colors))

    Rf = mylagrange(points, R)
    Gf = mylagrange(points, G)
    Bf = mylagrange(points, B)

    functR = sp.lambdify(x, Rf, 'numpy')
    functG = sp.lambdify(x, Gf, 'numpy')
    functB = sp.lambdify(x, Bf, 'numpy')

    indexlist = np.linspace( 0, max_iterations, max_iterations)

    goodR = functR(indexlist)
    goodG = functG(indexlist)
    goodB = functB(indexlist)

    for i in range(len(goodR)):
        palette.append([goodR[i], goodG[i], goodB[i]])
    palette.append((0,0,0))
    palette = np.clip(palette, 0, 255).astype(np.uint8)
    return(palette)


colores = [(144, 252, 249),(99, 180, 209),(118, 153, 212),(148, 72, 188),(72, 3, 85),(0,0,0)]