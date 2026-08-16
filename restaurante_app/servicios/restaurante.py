from typing import List, Optional, Set

from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:
    """Administra los productos y usuarios del restaurante."""

    def __init__(self) -> None:
        # LISTAS: almacenan las colecciones dinámicas de objetos.
        self.productos: List[Producto] = []
        self.usuarios: List[Usuario] = []

    # ==========================================================
    # PRODUCTOS
    # ==========================================================

    def registrar_producto(self, producto: Producto) -> bool:
        """Registra un producto evitando códigos duplicados."""

        if self.buscar_producto(producto.codigo) is not None:
            return False

        self.productos.append(producto)
        return True

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        """Busca un producto mediante su código."""

        for producto in self.productos:
            if producto.codigo.lower() == codigo.lower():
                return producto

        return None

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float
    ) -> bool:
        """Actualiza la información de un producto."""

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        producto.nombre = nombre
        producto.categoria = categoria
        producto.precio = precio

        return True

    def eliminar_producto(self, codigo: str) -> bool:
        """Elimina un producto mediante su código."""

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        self.productos.remove(producto)
        return True

    def listar_productos(self) -> List[Producto]:
        """Devuelve la lista de productos registrados."""

        return self.productos.copy()

    # ==========================================================
    # USUARIOS
    # ==========================================================

    def registrar_usuario(self, usuario: Usuario) -> bool:
        """Registra un usuario evitando identificaciones duplicadas."""

        if self.buscar_usuario(usuario.identificacion) is not None:
            return False

        self.usuarios.append(usuario)
        return True

    def buscar_usuario(self, identificacion: str) -> Optional[Usuario]:
        """Busca un usuario por su identificación."""

        for usuario in self.usuarios:
            if usuario.identificacion == identificacion:
                return usuario

        return None

    def listar_usuarios(self) -> List[Usuario]:
        """Devuelve la lista de usuarios registrados."""

        return self.usuarios.copy()

    # ==========================================================
    # CATEGORÍAS
    # ==========================================================

    def obtener_categorias(self) -> Set[str]:
        """
        Obtiene las categorías únicas de los productos.

        SET se utiliza para evitar categorías repetidas.
        """

        categorias: Set[str] = {
            producto.categoria
            for producto in self.productos
        }

        return categorias
