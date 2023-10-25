from guizero import App, PushButton, Text

def calcular_suma_cuadrados_pares():
    suma = 0
    for num in range(2, 21, 2): 
        suma += num ** 2
    resultado.value = f"la suma de todos los cuadrados de los pares de 0 a 20 ess: {suma}"

app = App("suma de cuadrados ")
texto_instruccion = Text(app, "Presiona aqui")
boton_calcular = PushButton(app, text="Calcular", command=calcular_suma_cuadrados_pares)
resultado = Text(app, "")

app.display()


