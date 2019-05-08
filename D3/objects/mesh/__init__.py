import D3

class Vertice:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.screenPos = [int(x),int(z)]
    def display(self):
        D3.pg.draw.circle(D3.screen, (255, 255, 255), self.screenPos, 2, 0)

class Edge:
    def __init__(self, startVert, endVert):
        self.startVert = startVert
        self.endVert = endVert

class Tri:
    def __init__(self, vert1, vert2, vert3):
        self.vert1 = vert1
        self.vert2 = vert2
        self.vert3 = vert3

from D3 import objects

class Mesh(objects.Object):
    def __init__(self, x, y, z, xrot, yrot, zrot):
        super().__init__(x, y, z, xrot, yrot, zrot)
        self.vertices = []
        self.edges = []
        self.faces = []
    def display(self):
        for vert in self.vertices:
            vert.display()

from D3.objects.mesh import Cube

Cube = Cube.Cube