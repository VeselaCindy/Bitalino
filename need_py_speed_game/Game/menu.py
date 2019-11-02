# coding: utf-8

import os, sys, time, random, pickle
import pygame as pg
from pygame import *
from .sounds_effects import *
from .traffic_lights_static import *

pg.init()


def game_introduction():
    import time
    def position_image_start(imagem, tam_tela):
        largura_imagem, altura_imagem = imagem.get_size()
        largura, altura = tam_tela
        return [(largura / 2) - (largura_imagem / 2), (altura / 2) - (altura_imagem / 2)]

    # load sons
    pg.mixer.pre_init(44100, -16, 2, 2048)
    pg.mixer.music.load('./need_py_speed_game/Game/musicas' + os.sep + 'Tema_PS2.mp3')
    pg.mixer.music.play(1)

    # Load image
    vut = pg.image.load('./need_py_speed_game/Game/imagens' + os.sep + 'vut.png').convert()
    # cc = pg.image.load('./need_py_speed_game/Game/imagens' + os.sep + 'logo_computacao.jpg').convert()
    logo_jogo = pg.image.load('./need_py_speed_game/Game/imagens' + os.sep + 'logo_jogo.jpg').convert()

    # Load Fonts
    fonte = pg.font.Font('./need_py_speed_game/Game/fontes' + os.sep + 'btseps2.TTF', 200)
    texto_apresentacao = fonte.render("Car game", True, WHITE)
    screen.fill(WHITE)
    screen.blit(vut, position_image_start(vut, size))
    pg.display.update()
    time.sleep(2)

    screen.fill(BLACK)
    screen.blit(texto_apresentacao, position_image_start(texto_apresentacao, size))
    pg.display.update()
    time.sleep(2)


def source_position(imagem, pos_inicial):
    x, y = pg.mouse.get_pos()
    largura, altura = imagem.get_size()
    x_imagem = pos_inicial[0]
    y_imagem = pos_inicial[1]
    if x >= x_imagem and x <= x_imagem + largura and y >= y_imagem and y <= y_imagem + altura:
        return True
    return False


def menu_reset():
    while True:
        menu = pg.image.load('./need_py_speed_game/Game/imagens' + os.sep + 'menu_configuracoes.jpg').convert()
        screen.blit(menu, [0, 0])
        pg.draw.rect(screen, WHITE, [100, 600, 10, 50], 0)

        fonte_menu1 = pg.font.Font('./need_py_speed_game/Game/fontes' + os.sep + 'Staubach.ttf', 45)
        fonte_menu2 = pg.font.Font('./need_py_speed_game/Game/fontes' + os.sep + 'Staubach.ttf', 55)

        texto1 = fonte_menu1.render('Rekordy budou vymazane.', True, BLUE_2)
        texto2 = fonte_menu1.render('Opravdu chcete pokracovat?', True, BLUE_2)
        texto3 = fonte_menu2.render('ANO', True, BLUE_2)
        texto4 = fonte_menu2.render('NE', True, BLUE_2)

        screen.blit(texto1, [(largura_tela / 2) - (texto1.get_size()[0] / 2), 250])
        screen.blit(texto2, [(largura_tela / 2) - (texto2.get_size()[0] / 2), 300])
        screen.blit(texto3, [400, 384])
        screen.blit(texto4, [550, 384])

        if source_position(texto3, [400, 384]):
            screen.blit(fonte_menu2.render('ANO', True, RED), [400, 384])
        elif source_position(texto4, [550, 384]) or pg.key.get_pressed()[K_ESCAPE]:
            screen.blit(fonte_menu2.render('NE', True, RED), [550, 384])

        for event in pg.event.get():
            if (pg.mouse.get_pressed()[0] and source_position(texto3, [400, 384])):
                with open('./need_py_speed_game/Game/salve_recordes' + os.sep + 'save_record.dat', 'wb') as f:
                    pickle.dump(0, f, 2)
                return True
            elif (pg.mouse.get_pressed()[0] and source_position(texto4, [550, 384])) or pg.key.get_pressed()[
                K_ESCAPE]:
                song_come_back.play(0)
                return True
            elif event.type == pg.QUIT:
                sys.exit()

        pg.display.update()


