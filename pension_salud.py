sal_base=float(input("Ingrese el salario base del empleado "))
aporte_pension=sal_base*0.04
aporte_salud=sal_base*0.04
descuento=aporte_pension+aporte_salud
sal_final=sal_base-descuento
print("El aporte de salud es de: $",aporte_salud)
print("El aporte de pension es de: $",aporte_pension)
print("El descuento del salario es de: $",descuento)
print("El salario final a pagar: $",sal_final)