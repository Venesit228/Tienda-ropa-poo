class Producto:
    def __init__(self, codigo: str, nombre: str, categoria, precio, stock: int) -> None:
        self.codigo: str = codigo
        self.nombre: str = nombre
        self.datos_basicos: tuple = (categoria, precio)
        self.stock: int = stock

    def obtener_categoria(self):
        return self.datos_basicos[0]

    def obtener_precio(self):
        return self.datos_basicos[1]

    def aumentar_stock(self, cantidad: int):
        if cantidad > 0:
            self.stock += cantidad

    def disminuir_stock(self, cantidad: int):
        if cantidad > 0 and cantidad <= self.stock:
            self.stock -= cantidad
            return True
        return False

    def mostrar_informacion(self):
        return f"Codigo: {self.codigo}, Nombre: {self.nombre}, Categoria: {self.obtener_categoria()}, Precio: ${self.obtener_precio():.2f}, Stock: {self.stock}"
# holaaaaa

class Inventario:
    def __init__(self, nombre_tienda: str):
        self.nombre_tienda: str = nombre_tienda
        self.productos = []
        self.resumen_categorias = {}

    def agregar_producto(self, producto):
        for p in self.productos:
            if p.codigo == producto.codigo:
                print("Ya existe un producto con este codigo.")
                return p
        self.productos.append(producto)

    def buscar_producto_por_codigo(self, codigo: str):
        for p in self.productos:
            if p.codigo == codigo:
                return p
        return None
    def buscar_por_nombre(self, nombre):
    resultados = []
    for p in self.productos:
        if nombre in p.nombre:
            resultados.append(p)
    return resultados

def eliminar_producto(self, codigo):
    for i in range(len(self.productos)):
        if self.productos[i].codigo == codigo:
            del self.productos[i]
            return True
    return False

def producto_mas_caro(self):
    if len(self.productos) == 0:
        return None
    mas_caro = self.productos[0]
    for p in self.productos:
        if p.obtener_precio() > mas_caro.obtener_precio():
            mas_caro = p
    return mas_caro

    def listar_productos(self):
        lista = []
        for p in self.productos:
            lista.append(p.mostrar_informacion())
        return lista

    def mostrar_productos_por_categoria(self, categoria):
        lista = []
        for p in self.productos:
            if p.obtener_categoria() == categoria:
                lista.append(p.mostrar_informacion())
        return lista

    def actualizar_resumen_categorias(self):
        self.resumen_categorias = {}
        for p in self.productos:
            categoria = p.obtener_categoria()
            if categoria in self.resumen_categorias:
                self.resumen_categorias[categoria] += 1
            else:
                self.resumen_categorias[categoria] = 1

    def mostrar_resumen_categorias(self):
        self.actualizar_resumen_categorias()
        lista = []
        for categoria, cantidad in self.resumen_categorias.items():
            lista.append(f"{categoria}: {cantidad}")
        return lista


inventario = Inventario("Mi Tienda de Ropa")

while True:
    print("\n===== MENU INVENTARIO =====")
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Buscar producto por codigo")
    print("4. Mostrar productos por categoria")
    print("5. Mostrar resumen de categorias")
    print("6. Aumentar stock de un producto")
    print("7. Disminuir stock de un producto")
    print("8. Salir")
    print("9.  Buscar producto por nombre")
    print("10. Eliminar producto")
    print("11. Mostrar producto mas caro")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        codigo = input("Codigo: ")
        nombre = input("Nombre: ")
        categoria = input("Categoria: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))
        producto = Producto(codigo, nombre, categoria, precio, stock)
        inventario.agregar_producto(producto)
        print("Producto agregado correctamente.")

    elif opcion == "2":
        productos = inventario.listar_productos()
        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            for p in productos:
                print(p)

    elif opcion == "3":
        codigo = input("Ingrese el codigo del producto: ")
        producto = inventario.buscar_producto_por_codigo(codigo)
        if producto != None:
            print(producto.mostrar_informacion())
        else:
            print("Producto no encontrado.")

    elif opcion == "4":
        categoria = input("Ingrese la categoria: ")
        productos = inventario.mostrar_productos_por_categoria(categoria)
        if len(productos) == 0:
            print("No hay productos en esta categoria.")
        else:
            for p in productos:
                print(p)

    elif opcion == "5":
        resumen = inventario.mostrar_resumen_categorias()
        if len(resumen) == 0:
            print("No hay productos registrados.")
        else:
            for linea in resumen:
                print(linea)

    elif opcion == "6":
        codigo = input("Codigo del producto: ")
        cantidad = int(input("Cantidad a aumentar: "))
        producto = inventario.buscar_producto_por_codigo(codigo)
        if producto != None:
            producto.aumentar_stock(cantidad)
            print("Stock actualizado.")
        else:
            print("Producto no encontrado.")

    elif opcion == "7":
        codigo = input("Codigo del producto: ")
        cantidad = int(input("Cantidad a disminuir: "))
        producto = inventario.buscar_producto_por_codigo(codigo)
        if producto != None:
            if producto.disminuir_stock(cantidad):
                print("Stock actualizado.")
            else:
                print("No hay suficiente stock.")
        else:
            print("Producto no encontrado.")

    elif opcion == "8":
        print("Saliendo del sistema...")
        break

    else:
        print("Opcion invalida. Intente nuevamente.")
    
    elif opcion == "9":
        nombre = input("Ingrese el nombre del producto: ")
        resultados = inventario.buscar_por_nombre(nombre)
        if len(resultados) == 0:
            print("No se encontraron productos con ese nombre.")
        else:
            for p in resultados:
                print(p.mostrar_informacion())
    
    elif opcion == "10":
        codigo = input("Codigo del producto a eliminar: ")
        if inventario.eliminar_producto(codigo):
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")
    
    elif opcion == "11":
        producto = inventario.producto_mas_caro()
        if producto != None:
            print("Producto mas caro:")
            print(producto.mostrar_informacion())
        else:
            print("No hay productos registrados.")
