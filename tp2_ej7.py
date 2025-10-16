
archivo = "ej7-grafo.txt"
aristas = []
nodos = []


f = open(archivo, "r") #aca abrimos el archivo tal cual aprendimos en la materia "informatica general"
lineas = f.readlines()
f.close()

for linea in lineas:
    linea = linea.strip()
    if linea == "":
        continue
    partes = linea.split()
    origen = partes[0]
    destino = partes[1]
    aristas.append([origen,destino])
    if origen not in nodos:
        nodos.append(origen)
    if destino not in nodos:
        nodos.append(destino)

orden = []


while len(nodos) > 0:
    encontrado = False
    for n in nodos:
        tiene_predecesor = False
        for a,b in aristas:
            if b == n:
                tiene_predecesor = True
                break
        if not tiene_predecesor:
            
            orden.append(n)
            encontrado = True
            break
    if encontrado:
        
        nueva_lista_nodos = []
        for x in nodos:
            if x != n:
                nueva_lista_nodos.append(x)
        nodos = nueva_lista_nodos

        
        nuevas_aristas = []
        for a,b in aristas:
            if a != n:
                nuevas_aristas.append([a,b])
        aristas = nuevas_aristas
    else:
        orden = None
        break


if orden == None:
    print("El grafo tiene ciclos. No se puede calcular T-Sort.")
else:
    print("Orden topológico:", orden)
