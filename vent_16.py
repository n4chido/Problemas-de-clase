from guizero import App, Combo, TextBox, PushButton, Text

def realizar_operacion():
    operacion = combo_operacion.value
    numero1 = float(entrada_numero1.value)
    numero2 = float(entrada_numero2.value)

    if operacion == "suma":
        resultado.value = f"el resultado es: {numero1 + numero2}"
    elif operacion == "resta":
        resultado.value = f"el resultado es: {numero1 - numero2}"
    elif operacion == "multiplicacion":
        resultado.value = f"el resultado es: {numero1 * numero2}"
    elif operacion == "dividision":
        if numero2 != 0:
            resultado.value = f"el resultado es: {numero1 / numero2}"
        else:
            resultado.value = "no se puede dividir por cero."

app = App("calculadora")
Text(app, "selecciona la operación que realizaras:")
combo_operacion = Combo(app, options=["suma", "resta", "multiplicacion", "dividision"])
Text(app, "ingresa el primer valor:")
entrada_numero1 = TextBox(app)
Text(app, "ingresa el segundo valor:")
entrada_numero2 = TextBox(app)
boton_calcular = PushButton(app, text="calcular", command=realizar_operacion)
resultado = Text(app, "resultado:")

app.display()
