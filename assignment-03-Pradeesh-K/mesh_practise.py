from compas.datastructures import Mesh  #easier for constructing large meshes
#obj files include the vertex and connectivity data
import os
#functionalities to interact with OS, create file path
HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, "data")
FILE = os.path.join(DATA, "faces.obj")

mesh = Mesh.from_obj(FILE)

