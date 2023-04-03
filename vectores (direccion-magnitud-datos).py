import math 

def datos_vectores(info,x,y):
    magnitud = math.sqrt(x**2 + y**2)
    direccion = math.atan2(y,x)
    direccion_grados = math.degrees(direccion)
    print(f'Para el vector -> {info}({x},{y})')
    print(f"La medida del vector es: {round(magnitud,2)}")
    print(f"La dirección del vector es: {round(abs(direccion_grados),2)}")
    print()

def comp_vectores(info, unidades, direccion):

    v_x = math.radians(direccion)
    vec_x = math.cos(v_x)
    x = unidades * vec_x

    v_y = math.radians(direccion)
    vec_y = math.sin(v_y)
    y = unidades * vec_y

    print(f'Los compenentes del vector con direccion de {direccion}° y {unidades} unidades.', end=' -> ')
    print(f'{info}({round(x)},{round(y)})')

diccionario_md = {'P':(5,3), 'R':(-9,5), 'T':(-5,-5), 'V':(5,-7), 'X':(-5,-7),
                  'Q':(4,-3), 'S':(-2,5), 'U':(-4, 6), 'W':(-6,-7), 'Y':(4,7)}

diccionario_comp = {'A':(15, 18), 'C':(18,135), 'E':(25, 175), 'G':(14,245), 'B':(4,3),
                    'I':(15,275), 'D':(18, 35), 'F':(18,165), 'H':(22, 335), 'J':(15,295)}

for i, k in diccionario_md.items():
    x, y = k[0],k[1]
    datos_vectores(i,x,y)

print()

for i, k in diccionario_comp.items():
    x, y = k[0], k[1]
    comp_vectores(i,x,y)

# datos_vectores(x = 5, y = 3)
# comp_vectores(unidades = 5.83, direccion = 30.96)

