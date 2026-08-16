from ast import List

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario


class Restaurante:

    def __init__(self) -> None:
        self.productos: List[Producto] = []
        self.usuarios: List[Usuario] = []
