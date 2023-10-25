from guizero import App, Text, TextBox, PushButton

def suma():
    try:
        n1 = int(a_ac.value)
        n2 = int(a_nac.value)
        
        if n1 >= 0 and n2 >= 0:
          
            if a_ac.value >= a_nac.value:

                resultado = n1-n2
                salida_suma.value = f"el proximo ano va a cumplir {resultado+1}"
            else:
                salida_suma.value = "el ano actual debe ser mayor al de nacimiento"

        else:
            salida_suma.value = "ingresa valores iguales o mayores a cero" 

    except ValueError:
        salida_suma.value = "Error"
    
app = App(title="edad por cumplir")

message = Text(app, text="dame el ano actual")
a_ac = TextBox(app, width=20)
message = Text(app, text="dame el ano de nacimiento")
a_nac = TextBox(app, width=20)

button = PushButton(app, text="calcular", command=suma)
salida_suma = Text(app, text="")

app.display()