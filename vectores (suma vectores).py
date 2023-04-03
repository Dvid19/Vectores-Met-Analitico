import math 

def datos_vectores(info,x,y):
    magnitud = math.sqrt(x**2 + y**2)
    tan = y/x
    direccion = math.atan(tan)
    direccion_grados = math.degrees(direccion)
    return info, round(magnitud,1), round(abs(direccion_grados), 1)

def comp_vectores(nombre,unidades, direccion):

    v_x = math.radians(direccion)
    vec_x = math.cos(v_x)
    x = unidades * vec_x

    v_y = math.radians(direccion)
    vec_y = math.sin(v_y)
    y = unidades * vec_y

    return nombre, round(x), round(y)

def sumas(op, suma, vec):
    sym = ('+', '-', '(', ')')
    sum_x = ''
    sum_y = ''
    for i in suma:
        if i.isalpha():
            #print(i, 'Es una letra')
            sum_x += str(vec[i][0])
            sum_y += str(vec[i][1])
        elif i in sym:
            #print(i, 'No es una letra')
            sum_x += i 
            sum_y += i
    sum_x_res = eval(sum_x)
    sum_y_res = eval(sum_y)
    R = (sum_x_res, sum_y_res)
    R_res = datos_vectores(op, R[0], R[1])
    return R, R_res

def mostrar_resultado(s):
    ### R
    suma_R1 = s
    rir = sumas('R1', suma_R1, vec)
    R1_res = rir[1]
    print(f'El resultante de >> {suma_R1} << es: ({R1_res[1]} L, {R1_res[2]}°)')
    return rir[0]

diccionario_md = {'P':(5,3), 'R':(-9,5), 'T':(-5,-5), 'V':(5,-7), 'X':(-5,-7),
                  'Q':(4,-3), 'S':(-2,-5), 'U':(-4, 6), 'W':(-6,-7), 'Y':(4,7)}

diccionario_comp = {'A':(15, 18), 'C':(18,135), 'E':(25, 175), 'G':(14,245), 'B':(4,3),
                    'I':(15,275), 'D':(18, 35), 'F':(18,165), 'H':(22, 335), 'J':(15,295)}
                    
vec = dict()

for i, k in diccionario_md.items():
    x, y = k[0],k[1]
    vec[i] = (x,y)

for i, k in diccionario_comp.items():
    x, y = k[0], k[1]
    veco = comp_vectores(i,x,y)
    vec[veco[0]] = (veco[1],veco[2])


ope = {'R1':'P+A+S+D', 'R2':'Q+C', 'R3':'A+B-T', 'R4':'W+A+B', 'R5':'X+C+E+D',
       'R6':'X+Y+F+G', 'R7':'H+I', 'R8':'P+T+V+C+E+F', 'R9':'H+Y', 'R10':'J+G-(T+X)'}

datos_graficos = []
for i in ope:
    print(i, end=' -> ')
    r_res = mostrar_resultado(ope[i])
    datos_graficos.append(r_res)

print(datos_graficos)



### R2
# suma_R2 = 'Q+C'
# R2, R2_res = sumas('R2', suma_R2, vec)
# print(R2_res)

# print(vec['P'][0], ' + ', vec['A'][0])
# print(vec['P'][1], ' + ', vec['A'][1])