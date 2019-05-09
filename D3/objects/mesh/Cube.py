from D3.objects import mesh

class Cube(mesh.Mesh):
    def __init__(self, x, y, z, xrot, yrot, zrot):
        super().__init__(x, y, z, xrot, yrot, zrot)

        for X in [-100, 100]:
            for Y in [-100, 100]:
                for Z in [-100, 100]:
                    self.vertices.append(mesh.Vertice(X, Y, Z))

        self.edges.append(mesh.Edge(self.vertices[0], self.vertices[1]))
        self.edges.append(mesh.Edge(self.vertices[0], self.vertices[2]))
        self.edges.append(mesh.Edge(self.vertices[0], self.vertices[4]))
        self.edges.append(mesh.Edge(self.vertices[3], self.vertices[1]))
        self.edges.append(mesh.Edge(self.vertices[3], self.vertices[2]))
        self.edges.append(mesh.Edge(self.vertices[3], self.vertices[7]))
        self.edges.append(mesh.Edge(self.vertices[6], self.vertices[4]))
        self.edges.append(mesh.Edge(self.vertices[6], self.vertices[7]))
        self.edges.append(mesh.Edge(self.vertices[6], self.vertices[2]))
        self.edges.append(mesh.Edge(self.vertices[5], self.vertices[1]))
        self.edges.append(mesh.Edge(self.vertices[5], self.vertices[7]))
        self.edges.append(mesh.Edge(self.vertices[5], self.vertices[4]))