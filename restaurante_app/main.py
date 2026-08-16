from typing import Callable, Dict, Tuple

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante


restaurante = Restaurante()


# ==========================================================
# FUNCIONES PARA PRODUCTOS
# ==========================================================

def registrar_producto() -> None:
    """Solicita los datos y registra un producto."""

    print("\n--- REGISTRAR PRODUCTO ---")

    codigo = input("Código: ").strip()
    nombre = input("Nombre: ").strip()
    categoria = input("Categoría: ").strip()

    if not codigo or not nombre or not categoria:
        print("Error: todos los campos son obligatorios.")
        return

    try:
        precio = float(input("Precio: "))

        if precio < 0:
            print("Error: el precio no puede ser negativo.")
            return

    except ValueError:
        print("Error: el precio debe ser un número válido.")
        return

    producto = Producto(
        codigo,
        nombre,
        categoria,
        precio
    )

    if restaurante.registrar_producto(producto):
        print("Producto registrado correctamente.")
    else:
        print("Error: ya existe un producto con ese código.")


def buscar_producto() -> None:
    """Busca un producto mediante su código."""

    print("\n--- BUSCAR PRODUCTO ---")

    codigo = input("Ingrese el código del producto: ").strip()

    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("Producto no encontrado.")
    else:
        print("\nProducto encontrado:")
        print(producto)


def actualizar_producto() -> None:
    """Actualiza los datos de un producto."""

    print("\n--- ACTUALIZAR PRODUCTO ---")

    codigo = input("Ingrese el código del producto: ").strip()

    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("Producto no encontrado.")
        return

    print(f"Producto actual: {producto}")

    nombre = input("Nuevo nombre: ").strip()
    categoria = input("Nueva categoría: ").strip()

    if not nombre or not categoria:
        print("Error: los campos no pueden estar vacíos.")
        return

    try:
        precio = float(input("Nuevo precio: "))

        if precio < 0:
            print("Error: el precio no puede ser negativo.")
            return

    except ValueError:
        print("Error: el precio debe ser un número válido.")
        return

    actualizado = restaurante.actualizar_producto(
        codigo,
        nombre,
        categoria,
        precio
    )

    if actualizado:
        print("Producto actualizado correctamente.")
    else:
        print("No fue posible actualizar el producto.")


def eliminar_producto() -> None:
    """Elimina un producto."""

    print("\n--- ELIMINAR PRODUCTO ---")

    codigo = input("Ingrese el código del producto: ").strip()

    eliminado = restaurante.eliminar_producto(codigo)

    if eliminado:
        print("Producto eliminado correctamente.")
    else:
        print("Producto no encontrado.")


def listar_productos() -> None:
    """Muestra todos los productos registrados."""

    print("\n--- LISTA DE PRODUCTOS ---")

    productos = restaurante.listar_productos()

    if not productos:
        print("No existen productos registrados.")
        return

    for producto in productos:
        print(producto)


# ==========================================================
# FUNCIONES PARA USUARIOS
# ==========================================================

def registrar_usuario() -> None:
    """Solicita los datos y registra un usuario."""

    print("\n--- REGISTRAR USUARIO ---")

    identificacion = input("Identificación: ").strip()
    nombre = input("Nombre: ").strip()
    correo = input("Correo: ").strip()

    if not identificacion or not nombre or not correo:
        print("Error: todos los campos son obligatorios.")
        return

    if "@" not in correo:
        print("Error: ingrese un correo electrónico válido.")
        return

    usuario = Usuario(
        identificacion,
        nombre,
        correo
    )

    if restaurante.registrar_usuario(usuario):
        print("Usuario registrado correctamente.")
    else:
        print("Error: ya existe un usuario con esa identificación.")


def listar_usuarios() -> None:
    """Muestra todos los usuarios registrados."""

    print("\n--- LISTA DE USUARIOS ---")

    usuarios = restaurante.listar_usuarios()

    if not usuarios:
        print("No existen usuarios registrados.")
        return

    for usuario in usuarios:
        print(usuario)


# ==========================================================
# CATEGORÍAS
# ==========================================================

def mostrar_categorias() -> None:
    """Muestra las categorías únicas de los productos."""

    print("\n--- CATEGORÍAS DE PRODUCTOS ---")

    categorias = restaurante.obtener_categorias()

    if not categorias:
        print("No existen categorías registradas.")
        return

    for categoria in sorted(categorias):
        print(f"- {categoria}")


# ==========================================================
# MENÚ PRINCIPAL
# ==========================================================

# TUPLA: representa las opciones estables del menú.
OPCIONES_MENU: Tuple[str, ...] = (
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9"
)


def mostrar_menu() -> None:
    """Muestra el menú principal del sistema."""

    print("\n")
    print("=" * 40)
    print("        SISTEMA DE RESTAURANTE")
    print("=" * 40)
    print("1. Registrar producto")
    print("2. Buscar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Listar productos")
    print("----------------------------------------")
    print("6. Registrar usuario")
    print("7. Listar usuarios")
    print("----------------------------------------")
    print("8. Mostrar categorías")
    print("9. Salir")
    print("=" * 40)


def ejecutar_menu() -> None:
    """Ejecuta el menú principal del sistema."""

    # DICCIONARIO: relaciona cada opción con la función correspondiente.
    acciones_menu: Dict[str, Callable[[], None]] = {
        "1": registrar_producto,
        "2": buscar_producto,
        "3": actualizar_producto,
        "4": eliminar_producto,
        "5": listar_productos,
        "6": registrar_usuario,
        "7": listar_usuarios,
        "8": mostrar_categorias
    }

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ").strip()

        if opcion not in OPCIONES_MENU:
            print("Error: seleccione una opción válida del menú.")
            continue

        if opcion == "9":
            print("\nGracias por utilizar el sistema de restaurante.")
            break

        accion = acciones_menu.get(opcion)

        if accion is not None:
            try:
                accion()
            except Exception as error:
                print(f"Ocurrió un error inesperado: {error}")


if __name__ == "__main__":
    ejecutar_menu()
