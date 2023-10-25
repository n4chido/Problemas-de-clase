from guizero import App, Text, TextBox, PushButton

def calcular_promedio():
    numeros = nums.value.split()  
    try:
        numeros = [int(num) for num in numeros]
        if all(num >= 0 for num in numeros):

          promedio = sum(numeros) / len(numeros) 
          resultado.value = f"el promedio es: {promedio:.2f}"
        else:
           resultado.value = "ingresa valores iguales o mayores a cero"
    
    except ValueError:
        resultado.value = "Error"

app = App("promedio de n numeros")

Text(app, "ingresa tus numeros a promediar")
nums = TextBox(app, width=20)
Text(app, "(separa los valores con espacios)")
button = PushButton(app,text= "calcular",command= calcular_promedio)
resultado = Text(app, "")

app.display()