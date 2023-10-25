from guizero import App, Text, TextBox, PushButton

def generar_cuadrado():
    try:
        numero = int(name.value)

        if numero >= 1:
            resultado = numero ** 2
            message_cuadrado.value = f"el cuadrado es: {resultado}"
        else:
            message_cuadrado.value = "ingresa valores iguales o mayores a uno" 

    except ValueError:
        message_cuadrado.value = "Ingresa un número válido."  

app = App(title="calcular cuadrado")

message = Text(app, text="dame un número")
name = TextBox(app, width=20)
button = PushButton(app, text="calcular", command=generar_cuadrado)
message_cuadrado = Text(app, text="")

app.display()

