cantidad=float(input("Ingrese el valor a invertir en el CDT "))
periodo=int(input("Ingrese la cantidad de dias del CDT "))
porcen_interes=float(input("Ingrese el porcentaje de interes del CDT "))
valor_interes=(cantidad*porcen_interes*periodo)/360
impuestos=valor_interes*0.07
total_pagar=(cantidad+valor_interes)-impuestos
print("El valor de los intereses es de: $",valor_interes)
print("El total a recibir es: $" , total_pagar)