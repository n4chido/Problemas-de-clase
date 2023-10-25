from guizero import App, Text, TextBox, PushButton

def calcular_sueldo_impuestos():
    try:
        percepciones = float(entrada_percepciones.value)
        sueldo_base = float(entrada_sueldo_base.value)
        
        if sueldo_base > 10000:
            impuesto = sueldo_base * 0.3
        else:
            impuesto = sueldo_base * 0.2
        
        canasta_basica = sueldo_base * 0.05
        prima_antiguedad = sueldo_base * 0.03
        deducciones = canasta_basica + prima_antiguedad
        sueldo_total = percepciones + sueldo_base - deducciones
        impuestos_totales = impuesto

        resultado_sueldo.value = f"su sueldo total es de: ${sueldo_total:.2f}"
        resultado_impuestos.value = f"le pagara al mendigo SAT: ${impuestos_totales:.2f}"
    except ValueError:
        resultado_sueldo.value = "error, ingresa valores validos"

app = App("calcular de sueldo e impuestos")
Text(app, "ingresa las percepciones:")
entrada_percepciones = TextBox(app)
Text(app, "ingresa su sueldo base:")
entrada_sueldo_base = TextBox(app)
boton_calcular = PushButton(app, text="calcular", command=calcular_sueldo_impuestos)
resultado_sueldo = Text(app, "sueldo Total: ")
resultado_impuestos = Text(app, "impuestos al SAT: ")

app.display()