
# Solicitud de datos
peso = float(input("ingrese su peso en kg: "))
altura = float(input("ingrese su altura en centimetros: "))

altura_m = altura / 100
# Calcular el IMC
imc = peso/(altura_m**2)

# Mostrar el resultado
print(f"Tu indice de masa corporal es: {imc:.2f}")

# Interpretar el IMC
if imc < 18.5:
    print("bajo peso")
if imc > 18.5 and imc < 25:
    print("Adecuado")
if imc > 25 and imc < 30:
    print("Sobrepeso")
if imc > 30 and imc < 35:
    print("Obesidad Grado I")
if imc > 35 and imc < 40:
    print("Obesidad Grado II")
if imc > 40:
    print("Obesidad Grado III")


