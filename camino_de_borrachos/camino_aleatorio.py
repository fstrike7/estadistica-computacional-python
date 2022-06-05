from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada
from bokeh.plotting import figure, show

def caminata(campo: Campo, borracho, pasos):
    """
    Toma una coordenada de inicio, mueve al borracho n veces (donde n es la cantidad de pasos)
    y obtiene una distancia promedio, comparando la coordenada de inicio con la coordenada final
    """
    inicio = campo.obtener_coordenada(borracho)
    for _ in range(pasos):
        campo.mover_borracho(borracho)
    
    return inicio.distancia(campo.obtener_coordenada(borracho))

def simular_caminata(pasos, intentos, borracho_type):
    """
    Instancia los distintos objetos, llama a la función caminata 
    y guarda la distancia en la variable resultados.
    """
    borracho = borracho_type(nombre="Prueba") # Instancia un borracho, indistinto de su tipo.
    origen = Coordenada(0,0) # Instancia una coordenada desde el punto x=0, y=0.
    resultados = list()

    for _ in range(intentos):
        campo = Campo() # Instancia un campo
        campo.anadir_borracho(borracho, origen)
        simulacion = caminata(campo, borracho, pasos)
        resultados.append(round(simulacion, 1))
    return resultados

def graficar(conjuntos):
    colores = ['red', 'blue', 'green']
    indice = 0
    grafica = figure(title="Camino aleatorio", x_axis_label="Pasos", y_axis_label="Distancia")
    for x, y, label in conjuntos:
        grafica.line(x, y, legend_label=label, color=colores[indice])
        indice += 1

    show(grafica)

def main(distancias, intentos, borracho_type):
    """
    Itera la cantidad de pasos que guardamos en la lista distancias, y por cada una simula una caminata de borracho.
    """
    medias_por_caminata = list()
    minimas = list()
    maximas = list()
    for pasos in distancias:
        distancias_recorridas = simular_caminata(pasos, intentos, borracho_type)
        # Sacamos la media del total de distancias
        distancia_media = round(sum(distancias_recorridas)/len(distancias_recorridas), 4)
        # Distancia máxima/minima usando método max y min
        distancia_maxima = max(distancias_recorridas)
        distancia_minima = min(distancias_recorridas)
        medias_por_caminata.append(distancia_media)
        minimas.append(distancia_minima)
        maximas.append(distancia_maxima)
        print(f'{borracho_type.__name__} caminata aleatoria de {pasos} pasos')
        print(f'\tDistancia media: {distancia_media} \n\tDistancia máxima: {distancia_maxima} \n\tDistancia minima: {distancia_minima}')
    graficar([
        (distancias, medias_por_caminata, "Distancia media"), # Gráficar distancia media
        (distancias, minimas, "Distancia minima"),
        (distancias, maximas, "Distancia máxima")    
    ])

if __name__ == '__main__':
    distancias = [10, 100, 1000, 10000]
    intentos = 100

    main(distancias, intentos, BorrachoTradicional)