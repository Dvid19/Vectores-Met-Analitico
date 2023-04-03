import matplotlib.pyplot as plt

def datos_grafico(x,y):

    dX = list()
    dY = list()

    if abs(x) > abs(y):mayor = round(x)
    else:mayor = round(y)

    if mayor > 0:
        mayor = mayor * -1
    
    for ix in range(mayor, 1):
        res = (x/abs(mayor)) * abs(ix)
        dX.append(round(res,1))

    for iy in range(mayor, 1):
        res = (y/abs(mayor)) * abs(iy)
        dY.append(round(res,1))

    return dX, dY

datos_ejes = [(32, 13), (-9, 10), (23, 10), (12, -2), (-28, 18), (-24, -8), (21, -24), (-50, 11), (24, -2), (10, -15)]

fig, ax = plt.subplots()
# Establecer límites de los ejes
ax.set_xlim([-50, 50])
ax.set_ylim([-50, 50])

# Establecer etiquetas de los ejes
ax.set_xlabel('Eje x')
ax.set_ylabel('Eje y')

xA, yA = datos_grafico(datos_ejes[0][0], datos_ejes[0][1])

plt.plot(xA, yA, label='Vector Resultante')

# Agregar un eje vertical y horizontal
ax.axhline(0, color='black')
ax.axvline(0, color='black')

plt.title('Grafica del vector resultante')
plt.legend()

plt.show()





