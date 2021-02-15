#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import pygame
import sys
import random
from pygame.locals import *  # udostępnienie nazw metod z locals

pygame.init()


def przygotuj_populacje(polegry):
    global spr

    nast_gen = [martwa] * komorka.poziom
    for i in range(komorka.poziom):
        nast_gen[i] = [martwa] * komorka.pion

    for y in range(komorka.pion):
        for x in range(komorka.poziom):

            populacja = 0
            # wiersz 1
            try:
                if polegry[x - 1][y - 1] == zywa:
                    populacja += 1
            except IndexError:
                pass
            try:
                if polegry[x][y - 1] == zywa:
                    populacja += 1
            except IndexError:
                pass
            try:
                if polegry[x + 1][y - 1] == zywa:
                    populacja += 1
            except IndexError:
                pass

            # wiersz 2
            try:
                if polegry[x - 1][y] == zywa:
                    populacja += 1
            except IndexError:
                pass
            try:
                if polegry[x + 1][y] == zywa:
                    populacja += 1
            except IndexError:
                pass

            # wiersz 3
            try:
                if polegry[x - 1][y + 1] == zywa:
                    populacja += 1
            except IndexError:
                pass
            try:
                if polegry[x][y + 1] == zywa:
                    populacja += 1
            except IndexError:
                pass
            try:
                if polegry[x + 1][y + 1] == zywa:
                    populacja += 1
            except IndexError:
                pass

            if polegry[x][y] == zywa:
                for liczba in tryb[0]:
                    if populacja == liczba:
                        nast_gen[x][y] = zywa
                        break
                    else:
                        nast_gen[x][y] = martwa
            if polegry[x][y] == martwa:
                for liczba in tryb[1]:
                    if populacja == liczba:
                        nast_gen[x][y] = zywa
                        break
                    else:
                        nast_gen[x][y] = martwa
    return nast_gen

def rysuj_populacje():

    for y in range(komorka.pion):
        for x in range(komorka.poziom):
            if komorka.gra[x][y] == zywa:
                pygame.draw.rect(okno_gry, (kolor_2),((x * komorka.rozmiar, y * komorka.rozmiar), (komorka.rozmiar, komorka.rozmiar )), 5)

def tlo():
    global font
    global font_2
    global stan

    okno_gry.fill(kolor_tla)
    okno_gry.blit(font.render("GRA W ŻYCIE", True, kolor_2), (szerokosc + 10 ,40))
    tryb_napis = "Tryb: {}".format(opcje_tryby[tryb_numer].tekst)
    okno_gry.blit(font_3.render(tryb_napis, True, kolor_2), (szerokosc + 75, 50 + roznica_wysokosc_napis))
    pygame.draw.line(okno_gry, (kolor_2), (szerokosc, 0), (szerokosc, 720), 5)

    if(stan == "trwa"):
        okno_gry.blit(font_2.render("Życie trwa", True, kolor_2), (szerokosc + 20, 200))
        liczba = "Populacja: {}".format(populacja)
        okno_gry.blit(menu_font.render(liczba , True, kolor_2), (szerokosc + 20, 200 + roznica_wysokosc_napis))
    if (stan == "koniec"):
        okno_gry.blit(font_2.render("Koniec Życia", True, kolor_2), (szerokosc + 20, 200))
        okno_gry.blit(menu_font.render("Liczba populacji", True, kolor_2), (szerokosc + 20, 200 + roznica_wysokosc_napis ))
        liczba = "wynosiła: {}".format(populacja)
        okno_gry.blit(menu_font.render(liczba, True, kolor_2), (szerokosc + 20, 200 + roznica_wysokosc_napis + 30))
    if (stan == "pauza"):
        okno_gry.blit(font_2.render("Pauza", True, kolor_2), (szerokosc + 20, 200))
        sterowanie()
    if(stan == "menu"):
        okno_gry.blit(font_2.render("Menu:", True, kolor_2), (szerokosc +20, 200))
        if(guzik_opcje):
            pygame.draw.rect(okno_gry, (kolor_2), ((guzik_wysokosc[0] - 28, guzik_wysokosc[1] + 7), (10, 10)), 5)
        if(guzik_wzor):
            okno_gry.blit(font_3.render("Zalecany tryb Conway's", True, kolor_2),(szerokosc + 20, 640 + roznica_wysokosc_napis))
        if(guzik_muzyka):
            glosnosc = "Głośność: {}%".format(int(muzyka.get_volume()*100 + 0.7))
            okno_gry.blit(menu_font.render(glosnosc, True, kolor_2),(szerokosc + 20, 200 + roznica_wysokosc_napis))
        if(guzik_rozmiar_spr):
            pygame.draw.rect(okno_gry, (kolor_2),((szerokosc + 20, 200 + roznica_wysokosc_napis), (komorka.rozmiar, komorka.rozmiar)), 5)
