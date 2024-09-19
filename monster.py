import pygame
import random
import animation


class Monster(animation.AnimateSprite):

    def __init__(self,game, name, size, offset=0):
        super().__init__(name,size)
        self.health = 160
        self.max_health = 160
        self.attack = 0.5
        self.game = game
        self.rect = self.image.get_rect()
        self.rect.x = 1120 + random.randint(0, 300)
        self.rect.y = 490 - offset
        self.loot_amount = 10
        self.start_animation()

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(2, 3)

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def damage(self, amount):
        self.health -= amount

        if self.health <= 0:
            self.rect.x = 1120 + random.randint(0, 300)
            self.velocity = random.randint(1,self.default_speed)
            self.health = self.max_health

            self.game.add_score(self.loot_amount)

            if self.game.comet_event.is_full_loaded():
                self.game.all_monsters.remove(self)

                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self,surface):

        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x - 20, self.rect.y - 20, self.max_health, 8])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x - 20, self.rect.y-20, self.health, 8])





    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else :
            self.game.player.damage(self.attack)


class Mummy(Monster):

    def __init__(self, game):
        super().__init__(game, "mummy", (130,200))
        self.set_speed(2)
        self.set_loot_amount(20)

class Alien(Monster):

    def __init__(self, game):
        super().__init__(game, "alien", (300,300),100)
        self.health = 400
        self.max_health = 400
        self.attack = 0.8
        self.set_speed(2)
        self.set_loot_amount(80)