def menu_record():
    # load Record
    with open('./need_py_speed_game/Game/salve_recordes' + os.sep + 'save_record.dat', 'rb') as f:
        record = pickle.load(f)

    menu = pg.image.load('./need_py_speed_game/Game/imagens' + os.sep + 'menu_recorde.jpg')
    fonte_menu1 = pg.font.Font('./need_py_speed_game/Game/fontes' + os.sep + 'Staubach.ttf', 70)
    fonte_menu2 = pg.font.Font('./need_py_speed_game/Game/fontes' + os.sep + 'Staubach.ttf', 50)

    texto1 = fonte_menu1.render('REKORD', True, BLUE_2)
    texto2 = fonte_menu2.render('Nejlepsi skore  =  %d' % record, True, BLUE_2)
    texto3 = fonte_menu1.render('Zpet', True, BLUE_2)

    while True:
        screen.blit(menu, [0, 0])
        screen.blit(texto1, [(largura_tela / 2) - (texto1.get_size()[0] / 2), 20])
        screen.blit(texto2, [20, 200])
        screen.blit(texto3, [750, 650])

        if source_position(texto3, [750, 650]) or pg.key.get_pressed()[K_ESCAPE]:
            screen.blit(fonte_menu1.render('Zpet', True, RED), [750, 650])

        for event in pg.event.get():
            if (pg.mouse.get_pressed()[0] and source_position(texto3, [750, 650])) or pg.key.get_pressed()[
                K_ESCAPE]:
                song_come_back.play(0)
                return True
            elif event.type == pg.QUIT:
                sys.exit()

        pg.display.update()


# Menu Credits
def menu_credits():
    menu = pg.image.load('./need_py_speed_game/Game/imagens' + os.sep + 'fundo_menu4.jpg')
    fonte_menu3 = pg.font.Font('./need_py_speed_game/Game/fontes' + os.sep + 'WeareDepraved.ttf', 70)
    fonte_menu4 = pg.font.Font('./need_py_speed_game/Game/fontes' + os.sep + 'WeareDepraved.ttf', 55)

    texto1 = fonte_menu3.render('Kredity', True, BLUE_2)
    texto2 = fonte_menu4.render('Vyvoj', True, BLUE)
    texto3 = fonte_menu4.render('NATAN MACENA RIBEIRO', True, BLUE)
    texto4 = fonte_menu4.render('RONAN DE ARAUJO SOUZA', True, BLUE)
    texto5 = fonte_menu4.render('AGRADECIMENTOS', True, BLUE)
    texto6 = fonte_menu4.render('LUIZ AUGUSTO MORAIS', True, BLUE)
    texto7 = fonte_menu4.render('DALTON DARIO SEREY GUERRERO', True, BLUE)
    texto8 = fonte_menu4.render('Opravneni', True, BLUE)
    texto9 = fonte_menu3.render('Zpet', True, BLUE_2)

    while True:

        screen.blit(menu, [0, 0])
        screen.blit(texto1, [(largura_tela / 2) - (texto1.get_size()[0] / 2), 30])
        screen.blit(texto2, [40, 150])
        screen.blit(texto3, [90, 250])
        screen.blit(texto4, [90, 310])
        screen.blit(texto5, [40, 410])
        screen.blit(texto6, [90, 510])
        screen.blit(texto7, [90, 570])
        screen.blit(texto8, [90, 630])
        screen.blit(texto9, [800, 690])

        if source_position(texto9, [800, 690]) or pg.key.get_pressed()[K_ESCAPE]:
            screen.blit(fonte_menu3.render('Zpet', True, RED), [800, 690])

        for event in pg.event.get():
            if (pg.mouse.get_pressed()[0] and source_position(texto9, [800, 690])) or pg.key.get_pressed()[
                K_ESCAPE]:
                song_come_back.play(0)
                return True
            elif event.type == pg.QUIT:
                sys.exit()

        pg.display.update()


