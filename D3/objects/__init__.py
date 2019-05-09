class Object:
    def __init__(self, x, y, z, xrot, yrot, zrot):
        self.x = x
        self.y = y
        self.z = z
        self.xrot = xrot
        self.yrot = yrot
        self.zrot = zrot
    def display(self, camera):
        pass

import D3.objects.mesh, D3.objects.camera