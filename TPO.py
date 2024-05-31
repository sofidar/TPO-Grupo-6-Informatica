#Una empresa cuenta con un plantel de vendedores, numerados con valores positivos arbitrarios. Por cada venta realizada se ingresa por teclado el número de vendedor y el importe
#de la misma, donde un número de vendedor -1 indica el final de los datos. Realizar un programa para imprimir:
#· Total vendido por cada vendedor, ordenado de mayor a menor según el total vendido.
#· Importe de la venta promedio por vendedor.
#· Número de vendedor con mayor cantidad de ventas.
#· Importe y número de vendedor correspondiente a la mayor venta realizada.
#La cantidad de vendedores no se conoce. Este dato deberá deducirse se las ventas ingresadas.

#una fucnión que ingrese datos (las  listas)
#una función que sea el método de inserción
#una función que de total vendido por vendedor
#función de promedio de ventas x vendedor
# función del vendedor con mayor cantidad de ventas --> buscar 
#función de mayor venta realizada --> buscar el mayor valor de la lista de ventas
    
def ingresar_ventas():
    vendedores = [ ]
    ventas = [ ]
    
    num_vendedor = int(input("Ingrese el número de vendedor (-1 para terminar): "))
    vendedores.append(num_vendedor)
    while num_vendedor != -1:
        importe_venta = float(input("Ingrese el importe de la venta: "))
        ventas.append(importe_venta)
        num_vendedor = int(input("Ingrese el número de vendedor (-1 para terminar): "))
        vendedores.append(num_vendedor)
        
    return ventas, vendedores

def metododeinsercion(lista):
    for i in range(1, len(lista)):
        aux = lista[i]
        j=i
        while j>0 and lista[j-1]>aux:
            j= j-1
        lista[j] = aux

def calcular_promedio_por_vendedor(ventas, vendedores, vendedor):
    total = 0
    cantidad_ventas = 0
    for i in range(len(ventas)):
        if vendedores[i] == vendedor:
            total += ventas[i]
            cantidad_ventas += 1
    return total / cantidad_ventas if cantidad_ventas != 0 else 0


ventas, vendedores = ingresar_ventas()

total_por_vendedor = calcular_promedio_por_vendedor(ventas, vendedores, vendedor)
total_por_vendedor_ordenado = metododeinsercion(total_por_vendedor)
