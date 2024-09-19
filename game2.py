import pygame
from player import Player
from monster import Monster
from monster import Mummy
from monster import Alien
from comet_event import CometFallEvent
from sounds import SoundManager

class Game :
    def __init__(self):
        self.is_playing = False
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.comet_event = CometFallEvent(self)
        self.all_monsters = pygame.sprite.Group()
        self.sound_manager = SoundManager()
        self.font = pygame.font.Font("assets/my_custom_font.ttf", 25)
        self.score = 0
        self.pressed = {}


    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def add_score(self, points=10):
        self.score += points


    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False
        self.score = 0
        self.sound_manager.play('game_over')

    def update(self, screen):


        score_texte = self.font.render(f"score : {self.score}", 1, (0,0,0))
        screen.blit(score_texte, (20, 20))


        screen.blit(self.player.image, self.player.rect)

        self.player.update_health_bar(screen)

        self.comet_event.update_bar(screen)

        self.player.update_animation()

        for projectile in self.player.all_projectiles:
            projectile.move()

        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        for comet in self.comet_event.all_comets:
            comet.fall()

        self.player.all_projectiles.draw(screen)

        self.all_monsters.draw(screen)

        self.comet_event.all_comets.draw(screen)

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 1037:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self,sprite , group):
        return pygame.sprite.spritecollide(sprite, group , False , pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))