def tlo_opcje():
    tlo()
    time.sleep(0.1)
def sterowanie():
    okno_gry.blit(menu_font.render("Możesz dodac", True, kolor_2), (szerokosc + 20, 220 + roznica_wysokosc_napis))
    okno_gry.blit(menu_font.render(" lub zabrac komórki", True, kolor_2), (szerokosc + 12, 220 + roznica_wysokosc_napis + 30))
    okno_gry.blit(font_3.render("Steruj myszką:", True, kolor_2), (szerokosc + 20, 580 + roznica_wysokosc_napis))
    okno_gry.blit(font_3.render("lewy - życie", True, kolor_2), (szerokosc + 20, 610 + roznica_wysokosc_napis))
    okno_gry.blit(font_3.render("prawy - śmierć", True, kolor_2), (szerokosc + 20, 640 + roznica_wysokosc_napis))
def kolor_zmiana(x):
    global kolor_tla
    global kolor_2
    kolor_tla = kolory[x].kolor1
    kolor_2 = kolory[x].kolor2

def animacja_menu():
    global delta
    delta += zegar.tick() / 1000.0
    if delta > 1/2:
        komorka.gra = przygotuj_populacje(komorka.gra)
        delta -= 1
    rysuj_populacje()

def wzory(numer, c = 0.2, d = 0.5):
    global komorka

    szerokosc_wzoru = len(wzor[numer])
    wysokosc_wzoru = len(wzor[numer][0])
    wybor_wzoru = numer
    a = 0
    b = 0
    x = int(szerokosc / komorka.rozmiar * c)
    y = int(wysokosc / komorka.rozmiar * d)

    for i in range(x, x + szerokosc_wzoru):
        for j in range(y, y + wysokosc_wzoru):
            try:
                komorka.gra[j][i] = wzor[wybor_wzoru][a][b]
            except IndexError:
                pass
            b += 1
        b = 0
        a += 1

def losowe():
    for i in range(int(szerokosc / komorka.rozmiar)):
        for j in range(int(wysokosc / komorka.rozmiar)):
            komorka.gra[i][j] = random.choice([martwa, martwa, zywa])

def petla_gry():
    global zycie_trwa
    global przycisk_wdol
    global martwa
    global zywa
    global gra
    global szybkosc_gry
    global szybkosc
    global stan
    global populacja
    global komorka

    szybkosc_gry =szybkosci[4]
    while True:
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN and event.key == K_RETURN:
                zycie_trwa = True
                szybkosc_gry = szybkosc
                stan = "trwa"

            if stan == "menu" or stan == "pauza" :
                if event.type == MOUSEBUTTONDOWN:
                    sterowanie()
                    przycisk_wdol = True
                    przycisk_typ = event.button

                if event.type == MOUSEBUTTONUP:
                    przycisk_wdol = False

                if przycisk_wdol:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if (mouse_x < 1080) :
                        mouse_x = int(mouse_x / komorka.rozmiar)
                        mouse_y = int(mouse_y / komorka.rozmiar)
                        # lewy przycisk myszy ożywia
                        if przycisk_typ == 1:
                            komorka.gra[mouse_x][mouse_y] = zywa
                        # prawy przycisk myszy uśmierca
                        if przycisk_typ == 3:
                            komorka.gra[mouse_x][mouse_y] = martwa
        tlo()
#koniec
        if stan == "koniec":
            opcje_inne[2].rect.collidepoint(pygame.mouse.get_pos())
            if opcje_inne[2].rect.collidepoint(pygame.mouse.get_pos()):
                opcje_inne[2].najazd = True
                if (event.type == MOUSEBUTTONDOWN and opcje_inne[2].tekst == "Wyjdź"):
                    komorka.tablica()
                    populacja = 0
                    stan = "menu"
                    return 0
            else:
                opcje_inne[2].najazd = False
            opcje_inne[2].rysuj()