# Menu help
def menu_help():
    menu = pg.image.load('./need_py_speed_game/Game/imagens' + os.sep + 'menu_ajuda.jpg')
    tecla1 = pg.image.load('./need_py_speed_game/Game/imagens' + os.sep + 'computer_key_Arrow_Left.png')
    tecla2 = pg.image.load('./need_py_speed_game/Game/imagens' + os.sep + 'computer_key_Arrow_Right.png')
    tecla3 = pg.image.load('./need_py_speed_game/Game/imagens' + os.sep + 'computer_key_Esc.png')
    fonte_menu3 = pg.font.Font('./need_py_speed_game/Game/fontes' + os.sep + 'Staubach.ttf', 65)
    fonte_menu4 = pg.font.Font('./need_py_speed_game/Game/fontes' + os.sep + 'Staubach.ttf', 50)

    texto1 = fonte_menu3.render('Napoveda', True, YELLOW)

    texto2 = fonte_menu4.render('Ovladani hry', True, ORANGE)
    texto3 = fonte_menu4.render('Vyhybejte se autum', True, ORANGE)
    texto4 = fonte_menu4.render('Zastavte co nejrchleji na cervenou', True, ORANGE)
    texto5 = fonte_menu4.render('Je potřeba udrzet plnou nádrz.', True, ORANGE)
    texto6 = fonte_menu4.render('Palivo doplníte, pokud seberete benzín', True, ORANGE)

    texto7 = fonte_menu4.render('Jak se hra ovládá?', True, ORANGE)
    texto8 = fonte_menu4.render('Rízení auta: vlevo/vpravo', True, ORANGE)
    texto9 = fonte_menu4.render('Pauza / Hra', True, ORANGE)

    texto10 = fonte_menu3.render('Zpet', True, YELLOW)
    while True:
        screen.blit(menu, [0, 0])
        screen.blit(pg.transform.scale(tecla1, [50, 50]), [20, 480])
        screen.blit(pg.transform.scale(tecla2, [50, 50]), [80, 480])
        screen.blit(pg.transform.scale(tecla3, [50, 50]), [20, 550])
        screen.blit(texto1, [(largura_tela / 2) - (texto1.get_size()[0] / 2), 10])
        screen.blit(texto2, [20, 100])
        screen.blit(texto3, [40, 170])
        screen.blit(texto4, [40, 220])
        screen.blit(texto5, [40, 270])
        screen.blit(texto6, [40, 320])

        screen.blit(texto7, [20, 390])
        screen.blit(texto8, [150, 460])
        screen.blit(texto9, [150, 530])

        screen.blit(texto10, [730, 650])

        if source_position(texto10, [730, 650]) or pg.key.get_pressed()[K_ESCAPE]:
            screen.blit(fonte_menu3.render('Zpet', True, RED), [730, 650])

        for event in pg.event.get():
            if (pg.mouse.get_pressed()[0] and source_position(texto9, [730, 650])) or pg.key.get_pressed()[
                K_ESCAPE]:
                song_come_back.play(0)
                return True
            elif event.type == pg.QUIT:
                sys.exit()

        pg.display.update()


# after pause game
def menu_leave_game(red_for_sec=5, first=False):
    if first:
        bottom = pg.image.load('./need_py_speed_game/Game/imagens' + os.sep + 'road.png')
        screen.blit(bottom, (0, 0))
    escape = 0
    traffic_lights = TrafficLightStatic(screen, "red")
    start_time = time.time()
    font_text = pg.font.Font('./need_py_speed_game/Game/fontes' + os.sep + 'nextwaveboldital.ttf', 100)
    text_waiting = font_text.render("Pockej na zelenou", True, BLACK)
    # semi transparent
    s = pygame.Surface((1024, 150))  # size
    s.set_alpha(150)
    s.fill((255, 255, 255))  # this fills the entire surface
    screen.blit(s, (0, 350))  # draw

    while True:
        screen.blit(text_waiting, [(512 - text_waiting.get_size()[0] / 2), 400])
        if time.time() - start_time > red_for_sec and traffic_lights.color == "red":
            traffic_lights.change_to_green()
        traffic_lights.print_object()

        for event in pg.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif pygame.key.get_pressed()[K_SPACE] and traffic_lights.color == "green":
                return False
            elif pygame.key.get_pressed()[K_ESCAPE]:
                song_come_back.play(0)
                return True
            elif escape > 1000000:
                return True

        pg.display.update()
        escape += 1


# Game Over
def game_over(score):
    score = int(score)
    print_record = False

    # load records
    with open('./need_py_speed_game/Game/salve_recordes' + os.sep + 'save_record.dat', 'rb') as f:
        record = pickle.load(f)

    if score > record:
        record = score
        # save record
        with open('./need_py_speed_game/Game/salve_recordes' + os.sep + 'save_record.dat', 'wb') as f:
            pickle.dump(score, f, 2)
            print_record = True

            fonte_record = pg.font.Font('./need_py_speed_game/Game/fontes' + os.sep + 'nextwaveboldital.ttf', 90)
            texto_record = fonte_record.render("NEW RECORD", True, ORANGE_2)
            texto_score = fonte_record.render("%d" % record, True, ORANGE_2)

    while True:
        fonte_fim = pg.font.Font('./need_py_speed_game/Game/fontes' + os.sep + 'JUSTFIST2.ttf', 70)
        texto_fim = fonte_fim.render("GAME OVER", True, RED)
        screen.blit(texto_fim, [(1024 / 2) - (texto_fim.get_size()[0] / 2), 300])
        if print_record:
            screen.blit(texto_record, [(1024 / 2) - (texto_record.get_size()[0] / 2), 300])
            screen.blit(texto_score, [(1024 / 2) - (texto_score.get_size()[0] / 2), 350])

        pg.display.update()
        pg.time.delay(6000)
        return True


