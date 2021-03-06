"""
Se encarga de todo lo relacionado con la interpretación de la
entrada del jugador.

El módulo almacena el último verbo y el último nombre reconocidos.

El análisis de la entrada del jugador se lleva a cabo en la función
interpretar.
"""

import vocabulario as voc

_verbo = None
_nombre = None

def verbo():
    """
    Devuelve el último verbo reconocido.

    Args:
        - No tiene

    Returns:
        - El último verbo reconocido, o None si no se
          ha reconocido ninguno.
    """
    return _verbo

def nombre():
    """Devuelve el último nombre reconocido."""
    return _nombre

def interpretar(orden):
    """
    Interpreta la orden del jugador.

    Args:
        - orden: str => La orden del jugador.

    Returns:
        - None

    Modifica:
        - Las variables globales _verbo y _nombre.
    """
    global _verbo
    global _nombre
    _verbo, _nombre = None, None
    lista = orden.upper().split()
    if len(lista) >= 1:
        _buscar_verbo_primera_palabra(lista)
    if len(lista) >= 2:
        _buscar_nombre_segunda_palabra(lista)

def marcar_error_sintactico():
    global _verbo
    _verbo = None

def hay_error_sintactico():
    return _verbo is None

def verbo_es_direccion():
    return voc.es_direccion(_verbo)

def _buscar_verbo_primera_palabra(lista):
    global _verbo
    global _nombre
    for palabra in voc.palabras:
        if lista[0] == palabra[0]:
            if palabra[1] == voc.VERBO:
                _verbo = lista[0]
                _nombre = None
            elif palabra[1] == voc.NOMBRE:
                marcar_error_sintactico()
                _nombre = None
            break

def _buscar_nombre_segunda_palabra(lista):
    global _verbo
    global _nombre
    for palabra in voc.palabras:
        if lista[1] == palabra[0]:
            if palabra[1] == voc.NOMBRE:
                _nombre = lista[1]
            else:
                marcar_error_sintactico()
