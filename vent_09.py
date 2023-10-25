from guizero import App, Box, Text, TextBox, PushButton

def calcular_sumas():
    nums = entrada_nums.value.split()
    suma_cuadrados_pares = 0
    suma_cubos_impares = 0
    
    for num in nums:
        try:
            num = int(num)
            if num>=0:
              if num % 2 == 0:
                suma_cuadrados_pares += num ** 2
              else:
                suma_cubos_impares += num ** 3
            else:
                resultado.value = "ingresa valores positivos"    
        except ValueError:
            resultado.value = "ingresa los valores separados por espacios"
            return

    resultado.value = f"la suma de los cuadrados de los pares: {suma_cuadrados_pares}\nla suma de los cuadrados de los impares: {suma_cubos_impares}"


app = App("suma de cuadrados pares e impares")
instruccion = Text(app, "ingresa los valores separados por espacios:")
entrada_nums = TextBox(app, width=40)
boton_calcular = PushButton(app, text="Calcular", command=calcular_sumas)
resultado = Text(app, "")

app.display()