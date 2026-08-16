class Restaurante:

    def __init__(self):
        self.productos = []
        self.clientes = []

    # PRODUCTOS
    def registrar_producto(self, producto):
        self.productos.append(producto)

    def listar_productos(self):
        if len(self.productos) == 0:
            print("No hay productos registrados.")
        else:
            for producto in self.productos:
                producto.mostrar_informacion()

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                producto.mostrar_informacion()
                return

        print("Producto no encontrado.")

    # CLIENTES
    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def listar_clientes(self):
        if len(self.clientes) == 0:
            print("No hay clientes registrados.")
        else:
            for cliente in self.clientes:
                print("----------------------")
                print("Nombre:", cliente.nombre)
                print("Correo:", cliente.correo)
                print("ID:", cliente.id_cliente)

    def buscar_cliente(self, id_cliente):
        for cliente in self.clientes:
            if cliente.id_cliente == id_cliente:
                print("----------------------")
                print("Nombre:", cliente.nombre)
                print("Correo:", cliente.correo)
                print("ID:", cliente.id_cliente)
                return

        print("Cliente no encontrado.")