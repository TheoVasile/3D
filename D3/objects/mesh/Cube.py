from D3.objects import mesh

class Cube(mesh.Mesh):
    def __init__(self, x, y, z, xrot, yrot, zrot):
        super().__init__(x, y, z, xrot, yrot, zrot)

        for X in [-100, 100]:
            for Y in [-100, 100]:
                for Z in [-100, 100]:
                    self.vertices.append(mesh.Vertice(X, Y, Z))