#pauza
        if stan == "pauza":
            for przycisk in (opcje_inne[1],opcje_inne[2]):
                przycisk.rect.collidepoint(pygame.mouse.get_pos())
                if przycisk.rect.collidepoint(pygame.mouse.get_pos()):
                    przycisk.najazd = True
                    if (event.type == MOUSEBUTTONDOWN and przycisk.tekst == "Wróć"):
                        stan = "trwa"
                        szybkosc_gry = szybkosc
                    if (event.type == MOUSEBUTTONDOWN and przycisk.tekst == "Wyjdź"):
                        komorka.tablica()
                        populacja = 0
                        stan = "menu"
                        return 0
                else:
                    przycisk.najazd = False
                przycisk.rysuj()
#gra trwa
        if stan == "trwa":
            opcje_inne[0].rect.collidepoint(pygame.mouse.get_pos())
            if opcje_inne[0].rect.collidepoint(pygame.mouse.get_pos()):
                opcje_inne[0].najazd = True
                if (event.type == MOUSEBUTTONDOWN and opcje_inne[0].tekst == "Pauza"):
                    stan = "pauza"
                    szybkosc_gry = szybkosci[4]
            else:
                opcje_inne[0].najazd = False
            opcje_inne[0].rysuj()
            spr = komorka.gra
            komorka.gra = przygotuj_populacje(komorka.gra)
            populacja += 1
            if (komorka.gra == spr):
                stan = "koniec"
#menu
        if stan == "menu":
            sterowanie()
            for przycisk in (opcje_inne[1],opcje_inne[3]):
                przycisk.rect.collidepoint(pygame.mouse.get_pos())
                if przycisk.rect.collidepoint(pygame.mouse.get_pos()):
                    przycisk.najazd = True
                    if (event.type == MOUSEBUTTONDOWN and przycisk.tekst == "Start"):
                        stan = "trwa"
                        szybkosc_gry = szybkosc
                    if (event.type == MOUSEBUTTONDOWN and przycisk.tekst == "Wróć"):
                        komorka = Komorka(rozmiary[0])
                        populacja = 0
                        stan = "menu"

                        return 0
                else:
                    przycisk.najazd = False
                przycisk.rysuj()
            opcje_inne[3].rect.collidepoint(pygame.mouse.get_pos())

        rysuj_populacje()
        pygame.display.update()

        pygame.time.delay(szybkosc_gry)

def intro(opcje):
    global szybkosci
    global szybkosc
    global tryb
    global guzik_opcje
    global guzik_wysokosc
    global guzik_muzyka
    global komorka
    global guzik_rozmiar_spr
    global guzik_wzor

    while True:

        tlo_opcje()
        animacja_menu()
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            for opcja in opcje:
                if opcja.rect.collidepoint(pygame.mouse.get_pos()):
                    opcja.najazd = True
                    if(event.type == MOUSEBUTTONDOWN ):
                        if (opcja.tekst == "Start"):
                            intro(opcje_start)
                        if (opcja.tekst == "Zmiana palety"):
                            guzik_wysokosc = guzik_paleta
                            guzik_opcje = True
                            intro(opcje_paleta)
                        if (opcja.tekst == "Opcje"):
                            intro(opcje_opcje)

# start
                        if (opcja.tekst == "Własna deklaracja"):
                            komorka = Komorka(rozmiar)
                            petla_gry()
                        if (opcja.tekst == "Losowa plansza"):
                            komorka = Komorka(rozmiar)
                            losowe()
                            petla_gry()
                        if (opcja.tekst == "Stworzone wzory"):
                            komorka = Komorka(rozmiar)
                            guzik_wzor = True
                            intro(opcje_wzory)
#paleta
                        if (opcja.tekst == "Lód"):
                           zmiana_kolor(0,opcja)
                        if (opcja.tekst == "Ogień"):
                            zmiana_kolor(1, opcja)
                        if (opcja.tekst == "Zieleń"):
                            zmiana_kolor(2, opcja)
                        if (opcja.tekst == "Drakula"):
                            zmiana_kolor(3, opcja)
                        if (opcja.tekst == "Róża"):
                            zmiana_kolor(4, opcja)

