from guizero import App, Text, TextBox, PushButton

def calcular_promedio():
    ano_nac = nums.value.split()
    try:
        ano_nac = [int(ano) for ano in ano_nac]
        if all(ano <= 2023 and ano > 0 for ano in ano_nac):
            edades = [2023 - ano for ano in ano_nac]
            promedio = sum(edades) / len(edades)
            resultado.value = f"la edad promedio es: {promedio:.2f} "
        else:
            resultado.value = "los valores tienen que ser positivos"
    except ValueError:
        resultado.value = "Error"

app = App("promedio de edades")

Text(app, "ingresa los anos de nacimiento")
nums = TextBox(app, width=20)
Text(app, "(separa los valores con espacios)")
button = PushButton(app, text="calcular", command=calcular_promedio)
resultado = Text(app, "")

app.display()