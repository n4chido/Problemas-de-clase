from guizero import App, Box, Text, TextBox, PushButton

def calcular_suma():
    numeros = entrada_numeros.value.split()
    if len(numeros) != 5:
        resultado.value = "ingresa valores validos"
        return

    suma = 0
    for numero in numeros:
        try:
            num = int(numero)
            if 5 <= num <= 10:
                suma += num
            else:
                resultado.value = "ingresa numeros entre 5 y 10"
                return
        except ValueError:
            resultado.value = "error"
            return

    resultado.value = f"la suma de los numeros es: {suma}"

app = App("suma de numeros entre 5 y 10")
instruccion = Text(app, "ingresa 5 numeros entre 5 y 10 separados por espacios:")
entrada_numeros = TextBox(app, width=40)
boton_calcular = PushButton(app, text="Calcular", command=calcular_suma)
resultado = Text(app, "")

app.display()