#opcje
                        if (opcja.tekst == "Rozmiar"):
                            guzik_wysokosc = guzik_rozmiar
                            guzik_opcje = True
                            guzik_rozmiar_spr = True
                            intro(opcje_rozmiar)
                        if (opcja.tekst == "Szybkość"):
                            guzik_wysokosc = guzik_szybkosc
                            guzik_opcje = True
                            intro(opcje_szybkosc)
                        if (opcja.tekst == "Tryb"):
                            guzik_wysokosc = guzik_tryb
                            guzik_opcje = True
                            intro(opcje_tryby)
                        if (opcja.tekst == "Muzyka"):
                            guzik_muzyka = True
                            intro(opcje_muzyka)
    #rozmiar
                        if(opcja.tekst == "Normalna"):
                            zmiana_rozmiar(0, opcja)
                        if (opcja.tekst == "Mała"):
                            zmiana_rozmiar(1, opcja)
                        if (opcja.tekst == "Bardzo mała"):
                            zmiana_rozmiar(2, opcja)
                        if (opcja.tekst == "Duża"):
                            zmiana_rozmiar(3, opcja)
                        if (opcja.tekst == "Bardzo duża"):
                            zmiana_rozmiar(4, opcja)

    #szybkosc
                        if (opcja.tekst == "Normalny"):
                            zmina_szybkosc(0, opcja)
                        if (opcja.tekst == "Wolno"):
                            zmina_szybkosc(1, opcja)
                        if (opcja.tekst == "Bardzo wolno"):
                            zmina_szybkosc(2, opcja)
                        if (opcja.tekst == "Szybko"):
                            zmina_szybkosc(3, opcja)
                        if (opcja.tekst == "Bardzo szybko"):
                            zmina_szybkosc(4, opcja)
    #tryby
                        if (opcja.tekst == "Conway's"):
                            zmiana_tryb(0, opcja)
                        if (opcja.tekst == "Nasiona"):
                            zmiana_tryb(1, opcja)
                        if (opcja.tekst == "Labirynt"):
                            zmiana_tryb(2, opcja)
                        if (opcja.tekst == "Miasta"):
                            zmiana_tryb(3, opcja)
                        if (opcja.tekst == "Wolfram"):
                            zmiana_tryb(4, opcja)
                        if (opcja.tekst == "Koral"):
                            zmiana_tryb(5, opcja)
    #wzory
                        if (opcja.tekst == "Szybowiec"):
                           zmiana_wzor(0)
                        if (opcja.tekst == "Dakota"):
                            zmiana_wzor(1)
                        if (opcja.tekst == "Krokodyl"):
                            zmiana_wzor(2)
                        if (opcja.tekst == "Pulsar"):
                            zmiana_wzor(3)
                        if (opcja.tekst == "Działa"):
                            zmiana_wzor(4)
    #muzyka
                        if (opcja.tekst == "Włącz/wyłącz"):
                            zmiana_muzyka(0)
                        if (opcja.tekst == "Głośniej"):
                            zmiana_muzyka(1)
                        if (opcja.tekst == "Ciszej"):
                            zmiana_muzyka(2)
#inne
                        if (opcja.tekst == "Wróć"):
                            guzik_opcje = False
                            guzik_muzyka = False
                            guzik_rozmiar_spr = False
                            guzik_wzor = False
                            time.sleep(0.1)
                            tlo_opcje()
                            time.sleep(0.1)
                            return 0
                        if (opcja.tekst == "Wyjście"):
                            pygame.quit()
                            sys.exit()
                else:
                    opcja.najazd = False
                opcja.rysuj()
            pygame.display.update()

def zmiana_kolor(x,opcja):
    global guzik_paleta
    global guzik_wysokosc

    kolor_zmiana(x)
    guzik_wysokosc = opcja.pozycja
    guzik_paleta = guzik_wysokosc
    tlo_opcje()
def zmiana_rozmiar(x, opcja):
    global komorka
    global guzik_rozmiar
    global guzik_wysokosc
    global guzik_rozmiar_spr
    global rozmiar

    guzik_rozmiar_spr = True
    rozmiar = rozmiary[x]
    komorka = Komorka(rozmiary[x])
    guzik_wysokosc = opcja.pozycja
    guzik_rozmiar = guzik_wysokosc
