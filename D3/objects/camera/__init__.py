import D3
from D3 import objects

class Camera(objects.Object):
    def __init__(self, x, y, z, xrot, yrot, zrot, width, height):
        super().__init__(x, y, z, xrot, yrot, zrot)
        self.width = width
        self.height = height
        self.projection = "ortho"
    def project(self, objects):
        for object in objects:
            object.display(self)