# Menu Principal
def root_menu():
    # Load fonts
    fonte_menu = pg.font.Font('./need_py_speed_game/Game/fontes' + os.sep + 'VirtualBliss.ttf', 70)
    fonte_menu2 = pg.font.Font('./need_py_speed_game/Game/fontes' + os.sep + 'VirtualBliss.ttf', 65)

    text_menu = fonte_menu.render("CAR GAME", True, YELLOW)

    sub_texto_menu1 = fonte_menu2.render("Hrat", True, YELLOW)
    sub_texto_menu2 = fonte_menu2.render("Napoveda", True, YELLOW)
    sub_texto_menu3 = fonte_menu2.render("Rekord", True, YELLOW)
    sub_texto_menu4 = fonte_menu2.render("Kredity", True, YELLOW)
    sub_texto_menu5 = fonte_menu2.render("Smazat zaznamy", True, YELLOW)
    sub_texto_menu6 = fonte_menu2.render("Konec", True, YELLOW)

    # Som do menu
    pg.mixer.pre_init(44100, -16, 2, 2048)
    pg.mixer.music.load('./need_py_speed_game/Game/musicas' + os.sep + random.choice(listas_musicas_menu))
    pg.mixer.music.play(-1)
    pg.mixer.music.set_volume(1)

    menu = pg.image.load('./need_py_speed_game/Game/imagens' + os.sep + 'fundo_menu.jpg')
    while True:
        # Imagem do menu
        screen.blit(menu, [0, 0])
        screen.blit(text_menu, [(largura_tela / 2) - (text_menu.get_size()[0] / 2), 30])
        screen.blit(sub_texto_menu1, [40, 150])
        screen.blit(sub_texto_menu2, [40, 250])
        screen.blit(sub_texto_menu3, [40, 350])
        screen.blit(sub_texto_menu4, [40, 450])
        screen.blit(sub_texto_menu5, [40, 550])
        screen.blit(sub_texto_menu6, [40, 650])

        if source_position(sub_texto_menu1, [40, 150]):
            screen.blit(fonte_menu2.render("Hrat", True, RED), [40, 150])
        elif source_position(sub_texto_menu2, [40, 250]):
            screen.blit(fonte_menu2.render("Napoveda", True, RED), [40, 250])
        elif source_position(sub_texto_menu3, [40, 350]):
            screen.blit(fonte_menu2.render("Rekord", True, RED), [40, 350])
        elif source_position(sub_texto_menu4, [40, 450]):
            screen.blit(fonte_menu2.render("Kredity", True, RED), [40, 450])
        elif source_position(sub_texto_menu5, [40, 550]):
            screen.blit(fonte_menu2.render("Smazat zaznamy", True, RED), [40, 550])
        elif source_position(sub_texto_menu6, [40, 650]):
            screen.blit(fonte_menu2.render("Konec", True, RED), [40, 650])

        for event in pg.event.get():
            if pg.mouse.get_pressed()[0] and source_position(sub_texto_menu1, [40, 150]):
                song_menu2.play(0)
                pg.mixer.music.stop()
                return True
            elif pg.mouse.get_pressed()[0] and source_position(sub_texto_menu2, [40, 250]):
                song_menu1.play(0)
                if menu_help():
                    continue
            elif pg.mouse.get_pressed()[0] and source_position(sub_texto_menu3, [40, 350]):
                song_menu1.play(0)
                if menu_record():
                    continue
            elif pg.mouse.get_pressed()[0] and source_position(sub_texto_menu4, [40, 450]):
                song_menu1.play(0)
                if menu_credits():
                    continue
            elif pg.mouse.get_pressed()[0] and source_position(sub_texto_menu5, [40, 550]):
                song_menu1.play(0)
                if menu_reset():
                    continue
            elif pg.mouse.get_pressed()[0] and source_position(sub_texto_menu6, [40, 650]):
                sys.exit()
            elif event.type == pg.QUIT:
                sys.exit()

        pg.display.update()


# Configuration screen
size = largura_tela, altura_leta = (1024, 768)
screen = pg.display.set_mode(size)
pg.display.set_caption('EMG game')

# Load cores
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
ORANGE_2 = (251, 79, 12)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
BLUE = (51, 181, 205)
BLUE_2 = (0, 0, 255)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
GRAY2 = (190, 190, 190)
