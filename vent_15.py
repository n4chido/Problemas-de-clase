from guizero import App, Combo, PushButton, Text

productos_vendidos = []

def agregar_producto():
    producto = combo_productos.value
    productos_vendidos.append(producto)
    resultado.value += f"{producto}\n"

app = App("ventas de branko")
Text(app, "seleccione el producto vendido:")
combo_productos = Combo(app, options=["Torta", "Taco", "Hotdog", "Pizza"])
boton_agregar = PushButton(app, text="Agregar", command=agregar_producto)
resultado = Text(app, "los productos vendidos fueron:\n")

app.display()