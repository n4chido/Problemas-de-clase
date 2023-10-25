from guizero import App, Text, TextBox, PushButton

numeros = []

def calcular_suma_cuadrados():
    try:
        numero = int(textbox.value)
        cuadrado = numero ** 2
        numeros.append(cuadrado)
        resultado_text.value = f"el cuadrado es: {cuadrado}"
        suma_text.value = f"sumatoria de cuadrados ingresados: {sum(numeros)}"
    except ValueError:
        resultado_text.value = "ingresa un número válido"

app = App("suma de Cuadrados")

Text(app, "ingresa un número:")
textbox = TextBox(app)
PushButton(app,text= "calcular", command=calcular_suma_cuadrados)
resultado_text = Text(app, "")
suma_text = Text(app, "suma de cuadrados: 0")

app.display()