def zmina_szybkosc(x, opcja):
    global guzik_szybkosc
    global guzik_wysokosc
    global szybkosc

    szybkosc = szybkosci[x]
    guzik_wysokosc = opcja.pozycja
    guzik_szybkosc = guzik_wysokosc
def zmiana_tryb(x, opcja):
    global guzik_tryb
    global guzik_wysokosc
    global tryb
    global tryb_numer

    tryb = tryby[x]
    tryb_numer = x
    guzik_wysokosc = opcja.pozycja
    guzik_tryb = guzik_wysokosc
def zmiana_wzor(x):
    global komorka
    global guzik_wzor

    wzory(x)
    guzik_wzor = False
    time.sleep(0.5)
    petla_gry()
    time.sleep(0.5)
def zmiana_muzyka(x):
    global muzyka_wlaczona
    global muzyka_glosnosc

    if(x == 0):
        if(muzyka_wlaczona):
            muzyka.stop()
            muzyka_wlaczona = False
        else:
            muzyka.play(-1)
            muzyka_wlaczona = True
    if(x == 1):
        muzyka.set_volume(muzyka_glosnosc + 0.1)
        muzyka_glosnosc += 0.1
    if (x == 2):
        muzyka.set_volume(muzyka_glosnosc - 0.1)
        muzyka_glosnosc -= 0.1
    tlo()

# tworzenie okna gry
szerokosc = 1080
wysokosc = 720
szerokosc_napis = 1100
szerokosc_napis2 = 1130
szerokosc_napis3 = 1170
wysokosc_napis = 320
roznica_szerokosc_napis = 0
roznica_wysokosc_napis = 50
okno_gry = pygame.display.set_mode((szerokosc+300, wysokosc), 0, 32)
ikona = pygame.image.load("icon.png")
pygame.display.set_icon(ikona)
pygame.display.set_caption('Gra w życie')
szybkosc = 50


class Kolor:

    def __init__(self, kolor1 , kolor2):
        self.kolor1 = kolor1
        self.kolor2 = kolor2

kolory = [Kolor(( 112 , 202 , 209),(142 , 227 , 245)) , Kolor((214 , 50 , 48),(243 , 146 , 55)),
          Kolor((56 , 167, 0),(62 , 255 , 139)) , Kolor((7 , 17 , 8),(191 , 177 , 193)) ,
          Kolor((196 , 122 , 192),(97 , 41 , 64))]
kolor_tla = kolory[0].kolor1
kolor_2 = kolory[0].kolor2

szybkosci = [100, 200, 400, 10, 5]
rozmiary = [30, 20 , 10, 40 , 60]
rozmiar = rozmiary[0]
tryby = [[ [2,3],[3]]   ,   [[9],[2]]   ,  [[1,2,3,4,5],[3]]   ,   [[2,3,4,5],[4,5,6,7,8]]  ,
        [[0,1,8],[0,1,8]]   ,   [[4,5,6,7,8],[3]]]
