"""
Actividad: Algoritmos de ordenamiento
Estudiante 1: Bubble Sort e Insertion Sort

Cada algoritmo es una función que recibe una lista y devuelve:
    (lista_ordenada, historial, comparaciones, cambios)
El historial guarda una "foto" de la lista al terminar cada iteración.
"""


def bubble_sort(datos):
    """Ordena de menor a mayor comparando vecinos (Bubble Sort)."""
    lista = datos.copy()          # trabajamos sobre una copia
    n = len(lista)
    historial = []
    comparaciones = 0
    intercambios = 0

    for pasada in range(n - 1):
        hubo_cambio = False
        # Tras cada pasada el mayor valor queda en su posición final,
        # por eso el recorrido se acorta en 'pasada' posiciones.
        for i in range(n - 1 - pasada):
            comparaciones += 1
            if lista[i] > lista[i + 1]:
                # Intercambio de dos elementos vecinos
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                intercambios += 1
                hubo_cambio = True
        historial.append(lista.copy())
        if not hubo_cambio:
            break                 # Sin cambios: la lista ya está ordenada
    return lista, historial, comparaciones, intercambios


def insertion_sort(datos):
    """Ordena insertando cada elemento en su lugar (Insertion Sort)."""
    lista = datos.copy()
    historial = []
    comparaciones = 0
    desplazamientos = 0

    for i in range(1, len(lista)):
        clave = lista[i]          # elemento que vamos a insertar
        j = i - 1                 # último elemento de la parte ya ordenada
        while j >= 0:
            comparaciones += 1
            if lista[j] > clave:
                lista[j + 1] = lista[j]   # desplaza el mayor a la derecha
                desplazamientos += 1
                j -= 1
            else:
                break             # ya encontramos el lugar de la clave
        lista[j + 1] = clave      # inserta la clave en su posición
        historial.append(lista.copy())
    return lista, historial, comparaciones, desplazamientos


def mostrar_historial(titulo, original, historial, etiqueta):
    """Imprime el estado de la lista después de cada iteración."""
    print(f"\n{titulo}")
    print(f"  Lista inicial : {original}")
    for numero, estado in enumerate(historial, start=1):
        print(f"  {etiqueta} {numero}: {estado}")


def imprimir_resumen(caso, datos):
    """Ejecuta ambos algoritmos y muestra una línea por algoritmo."""
    _, h1, c1, i1 = bubble_sort(datos)
    _, h2, c2, d2 = insertion_sort(datos)
    print(f"{caso:<26}{'Bubble Sort':<16}{len(h1):<10}{c1:<15}{i1}")
    print(f"{'':<26}{'Insertion Sort':<16}{len(h2):<10}{c2:<15}{d2}")


def main():
    datos = [64, 34, 25, 12, 22, 11, 90]

    print("=" * 62)
    print("  ALGORITMOS DE ORDENAMIENTO: BUBBLE SORT E INSERTION SORT")
    print("=" * 62)

    ordenada, historial, comp, camb = bubble_sort(datos)
    mostrar_historial("--- Bubble Sort ---", datos, historial, "Pasada")
    print(f"  Resultado     : {ordenada}")
    print(f"  Comparaciones : {comp} | Intercambios: {camb}")

    ordenada, historial, comp, desp = insertion_sort(datos)
    mostrar_historial("--- Insertion Sort ---", datos, historial, "Inserción")
    print(f"  Resultado     : {ordenada}")
    print(f"  Comparaciones : {comp} | Desplazamientos: {desp}")

    # Verificación automática contra la función sorted() de Python
    correcto = ordenada == sorted(datos)
    estado = "CORRECTO" if correcto else "ERROR"
    print(f"\nVerificación con sorted(): {estado}")

    print("\n" + "-" * 62)
    print("Resumen por caso (iteraciones, comparaciones, cambios)")
    print(f"{'Caso':<26}{'Algoritmo':<16}{'Iter.':<10}"
          f"{'Comparaciones':<15}Cambios")
    imprimir_resumen("Lista de ejemplo", datos)
    imprimir_resumen("Mejor caso (ordenada)", sorted(datos))
    imprimir_resumen("Peor caso (invertida)", sorted(datos, reverse=True))


if __name__ == "__main__":
    main()