# universidad_ultra_simple.py

import random

# Crear arreglos 1D
INSCRIPTOS = [0]*(4*5*2*25*85)
CAPACIDAD = [0]*(4*5*2*25*85)

# Cargar datos aleatorios
for edificio in range(4):
    for piso in range(5):
        for ala in range(2):
            for aula in range(25):
                for bloque in range(85):
                    pos = (((edificio*5 + piso)*2 + ala)*25 + aula)*85 + bloque
                    cap = random.randint(20,100)
                    CAPACIDAD[pos] = cap
                    INSCRIPTOS[pos] = random.randint(0,cap)

# item a)
max_porcentaje = -1
mejor_aula = None

for edificio in range(4):
    for piso in range(5):
        for ala in range(2):
            for aula in range(25):
                for bloque in range(85):
                    pos = (((edificio*5 + piso)*2 + ala)*25 + aula)*85 + bloque
                    porcentaje = INSCRIPTOS[pos]/CAPACIDAD[pos]
                    if porcentaje > max_porcentaje:
                        max_porcentaje = porcentaje
                        mejor_aula = (edificio,piso,ala,aula,bloque)

print("Mayor porcentaje:", max_porcentaje)
print("Aula/Bloque:", mejor_aula)

# item b)
bloque = 10
for piso in range(5):
    total = 0
    count = 0
    for edificio in range(4):
        for ala in range(2):
            for aula in range(25):
                pos = (((edificio*5 + piso)*2 + ala)*25 + aula)*85 + bloque
                total += INSCRIPTOS[pos]
                count += 1
    print("Promedio piso", piso, ":", total/count)

# item c)

edificio, piso, bloque = 0, 2, 10
total_ala = [0,0]
for ala in range(2):
    total = 0
    for aula in range(25):
        pos = (((edificio*5 + piso)*2 + ala)*25 + aula)*85 + bloque
        total += INSCRIPTOS[pos]
    total_ala[ala] = total

print("Alumnos por ala en edificio", edificio, "piso", piso, "bloque", bloque, ":", total_ala)
