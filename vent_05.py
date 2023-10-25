from guizero import App, Text, TextBox, PushButton, Box

calif = []  

def calcular_aprobados():
    global calif  
    try:
        calif_str = calif_box.value
        calif = [float(cal) for cal in calif_str.split()]

        if all(0 <= cal <= 10 for cal in calif):
           aprobados = sum(1 for cal in calif if cal >= 7)
           resultado.value = f"los alumnos que pasaron son: {aprobados}"
        else:
            resultado.value = "ingresa calificaciones válidas"

    except ValueError:
        resultado.value = "ingresa calificaciones válidas."


app = App("contador de alumnos que aprobaron", width=500)

Text(app, "ingresa las calificaciones:")
calif_box = TextBox(app, width=40)
Text(app, "(separa los valores con espacios)")
boton_calcular = PushButton(app, text="calcular", command=calcular_aprobados)
resultado = Text(app, "")

app.display()