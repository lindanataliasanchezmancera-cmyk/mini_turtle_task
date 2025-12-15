import turtle
# Importo turtle, aunque en este código no se usa directamente

tortuga = "t"
# Variable simbólica para representar la tortuga

espacios = 0
# Guarda la posición horizontal de la tortuga


def adelante(camina_adelante):
    # Mueve la tortuga hacia adelante
    global espacios
    # Uso global para poder modificar la variable espacios

    print((" " * espacios) + "→" + ("-" * camina_adelante) + "↓")
    # Imprime el movimiento de la tortuga en forma de texto

    espacios += camina_adelante + 1
    # Actualiza la posición después de avanzar


def abajo(camina_abajo):
    # Mueve la tortuga hacia abajo
    for _ in range(camina_abajo):
        print((" " * espacios) + "|")
        # Imprime una línea vertical alineada con la posición actual


def reiniciar():
    # Reinicia la posición de la tortuga
    global posicion_x
    # Se intenta usar una variable global

    posicion_x = 0
    # Error: esta variable no existe, debería ser 'espacios'
