
import struct
import sys
from collections import namedtuple

V2 = namedtuple('Point2', ['x', 'y'])

def char(c):
    # 1 byte
    return struct.pack('=c', c.encode('ascii'))

def word(w):
    # 2 bytes
    return struct.pack('=h', w)

def dword(d):
    # 4 bytes
    return struct.pack('=l', d)

def color(r, g, b):
    
    return bytes([int(b * 255),
                  int(g * 255),
                  int(r * 255)])

class Renderer(object):
    def __init__(self, width, height):
        sys.setrecursionlimit(20000)
        self.width = width
        self.height = height

        # es el color que quiero de fondo
        self.clearColor = color(0, 0, 0)

        self.currColor = color(1 ,1 ,1)

        self.glViewport(0, 0, self.width, self.height)

        self.glClear()

    def glViewport(self, posX, posY, width, height):
        self.vpX = posX
        self.vpY = posY
        self.vpWidth = width
        self.vpHeight = height

    def glClearColor(self, r, g, b):
        self.clearColor = color(r, g, b)

    def glColor(self, r, g, b):
        self.currColor = color(r, g, b)

    def glClear(self):
        # aca se guardara el array de pixeles
        self.pixels = [[ self.clearColor for y in range(self.height) ]
                       for x in range(self.width)]


    def glClearViewport(self, clr = None):
        for x in range(self.vpX, self.vpX + self.vpWidth):
            for y in range(self.vpY, self.vpY + self.vpHeight):
                self.glPoint(x, y, clr)

    def glPoint(self, x, y, clr = None):
        if (0 <= x < self.width) and (0 <= y < self.height):
            self.pixels[x][y] = clr or self.currColor


    def glPoint_vp(self, ndcX,  ndcY, clr = None):
        x = (ndcX + 1) * (self.vpWidth / 2) + self.vpX
        y = (ndcY + 1) * (self.vpHeight / 2) + self.vpY

        x = int(x)
        y = int(y)

        self.glPoint(x ,y, clr)

    def glLine(self, v0, v1, clr = None):
        # Bresenham line algorithm
        # y = m * x + b

        x0 = int(v0.x)
        x1 = int(v1.x)
        y0 = int(v0.y)
        y1 = int(v1.y)

        if x0 == x1 and y0 == y1:
            self.glPoint(x0, y0, clr)
            return

        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        steep = dy > dx

        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1

        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        offset = 0
        limit = 0.5
        m = dy /dx
        y = y0

        for x in range(x0, x1 + 1):
            if steep:
                self.glPoint(y, x, clr)

            else:
                self.glPoint(x, y, clr)

            offset += m

            if offset >= limit:
                if y0 < y1:
                    y += 1
                else:
                    y -= 1

                limit += 1


    def makeBorder(self, fig, clr = None):
        for i in range(len(fig)):
            self.glLine(fig[i], fig[( i+ 1) % len(fig)], clr)


    def glFlood(self, fig, x, y, clrBg = None, clrIn = None):

        if (self.pixels[x][y] == clrBg):

            self.glPoint(x, y, clrIn)
            # Basandose en el algoritmo de Flood Fill y utilizando Depth-first search
            self.glFlood(fig, x - 1, y, clrBg, clrIn)  # pixel hacia arriba
            self.glFlood(fig, x + 1, y, clrBg, clrIn)  # pixel hacia abajo
            self.glFlood(fig, x, y - 1, clrBg, clrIn)  # pixel hacia la izquierda
            self.glFlood(fig, x, y + 1, clrBg, clrIn)  # pixel hacia la derecha


    def glFill(self, fig, clrBg=None, clrIn=None):

        # Obteniendo puntos en x & y
        pointsX = [f.x for f in fig]
        pointsY = [f.y for f in fig]

        # Cordenada de puntos x & y para comenzar en el centro
        startX = int(min(pointsX) + ((max(pointsX) - min(pointsX)) / 2))
        startY = int(min(pointsY) + ((max(pointsY) - min(pointsY)) / 2))
        
        self.glFlood(fig, startX, startY, clrBg, clrIn)

    def glFinish(self, filename):
        with open(filename, "wb") as file:

            # Header
            file.write(bytes('B'.encode('ascii')))
            file.write(bytes('M'.encode('ascii')))
            file.write(dword(14 + 40 + (self.width * self.width * 3)))
            file.write(dword(0))
            file.write(dword(14 + 40))

            # InfoHeader
            file.write(dword(40))
            file.write(dword(self.width))
            file.write(dword(self.height))
            file.write(word(1))
            file.write(word(24))
            file.write(dword(0))
            file.write(dword(self.width * self.height * 3))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))

            # Color table
            for y in range(self.height):
                for x in range(self.width):
                    file.write(self.pixels[x][y])






