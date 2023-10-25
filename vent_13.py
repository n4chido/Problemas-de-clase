from guizero import App, PushButton, Text

def toggle_flag_and_print():
    global x
    if x == 0:
        x = 1
    else:
        x = 0
    resultado.value += str(x)

x = 0

app = App("Serie 101010")
boton_imprimir = PushButton(app, text="imprimir", command=toggle_flag_and_print)
resultado = Text(app, text="serie: ")  # Usar Text en lugar de PushButton

app.display()