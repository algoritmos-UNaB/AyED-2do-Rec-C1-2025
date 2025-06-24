# 🎸 Examen Parcial: Sistema de Gestión de Concurso de Bandas de Rock
# Universidad: [Nombre de tu Universidad]
# Materia: Algoritmos y Estructuras de Datos
# Estudiante: [Tu nombre]
# Fecha: [Fecha del examen]

# =============================================================================
# EJERCICIO 1: CLASES FUNDAMENTALES (10 puntos)
# =============================================================================

class Banda:
    """
    Clase para representar una banda musical en el concurso.
    """
    def __init__(self, nombre, integrantes, genero_musical, ciudad_origen):
        # TODO: Implementar constructor
        # Atributos: nombre, integrantes (lista), genero_musical, ciudad_origen, 
        # presentaciones (lista), ranking_actual (inicializar en 100)
        pass
    
    def sumar_puntos(self, puntos):
        """Suma puntos al ranking actual de la banda."""
        # TODO: Implementar método
        pass
    
    def restar_puntos(self, puntos):
        """Resta puntos al ranking actual de la banda. Mínimo 100."""
        # TODO: Implementar método
        pass


class PresentacionMusical:
    """
    Clase para representar una presentación musical en el concurso.
    """
    def __init__(self, identificador, nombre, lugar, par):
        # TODO: Implementar constructor
        # Atributos: identificador (int), nombre, lugar, par (puntos totales), 
        # bandas (lista), puntos_obtenidos (dict)
        pass


# =============================================================================
# EJERCICIO 2: LÓGICA DE COMPETENCIAS (18 puntos)
# =============================================================================

# Agregar estos métodos a la clase Banda:

def iniciar_competencia(self, presentacion_musical):
    """
    Inicia una competencia para la banda.
    - Agregar presentación a la lista de presentaciones
    - Asignar lista privada de bandas participantes
    - Recalcular ranking usando últimas 8 mejores presentaciones
    """
    # TODO: Implementar método
    pass

def calcular_ranking(self, lista_presentaciones):
    """
    Calcula el ranking basado en las últimas 8 mejores puntuaciones.
    Usar búsqueda lineal para obtener las presentaciones necesarias.
    """
    # TODO: Implementar método
    pass

def eliminar_competencia(self, identificador):
    """
    Elimina TODAS las instancias de la presentación con ese ID.
    Tanto de la lista de la banda como de otras bandas participantes.
    Recalcular rankings correspondientes tras cada eliminación.
    """
    # TODO: Implementar método
    pass


# =============================================================================
# EJERCICIO 3: ESTRUCTURAS DE DATOS (24 puntos)
# =============================================================================

class Nodo:
    """Nodo para la lista enlazada."""
    def __init__(self, dato):
        # TODO: Implementar constructor
        pass

class ListaEnlazada:
    """Lista simple enlazada."""
    def __init__(self):
        # TODO: Implementar constructor
        pass
    
    def agregar_al_inicio(self, dato):
        """Agrega un elemento al inicio de la lista."""
        # TODO: Implementar método
        pass
    
    def agregar_al_final(self, dato):
        """Agrega un elemento al final de la lista."""
        # TODO: Implementar método
        pass
    
    def obtener_tamaño(self):
        """Retorna el tamaño de la lista."""
        # TODO: Implementar método
        pass
    
    def obtener_elemento(self, indice):
        """Retorna el elemento en el índice especificado."""
        # TODO: Implementar método
        pass

class Pila:
    """Pila implementada usando lista enlazada."""
    def __init__(self):
        # TODO: Implementar constructor
        pass
    
    def apilar(self, elemento):
        """Apila un elemento en la pila."""
        # TODO: Implementar método
        pass
    
    def desapilar(self):
        """Desapila y retorna el elemento del tope."""
        # TODO: Implementar método
        pass
    
    def tope(self):
        """Retorna el elemento del tope sin desapilar."""
        # TODO: Implementar método
        pass
    
    def esta_vacia(self):
        """Retorna True si la pila está vacía."""
        # TODO: Implementar método
        pass
    
    def __iter__(self):
        """Iterador para la pila."""
        # TODO: Implementar método
        pass
    
    def __next__(self):
        """Siguiente elemento del iterador."""
        # TODO: Implementar método
        pass

class PilaPresentaciones:
    """
    Pila que se comporta como COLA (FIFO).
    Redefinir operaciones para comportamiento de cola.
    """
    def __init__(self):
        # TODO: Implementar constructor
        pass
    
    def apilar(self, elemento):
        """Agrega elemento (comportamiento de cola)."""
        # TODO: Implementar método
        pass
    
    def desapilar(self):
        """Retorna primer elemento en entrar (FIFO)."""
        # TODO: Implementar método
        pass
    
    def tope(self):
        """Retorna el elemento que será desapilado."""
        # TODO: Implementar método
        pass
    
    def esta_vacia(self):
        """Retorna True si la cola está vacía."""
        # TODO: Implementar método
        pass
    
    def __iter__(self):
        """Iterador para la cola."""
        # TODO: Implementar método
        pass
    
    def __next__(self):
        """Siguiente elemento del iterador."""
        # TODO: Implementar método
        pass


# =============================================================================
# EJERCICIO 4: MANEJO DE DATOS Y ARCHIVOS (18 puntos)
# =============================================================================

# Agregar este método a la clase Banda:

def presentaciones_a_string(self):
    """
    Retorna lista de strings con los atributos de todas las presentaciones.
    Formato: una presentación por string, listos para imprimir.
    """
    # TODO: Implementar método
    pass

def generar_bandas_aleatorias():
    """
    Genera entre 15-25 bandas con datos realistas.
    Asigna 8-12 presentaciones musicales aleatorias.
    Sin asistencia del usuario - completamente automático.
    """
    # TODO: Implementar función
    pass

def exportar_txt_bandas(lista_bandas):
    """
    Función que recibe la lista de bandas del punto 4.2.
    Genera archivos txt individuales por banda.
    Nombre del archivo = nombre de la banda + '.txt'
    Una presentación por línea con todos sus datos.
    """
    # TODO: Implementar función
    pass


# =============================================================================
# CÓDIGO DE PRUEBA (OPCIONAL - PARA VERIFICAR IMPLEMENTACIÓN)
# =============================================================================

if __name__ == "__main__":
    # Código de prueba para verificar que las clases funcionan
    print("🎸 Sistema de Gestión de Concurso de Bandas de Rock")
    print("✅ Archivo ejercicio1.py cargado correctamente")
    
    # Aquí puedes agregar código de prueba durante el desarrollo
    # pero recuerda que solo se evalúa la implementación de las clases y métodos 