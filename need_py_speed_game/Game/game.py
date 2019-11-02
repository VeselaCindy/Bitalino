# coding: utf-8

import pygame, os, sys, time, pickle
from pygame import *
import time as timer
from .stripes import *
from .car import *
from .trees import *
from .drink import *
from random import gauss
from .menu import *
from .traffic_lights_static import *

pygame.init()
game_introduction()


def random_time():
    return int(gauss(8, 2))


# Menu
def game():
    record = 0
    if root_menu():  # main menu
        pygame.mixer.music.load(
            './need_py_speed_game/Game/musicas' + os.sep + 'theme_song' + os.sep + random.choice(lista_musicas))
        screen = pygame.display.set_mode((1024, 768))
        screen = pygame.display.get_surface()
        bottom = pygame.image.load('./need_py_speed_game/Game/imagens' + os.sep + 'road.png')
        pygame.display.set_caption('CAR EMG GAME')
        clock = pygame.time.Clock()
        fuel = Fuel(screen)
        car = Car(screen)
        stripes = [Stripes(screen)]
        enemy_car = EnemyCar(screen)
        # traffic_lights = TrafficLights(screen)
        traffic_lights_static = TrafficLightStatic(screen)
        time_change = random_time()  # after some seconds change the lights
        right_trees = [Trees(screen, 'direita')]  # right trees
        left_trees = [Trees(screen, 'esquerda')]  # left trees
        pygame.key.set_repeat()

        i = 0
        score = 0
        # couter_show_lights_time = 100
        print_fuel = False
        show_fuel = False

        print_drink = False
        show_drink = False

        drink = Drink(screen)  # drink
        cont_drink = 0

        cont_fuel = 1
        car_speed = 20
        cont_score = 0
        cont_view = 20
        car_crash = False  # car crash

        # Music
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)

        start_time = timer.time()

        while True:
            clock.tick(20)
            if i % 200 == 0 and i != 0:
                print_fuel = True
                show_fuel = True

            # close or pause game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif pygame.key.get_pressed()[K_SPACE] and traffic_lights_static.color == "red":
                    pygame.mixer.music.pause()
                    song_pause.play(0)
                    result = menu_leave_game()
                    if result:
                        game()  # go to menu
                    elif result == False:
                        traffic_lights_static.change_to_green()
                        start_time = time.time()
                        time_change = random_time()
                    pygame.mixer.music.unpause()
            # for start the game
            """
            if first:
                screen.blit(bottom, (0, 0))
                traffic_lights_static.print_object()
                pygame.mixer.music.pause()
                song_pause.play(0)
                print("here")
                timer.sleep(5)
                print("after sleep")
                if start():
                    print("after first")
                    game()
                pygame.mixer.music.unpause()
            """
            key = pygame.key.get_pressed()
            car.move_car(key, car_speed)

            if i % 250 == 0:
                show_drink = True
                print_drink = True

            if i % 10 == 0 and len(right_trees) < 6:
                right_trees.append(Trees(screen, 'direita'))  # direita = right
                left_trees.append(Trees(screen, 'esquerda'))  # esquerda = left
                stripes.append(Stripes(screen))
            screen.blit(bottom, (0, 0))

            for j in range(len(right_trees)):  # right trees
                stripes[j].print_stripes(screen)
                right_trees[j].print_tree(screen)
                left_trees[j].print_tree(screen)
                enemy_car.print_object(screen)
            if show_fuel:
                fuel.print_fuel(screen)
            if show_drink:
                drink.print_drink(screen)

            car.print_car(screen)
            # change the color
            pom_time = timer.time() - start_time
            if pom_time > time_change and traffic_lights_static.color == "green":
                traffic_lights_static.change_to_red()

            if traffic_lights_static.color == "red":
                if pygame.key.get_pressed()[K_SPACE]:
                    pygame.mixer.music.pause()
                    song_pause.play(0)
                    if menu_leave_game():
                        game()
                    pygame.mixer.music.unpause()
                elif pom_time > time_change + 10:
                    game_over(score)

            traffic_lights_static.print_object()

            # Score
            font = pygame.font.Font('./need_py_speed_game/Game/fontes' + os.sep + 'nextwaveboldital.ttf', 55)
            texto_score = font.render("Score", True, BLACK)

            score = cont_score * 10
            texto_valor_score = font.render("%d" % score, True, BLACK)
            screen.blit(texto_score, [730, 15])
            screen.blit(texto_valor_score, [900, 15])

            # Bonus extra
            if int(score) % 5000 == 0 and score > 0:
                cont_view = 0
                cont_score += 5.0
                bonus = 10
                car_crash = False
                bonus_extra = True

            if cont_view < 20 and bonus_extra:
                font = pygame.font.Font('./need_py_speed_game/Game/fontes' + os.sep + 'WeareDepraved.ttf', 80)
                texto_bonus = font.render("YOU ARE FAST", True, GREEN)

                cor_font = GREEN
                score = cont_score * 15
                screen.blit(texto_bonus, [512 - texto_bonus.get_size()[0] / 2, 150])
            else:
                bonus_extra = False

            # Bonus
            if int(score) % 600 == 0 and score > 0:
                song_bonus1.play(0)
                cont_score += 2.0
                cont_view = 0
                bonus = 2
                cor_font = ORANGE
                car_crash = False

            if int(score) % 1000 == 0 and int(score) % 5000 != 0 and score > 0:
                song_bonus2.play(0)
                cont_score += 5.0
                cont_view = 0
                bonus = 5
                cor_font = RED
                car_crash = False

            if cont_view < 20:
                font = pygame.font.Font('./need_py_speed_game/Game/fontes' + os.sep + 'nextwaveboldital.ttf', 75)
                texto_good = font.render("+ %d0 BONUS" % bonus, True, cor_font)

                screen.blit(texto_good, [320, 80])
                cont_view += 1

            if cont_fuel < 96:
                font = pygame.font.Font('./need_py_speed_game/Game/fontes' + os.sep + 'nextwaveboldital.ttf', 50)
                texto_gasolina = font.render("FUEL", True, BLACK)
                screen.blit(texto_gasolina, [10, 10])
                pygame.draw.rect(screen, BLACK, [50, 55, 20, 100], 3)
                pygame.draw.rect(screen, RED, [52, 57, 16, 96], 0)
                pygame.draw.rect(screen, WHITE, [52, 57, 16, cont_fuel], 0)
                cont_fuel += 0.1
            else:
                pygame.mixer.music.stop()
                song_game_over.play(0)
                if game_over(score):
                    game()

            pygame.display.update()

            car_rect = car.rect_car.inflate(-50, -50)
            enemy_car_rect = enemy_car.rect_objeto.inflate(-30, -30)
            fuel_rect = fuel.rect_fuel.inflate(-20, -20)
            drink_rect = drink.rect_comb.inflate(-10, -10)

            # Collision with car
            if car_rect.colliderect(enemy_car_rect):
                pygame.mixer.music.stop()
                song_game_over.play(0)
                if game_over(score):
                    game()

            # Collision with fuel
            if fuel_rect.colliderect(car.rect_car):
                song_bonus1.play(0)
                Comb = 1000
                show_fuel = False

                cont_fuel -= 1
                cont_view = 0
                car_crash = True

            # crash with drink
            if car_rect.colliderect(drink_rect):
                song_drink.play(0)
                car_speed = 10
                cont_drink = 0
                show_drink = False

            if cont_view < 15 and car_crash:
                cont_score += 1.0
                bonus = 1
                cor_font = YELLOW

            for j in range(len(right_trees)):
                right_trees[j].move_tree('direita')
                left_trees[j].move_tree('esquerda')
                stripes[j].mover_stripes()
                enemy_car.move_object()
                if print_fuel:
                    print_fuel = fuel.move_fuel(print_fuel)
                if print_drink:
                    print_drink = drink.move_drink(print_drink)

            i += 1
            cont_score += 0.1

            # drink effect
            if cont_drink == 75:
                car_speed = 20  # speed car
            cont_drink += 1
