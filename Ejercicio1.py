def minion_game (cadena):
    puntuacionstuart = 0
    puntuacionkevin = 0
    vocal = 'aeiouAEIOU'
    for i in range (len(cadena)):
        if cadena[i] not in vocal:
            puntuacionstuart += (len(cadena))
        else: 
            puntuacionkevin += (len(cadena))
    print ("La puntuación de Stuart es " + puntuacionstuart + "y la puntuación de Kevin es " + puntuacionkevin)
    if puntuacionstuart > puntuacionkevin:
        print ("Ganador, Stuart")
    elif puntuacionstuart < puntuacionkevin:
        print ("Ganador, Kevin")
    else:
        print ("Empate :(")

cadena = input ("Escoja una palabra: ")
if __name__ == "__main__":
    minion_game (cadena)