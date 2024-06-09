# Escribir el popular juego del tres en raya.
# El juego consiste en un tablero de 3x3 en el que dos jugadores
# van colocando fichas (una cada uno) por turnos. El objetivo es
# conseguir tres fichas propias en línea recta, ya sea en
# horizontal, vertical o diagonal.
# El programa debe mostrar el tablero cada vez que se coloca una
# ficha. Se debe detectar si hay un ganador o si hay empate.
# En ese caso, el programa debe indicarlo y terminar.
# El tablero se puede representar con una lista de 3 elementos,
# en la que cada elemento es a su vez una lista de 3 elementos,
# de modo que cada posición del tablero se puede representar
# con las coordenadas fila y columna.
# Por ejemplo, la posición central se representa como tablero[1][1].
# Para pedir las jugadas, el programa mostrará las posiciones
# válidas en las que se puede colocar una ficha.
# El programa debe comprobar la validez de las jugadas.
# Si un jugador introduce una jugada inválida, el programa debe
# detectarlo y seguir pidiendo jugadas hasta que el jugador
# introduzca una correcta.
# El programa debe preguntar si los jugadores quieren volver a
# jugar al terminar una partida.
# El programa debe llevar un contador de partidas ganadas por
# cada jugador y de partidas empatadas.
# Se debe generar la documentación de cada módulo y/o función con el módulo pydoc.

import random

def mostrar_tablero(tablero):
    """
    Esta función imprime el tablero actual del juego.
    :param tablero: Una lista de listas que representa el tablero del juego.
    """
    print("Tablero actual:")

    for fila in tablero:
        print(" --- --- ---")
        print("|", end="")
        for casilla in fila:
            print(" {} |".format(casilla), end="")
        print()
    print(" --- --- ---")
    print("Ingrese su jugada como dos números separados por una coma.\nPor ejemplo: '12' sin las comillas para colocar su ficha en la fila 1, columna 2.")

def comprobar_ganador(tablero):
    """
    Esta función comprueba si hay un ganador en el juego actual.
    Comprueba todas las filas, columnas y diagonales para ver si todas las casillas son iguales y no están vacías.
    :param tablero: Una lista de listas que representa el tablero del juego.
    :return: True si hay un ganador, False en caso contrario.
    """

    for fila in tablero:
        if fila[0] == fila[1] == fila[2] and fila[0] != " ":
            return fila[0]
    for i in range(3):
        if tablero[0][i] == tablero[1][i] == tablero[2][i] and tablero[0][i] != " ":
            return tablero[0][i]
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " ":
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " ":
        return tablero[0][2]
    return None

def comprobar_empate(tablero):
    """
    Esta función comprueba si el juego ha terminado en empate.
    Esto ocurre cuando todas las casillas del tablero están llenas y no hay un ganador.
    :param tablero: Una lista de listas que representa el tablero del juego.
    :return: True si el juego ha terminado en empate, False en caso contrario.
    """

    for fila in tablero:
        for casilla in fila:
            if casilla == " ":
                return False
    return True

def pedir_jugada(jugador, tablero):
    """
    Esta función pide al jugador actual que introduzca su jugada.
    La jugada es una cadena que representa la fila y la columna donde el jugador quiere colocar su ficha.
    :param jugador: El número del jugador actual (1 o 2).
    :param tablero: Una lista de listas que representa el tablero del juego.
    :return: Una tupla que contiene la fila y la columna donde el jugador quiere colocar su ficha.
    """

    print("Turno del jugador", jugador)
    jugada = input("Introduce la fila y columna donde colocar la ficha: ")
    while len(jugada) != 2 or not jugada[0].isdigit() or not jugada[1].isdigit():
        jugada = input("Introduce una jugada válida: ")
    fila = int(jugada[0]) - 1
    columna = int(jugada[1]) - 1
    while fila < 0 or fila > 2 or columna < 0 or columna > 2 or tablero[fila][columna] != " ":
        jugada = input("Introduce una jugada válida: ")
        fila = int(jugada[0]) - 1
        columna = int(jugada[1]) - 1
    return fila, columna

def jugar_tres_en_raya():
    """
    Esta función controla el flujo del juego del tres en raya.
    """

    # Inicializar el tablero
    tablero = [[" " for _ in range(3)] for _ in range(3)]

    # Inicializar los contadores de partidas ganadas y empatadas
    partidas_ganadas_jugador1 = 0
    partidas_ganadas_jugador2 = 0
    partidas_empatadas = 0

    # Variable para controlar si los jugadores quieren volver a jugar
    jugar_nuevamente = True

    while jugar_nuevamente:
        """
        Este bucle se ejecuta mientras los jugadores quieran seguir jugando.
        """

        # Variable para controlar el turno del jugador
        jugador_actual = 1

        # Variable para controlar si el juego ha terminado
        juego_terminado = False

        # Mostrar el tablero inicial
        mostrar_tablero(tablero)

        while not juego_terminado:
            """
            Este bucle se ejecuta mientras el juego no haya terminado.
            """

            # Pedir la jugada al jugador actual
            fila, columna = pedir_jugada(jugador_actual, tablero)

            # Colocar la ficha en el tablero
            tablero[fila][columna] = "X" if jugador_actual == 1 else "O"

            # Mostrar el tablero actualizado
            mostrar_tablero(tablero)

            # Comprobar si hay un ganador
            ganador = comprobar_ganador(tablero)
            if ganador:
                print("¡El jugador", jugador_actual, "ha ganado!")
                if jugador_actual == 1:
                    partidas_ganadas_jugador1 += 1
                else:
                    partidas_ganadas_jugador2 += 1
                juego_terminado = True
            else:
                # Comprobar si hay un empate
                if comprobar_empate(tablero):
                    print("¡Empate!")
                    partidas_empatadas += 1
                    juego_terminado = True
                else:
                    # Cambiar al siguiente jugador
                    jugador_actual = 2 if jugador_actual == 1 else 1

        # Preguntar si los jugadores quieren volver a jugar
        respuesta = input("¿Quieren volver a jugar? (s/n): ")
        jugar_nuevamente = respuesta.lower() == "s"

        # Mostrar el contador de partidas ganadas y empatadas
        print("Partidas ganadas por el jugador 1:", partidas_ganadas_jugador1)
        print("Partidas ganadas por el jugador 2:", partidas_ganadas_jugador2)
        print("Partidas empatadas:", partidas_empatadas)

# Llamar a la función para iniciar el juego
jugar_tres_en_raya()