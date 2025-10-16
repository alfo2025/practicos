
aristas = [['A','C'], ['B','C'], ['B','D'], ['C','E'], ['D','F'], ['E','F'], ['F','G']]


nodos = []
for a, b in aristas:
    if a not in nodos:
        nodos.append(a)
    if b not in nodos:
        nodos.append(b)

orden = []

while len(nodos) > 0:
    encontrado = False
    for i in range(len(nodos)):
        n = nodos[i]
        
        tiene_predecesor = False
        for a, b in aristas:
            if b == n:
                tiene_predecesor = True
                break
        if not tiene_predecesor:
            
            orden.append(n)
            nodos.pop(i)
            # en esta parte de aca estoy borrando las aristas que estan saliendo de ese nodo 
            j = 0
            while j < len(aristas):
                if aristas[j][0] == n:
                    aristas.pop(j)
                else:
                    j += 1
            encontrado = True
            break
    if not encontrado:
        orden = None  # aca puedo ver que encontre el ciclo 
        break

if orden == None:
    print("El grafo tiene ciclos. No se puede calcular T-Sort.")
else:
    print("Orden topológico:", orden)
