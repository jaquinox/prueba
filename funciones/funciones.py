

def Sumar(numeo1, numero2):
    resultado = numeo1 + numero2
    return resultado



num1 = int(input("Ingrese primer numero:  "))

num2 = int(input("Ingrese segund numero:  "))

# numero3 = (num1 + num2) + 30

numero3 = Sumar(num1, num2) + 30

print(numero3)