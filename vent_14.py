from guizero import App, Text, TextBox, PushButton

def determinar_dia_semana():
    try:
        numero = int(entrada_numero.value)
        if 1 <= numero <= 7:
            dias_semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "pomingo"]
            dia = dias_semana[numero - 1]
            resultado.value = f"ese día de la semana cae en: {dia}"
        else:
            resultado.value = "ingresa un número entre 1 y 7"
    except ValueError:
        resultado.value = "error"

app = App("dia de la semana")
Text(app, "ingresa un número:")
entrada_numero = TextBox(app, width=20)
Text(app, "(1 para lunes, 2 para martes, etc.)")
boton_determinar = PushButton(app, text="Determinar", command=determinar_dia_semana)
resultado = Text(app, "")

app.display()
