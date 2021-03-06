import D3
from D3 import objects

class Camera(objects.Object):
    def __init__(self, x, y, z, xrot, yrot, zrot, width, height, fov, startDist, endDist):
        super().__init__(x, y, z, xrot, yrot, zrot)
        self.width = width
        self.height = height
        self.projection = "persp"
        self.fov = fov
        self.startDist = startDist
        self.endDist = endDist
        self.aspectRatio = self.width/self.height

        D3.calculate.plane([1, 2, 3], [2, 3, 2], [4, 5, 1])

    def project(self, objects):
        for object in objects:
            object.display(self)