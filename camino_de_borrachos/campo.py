class Campo:

    def __init__(self):
        self.coordenadas_de_borrachos = {}
    
    def anadir_borracho(self, borracho, coordenada):
        """
        Agrega un borracho al diccionario coordenadas_de_borrachos, 
        el cual guarda como clave al borracho y como valor su posición como coordenada.
        """ 
        self.coordenadas_de_borrachos[borracho] = coordenada

    def mover_borracho(self, borracho):
        """
        Recibe un borracho, llama a su función camina la cual nos devuelve una tupla aleatoria con dos valores:
        delta_x y delta_y, que corresponden a los pasos que debe hacer el borracho sobre su eje.
        Consulta la coordenada actual del borracho desde el diccionario coordenadas_de_borrachos, 
        y llama a la función mover pasandole como argumento los resultados de la tupla.
        Guarda el resultado de esa función (es decir, una nueva coordenada) en el diccionario.
        """
        delta_x, delta_y = borracho.camina()
        coordenada_actual = self.coordenadas_de_borrachos[borracho]
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)
        self.coordenadas_de_borrachos[borracho] = nueva_coordenada

    def obtener_coordenada(self, borracho):
        """
        Recibe un borracho y devuelve su coordenada actual.
        """
        return self.coordenadas_de_borrachos[borracho]