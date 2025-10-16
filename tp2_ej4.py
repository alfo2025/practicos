# radix_sort_palabras.py

def radix_sort_palabras(palabras):
    """
    Ordena una lista de palabras usando Radix Sort.
    """
    if not palabras:
        return palabras

    max_len = max(len(p) for p in palabras)

    for i in range(max_len - 1, -1, -1):
      
        buckets = [[] for _ in range(256)]

        for palabra in palabras:
          
            char_index = ord(palabra[i]) if i < len(palabra) else 0
            buckets[char_index].append(palabra)

        
        palabras = [p for bucket in buckets for p in bucket]

    return palabras


def leer_palabras_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()
        palabras = [p.strip() for p in contenido.split(',') if p.strip()]
    return palabras

def guardar_palabras_en_archivo(nombre_archivo, palabras):
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        f.write(','.join(palabras))




if __name__ == "__main__":
    archivo_entrada = "ej4-palabrasSinOrdenar.txt"  
    archivo_salida = "ej4-palabras_ordenadas.txt"

    palabras = leer_palabras_desde_archivo(archivo_entrada)
    palabras_ordenadas = radix_sort_palabras(palabras)
    guardar_palabras_en_archivo(archivo_salida, palabras_ordenadas)

    print("Palabras ordenadas guardadas en:", archivo_salida)
