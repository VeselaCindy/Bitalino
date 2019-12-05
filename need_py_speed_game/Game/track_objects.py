import pygame, sys, os, random


class EnemyCar(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.positions = [[480, 350], [505, 350]]
        self.position_ambulance = [510, 350]
        self.position = random.choice(self.positions)
        path = './need_py_speed_game/Game/imagens/'
        self.objects = [pygame.image.load(path + 'adv_car.png'),
                        pygame.image.load(path + 'adv_car2.png'),
                        pygame.image.load(path + 'adv_car3.png'),
                        pygame.image.load(path + 'adv_car4.png'),
                        pygame.image.load(path + 'ambulance.png')]
        self.witch_object = random.choice(range(5))
        self.object = self.objects[self.witch_object]
        self.is_ambulance = False
        self.size_object_x = 80
        self.size_object_y = 80
        self.position_object_x = self.position[0]
        self.position_object_y = self.position[1]
        self.object_print = pygame.transform.scale(self.object, (self.size_object_x, self.size_object_y))
        self.rect_objeto = self.object_print.get_rect()
        self.rect_objeto.x, self.rect_objeto.y = self.position
        # self.mask = pygame.mask.from_surface(self.object)
        self.first = True

    def move_object(self, speed=0.1):

        if self.position == [505, 350]:
            self.position_object_x += 0.12 * (self.size_object_x / 10)
        elif self.position == [480, 350]:
            self.position_object_x -= 0.24 * (self.size_object_x / 10)

        self.position_object_y += speed * (self.size_object_y / 8)
        self.size_object_x += 1
        self.size_object_y += 1

        self.object_print = pygame.transform.scale(self.object, (self.size_object_x, self.size_object_y))
        self.rect_objeto = self.object_print.get_rect()
        self.rect_objeto.x, self.rect_objeto.y = (self.position_object_x, self.position_object_y)
        if self.position_object_y > 1200 or self.position_object_x > 2000 or self.position_object_x < -500:
            # self.witch_object = random.choice(self.objects)
            self.witch_object = random.choice(range(5))
            # self.object = pygame.image.load('./need_py_speed_game/Game/imagens' + os.sep + self.witch_object)
            self.is_ambulance = self.witch_object == 4
            self.object = self.objects[self.witch_object]
            self.position = random.choice(self.positions)
            self.size_object_x = 20
            self.size_object_y = 20
            if self.is_ambulance:
                self.position = self.position_ambulance
                self.size_object_x = 40
                self.size_object_y = 40
                self.position_object_x = self.position_ambulance[0]
                self.position_object_y = self.position_ambulance[1]
            else:
                self.position_object_y = self.position[1]
                self.position_object_x = self.position[0]
            self.first = True

            self.object_print = pygame.transform.scale(self.object, (self.size_object_x, self.size_object_y))
            self.rect_objeto = self.object_print.get_rect()
            self.rect_objeto.x, self.rect_objeto.y = (self.position_object_x, self.position_object_y)
        else:
            self.first = False

    def print_object(self):
        self.object_print = pygame.transform.scale(self.object, (self.size_object_x, self.size_object_y))
        self.screen.blit(self.object_print, (self.position_object_x, self.position_object_y))
        return self.is_ambulance, self.first
        # self.rect_objeto.normalize()