wzor = [
[[1,0,0], [0, 1, 1], [1,1,0]],

[[0,1,1,1,1], [1,0,0,0,1], [0,0,0,0,1], [1,0,0,1,0]],

[[0,0,0,0,1,1,0,0,0,0], [0,0,1,0,0,0,0,1,0,0], [0,1,0,0,0,0,0,0,1,0], [1,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,0,1],[0,1,0,0,0,0,0,0,1,0], [0,0,1,0,0,0,0,1,0,0],
[0,0,0,0,1,1,0,0,0,0]],

[[0,0,0,0,1,0,0,0,0,0,1,0,0,0,0], [0,0,0,0,1,0,0,0,0,0,1,0,0,0,0], [0,0,0,0,1,1,0,0,0,1,1,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [1,1,1,0,0,1,1,0,1,1,0,0,1,1,1], [0,0,1,0,1,0,1,0,1,0,1,0,1,0,0],
[0,0,0,0,1,1,0,0,0,1,1,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,1,1,0,0,0,1,1,0,0,0,0],
[0,0,1,0,1,0,1,0,1,0,1,0,1,0,0], [1,1,1,0,0,1,1,0,1,1,0,0,1,1,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,1,1,0,0,0,1,1,0,0,0,0], [0,0,0,0,1,0,0,0,0,0,1,0,0,0,0], [0,0,0,0,1,0,0,0,0,0,1,0,0,0,0]],

[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
[1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

        ]
tryb = tryby[0]
tryb_numer = 0

class Opcja:
    najazd = False

    def __init__(self, tekst, pozycja):
        self.tekst = tekst
        self.pozycja = pozycja
        self.set_rect()
        self.rysuj()

    def rysuj(self):
        self.set_rend()
        okno_gry.blit(self.rend, self.rect)

    def set_rend(self):
        self.rend = menu_font.render(self.tekst, True, self.zmien_kolor())

    def zmien_kolor(self):
        if self.najazd:
            return (255, 255, 255)
        else:
            return kolor_2

    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pozycja

#szczegoly menu
menu_font = pygame.font.Font("Gatometrix.otf", 40)
font = pygame.font.Font("Gatometrix.otf", 70)
font_2 = pygame.font.Font("Gatometrix.otf", 50)
font_3 = pygame.font.Font("Gatometrix.otf", 30)
opcje = [Opcja("Start", (szerokosc_napis , wysokosc_napis)), Opcja("Zmiana palety", (szerokosc_napis , wysokosc_napis + roznica_wysokosc_napis)),
           Opcja("Opcje", (szerokosc_napis , wysokosc_napis + 2* roznica_wysokosc_napis)), Opcja("Wyjście", (szerokosc_napis , wysokosc_napis + 7*roznica_wysokosc_napis ))]
opcje_start = [Opcja("Własna deklaracja" , (szerokosc_napis , wysokosc_napis)), Opcja("Losowa plansza", (szerokosc_napis , wysokosc_napis + roznica_wysokosc_napis)),
            Opcja("Stworzone wzory", (szerokosc_napis , wysokosc_napis + 2*roznica_wysokosc_napis)), Opcja("Wróć", (szerokosc_napis , wysokosc_napis + 6*roznica_wysokosc_napis))]
opcje_paleta = [Opcja("Lód", (szerokosc_napis2, wysokosc_napis)), Opcja("Ogień", (szerokosc_napis2, wysokosc_napis + roznica_wysokosc_napis)),
           Opcja("Zieleń", (szerokosc_napis2, wysokosc_napis + 2* roznica_wysokosc_napis)), Opcja("Drakula", (szerokosc_napis2, wysokosc_napis + 3*roznica_wysokosc_napis )),
          Opcja("Róża",(szerokosc_napis2, wysokosc_napis + 4*roznica_wysokosc_napis )),Opcja("Wróć", (szerokosc_napis , wysokosc_napis + 6*roznica_wysokosc_napis ))]
opcje_opcje = [Opcja("Rozmiar", (szerokosc_napis , wysokosc_napis)), Opcja("Szybkość", (szerokosc_napis , wysokosc_napis + roznica_wysokosc_napis)),
               Opcja("Tryb", (szerokosc_napis , wysokosc_napis + 2*roznica_wysokosc_napis)), Opcja("Muzyka", (szerokosc_napis , wysokosc_napis + 3*roznica_wysokosc_napis)),
               Opcja("Wróć", (szerokosc_napis , wysokosc_napis + 6* roznica_wysokosc_napis))]
opcje_szybkosc = [Opcja("Normalny", (szerokosc_napis2, wysokosc_napis)), Opcja("Wolno", (szerokosc_napis2, wysokosc_napis + roznica_wysokosc_napis)),
                  Opcja("Bardzo wolno", (szerokosc_napis2, wysokosc_napis + 2*roznica_wysokosc_napis)),  Opcja("Szybko", (szerokosc_napis2, wysokosc_napis + 3*roznica_wysokosc_napis)),
                  Opcja("Bardzo szybko", (szerokosc_napis2, wysokosc_napis + 4*roznica_wysokosc_napis)), Opcja("Wróć", (szerokosc_napis , wysokosc_napis + 6* roznica_wysokosc_napis))]
opcje_rozmiar = [Opcja("Normalna", (szerokosc_napis2, wysokosc_napis)), Opcja("Mała", (szerokosc_napis2, wysokosc_napis + roznica_wysokosc_napis)),
                  Opcja("Bardzo mała", (szerokosc_napis2, wysokosc_napis + 2*roznica_wysokosc_napis)),  Opcja("Duża", (szerokosc_napis2, wysokosc_napis + 3*roznica_wysokosc_napis)),
                  Opcja("Bardzo duża", (szerokosc_napis2, wysokosc_napis + 4*roznica_wysokosc_napis)), Opcja("Wróć", (szerokosc_napis , wysokosc_napis + 6* roznica_wysokosc_napis))]
opcje_inne = [Opcja("Pauza", (szerokosc_napis , wysokosc_napis )),Opcja("Wróć", (szerokosc_napis , wysokosc_napis + 4*roznica_wysokosc_napis)),
              Opcja("Wyjdź", (szerokosc_napis , wysokosc_napis + 5*roznica_wysokosc_napis)), Opcja("Start", (szerokosc_napis , wysokosc_napis + 3*roznica_wysokosc_napis))]
opcje_tryby =  [Opcja("Conway's", (szerokosc_napis2, wysokosc_napis)), Opcja("Nasiona", (szerokosc_napis2, wysokosc_napis + roznica_wysokosc_napis)),
           Opcja("Labirynt", (szerokosc_napis2, wysokosc_napis + 2* roznica_wysokosc_napis)), Opcja("Miasta", (szerokosc_napis2, wysokosc_napis + 3*roznica_wysokosc_napis )),
           Opcja("Wolfram", (szerokosc_napis2, wysokosc_napis + 4*roznica_wysokosc_napis )), Opcja("Koral", (szerokosc_napis2, wysokosc_napis + 5*roznica_wysokosc_napis )),
                Opcja("Wróć", (szerokosc_napis , wysokosc_napis + 6*roznica_wysokosc_napis ))]
opcje_wzory = [Opcja("Szybowiec", (szerokosc_napis3, wysokosc_napis)), Opcja("Dakota", (szerokosc_napis3, wysokosc_napis + roznica_wysokosc_napis)),
           Opcja("Krokodyl", (szerokosc_napis3, wysokosc_napis + 2* roznica_wysokosc_napis)), Opcja("Pulsar", (szerokosc_napis3, wysokosc_napis + 3*roznica_wysokosc_napis )),
          Opcja("Działa",(szerokosc_napis3, wysokosc_napis + 4*roznica_wysokosc_napis )),Opcja("Wróć", (szerokosc_napis , wysokosc_napis + 6*roznica_wysokosc_napis ))]
opcje_muzyka = [Opcja("Włącz/wyłącz", (szerokosc_napis , wysokosc_napis)), Opcja("Głośniej", (szerokosc_napis , wysokosc_napis + roznica_wysokosc_napis)),
               Opcja("Ciszej", (szerokosc_napis , wysokosc_napis + 2*roznica_wysokosc_napis)), Opcja("Wróć", (szerokosc_napis , wysokosc_napis + 6* roznica_wysokosc_napis))]
guzik_opcje = False
guzik_wysokosc = guzik_paleta = guzik_rozmiar = guzik_szybkosc = guzik_tryb = guzik_wzory = (szerokosc_napis2, wysokosc_napis)
stan ="menu"
guzik_rozmiar_spr = False
guzik_wzor = False
muzyka = pygame.mixer.music
muzyka.load('song.mp3')
muzyka.play(-1)
muzyka_wlaczona = True
muzyka_glosnosc = 0.5
muzyka.set_volume(muzyka_glosnosc)
guzik_muzyka = False
zegar =pygame.time.Clock()
delta =0.0

#zmienne sterujące
zycie_trwa = False
przycisk_wdol = False
populacja = 0
martwa = 0
zywa = 1

class Komorka:

    def __init__(self, rozmiar):
        self.rozmiar = rozmiar
        self.poziom = int(szerokosc / rozmiar)
        self.pion = int(wysokosc / rozmiar)
        self.tablica()
    def tablica(self):
        self.gra = [martwa] * self.poziom
        for i in range(self.poziom):
            self.gra[i] = [martwa] * self.pion

komorka = Komorka(rozmiary[0])
komorka_menu= Komorka(rozmiary[0])
spr = komorka.gra
wzory(3, 0.16, 0.45)

intro(opcje)

