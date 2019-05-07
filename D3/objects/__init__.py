class Object:
    def __init__(self, x, y, z, xrot, yrot, zrot):
        self.x = x
        self.y = y
        self.z = z
        self.xrot = xrot
        self.yrot = yrot
        self.zrot = zrot

class Mesh(Object):
    def __init__(self, x, y, z, xrot, yrot, zrot):
        super().__init__(x, y, z, xrot, yrot, zrot)

import D3.objects.mesh