import D3

#a singular point on a mesh
class Vertice:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.screenPos = [int(x + D3.WIDTH/2), int(z + D3.HEIGHT/2)]

    #project point onto screen
    def calculateScreenPos(self, projection):
        #project including perspective
        if projection == "persp":
            pass
        #project without perspective
        if projection == "ortho":
            self.screenPos[0] = int(self.x + D3.WIDTH/2)
            self.screenPos[1] = int(self.z + D3.HEIGHT/2)

    def display(self, camera):
        self.calculateScreenPos(camera.projection)
        D3.pg.draw.circle(D3.SCREEN, (255, 255, 255), self.screenPos, 2, 0)

    def get_pos(self):
        return self.x, self.y, self.z
    def set_pos(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def get_screenPos(self):
        return self.screenPos
    def set_screenPos(self, x, y):
        self.screenPos[0] = x
        self.screenPos[1] = y

#connects 2 verts
class Edge:
    def __init__(self, startVert, endVert):
        self.startVert = startVert
        self.endVert = endVert
    def display(self):
        D3.pg.draw.line(D3.SCREEN, (200, 200, 200), self.startVert.get_screenPos(), self.endVert.get_screenPos(), 1)

#makes a face out of 3 verts
class Tri:
    def __init__(self, vert1, vert2, vert3):
        self.vert1 = vert1
        self.vert2 = vert2
        self.vert3 = vert3

from D3 import objects

#general mesh object, contains vertices, edges, and faces
class Mesh(objects.Object):
    def __init__(self, x, y, z, xrot, yrot, zrot):
        super().__init__(x, y, z, xrot, yrot, zrot)
        self.vertices = []
        self.edges = []
        self.faces = []
    def display(self, camera):
        for edge in self.edges:
            edge.display()
        for vert in self.vertices:
            vert.display(camera)

from D3.objects.mesh import Cube

Cube = Cube.Cube