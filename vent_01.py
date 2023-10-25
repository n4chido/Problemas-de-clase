from guizero import App, Text, TextBox, PushButton

def suma():
    try:
        num1 = int(n1.value)
        num2 = int(n2.value)
        num3 = int(n3.value)
        if num1 >= 0 and num2 >= 0 and num3 >= 0:

          resultado = num1 + num2 + num3
          salida_suma.value = f"La suma es: {resultado}"

        else:
          salida_suma.value = "ingresa valores iguales o mayores a cero"

    except ValueError:
        salida_suma.value = "Error"

app = App(title="Suma de 3 números")

message = Text(app, text="dame 3 números enteros")
n1 = TextBox(app, width=20)
n2 = TextBox(app, width=20)
n3 = TextBox(app, width=20)

button = PushButton(app, text="Suma", command=suma)
salida_suma = Text(app, text="")

app.display()

