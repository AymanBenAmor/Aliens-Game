import pygame
from projectile import Projectile
import animation


class Player(animation.AnimateSprite):

    def __init__(self,game):
        super().__init__("player")
        self.game = game
        self.health = 160
        self.max_health = 160
        self.attack = 20
        self.velocity = 6
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 480

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.game_over()

    def update_animation(self):
        self.animate()

    def update_health_bar(self,surface):

        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x -15, self.rect.y - 25, self.max_health, 8])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x - 15, self.rect.y-25, self.health, 8])

    def launch_projectile(self):

        self.all_projectiles.add(Projectile(self))
        #self.start_animation()
        self.game.sound_manager.play('tir')



    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity