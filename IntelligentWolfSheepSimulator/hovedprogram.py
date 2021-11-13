import pgzrun
from spillbrett import Spillbrett

bane = "IntelligentWolfSheepSimulator/testbaner/testbane3.txt"
spillbrett = Spillbrett(3000)
spillbrett.legg_til_objekter_fra_fil(bane)


# Dette er prekode som gjoer at pygame-zero fungerer. Ikke endre dette:
WIDTH = 900
HEIGHT = 700


def draw():
    screen.fill((128, 81, 9))
    spillbrett.tegn(screen)


def update():
    spillbrett.oppdater()


pgzrun.go()
