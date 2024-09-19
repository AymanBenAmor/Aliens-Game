import pygame
import math
from game2 import Game
pygame.init()

clock = pygame.time.Clock()
FPS = 60



pygame.display.set_caption('Comet fall Game')
screen = pygame.display.set_mode((1200,720))


backround=pygame.image.load("assets/bg.jpg")

creator = pygame.image.load("assets/creator.png")
creator = pygame.transform.scale(creator, (300,100))
creator_rect = creator.get_rect()

banner = pygame.image.load("assets/banner.png")
banner = pygame.transform.scale(banner, (550,400))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)
banner_rect.y = 40

play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button, (350,120))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.155)
play_button_rect.y = math.ceil(screen.get_height() / 1.5)



game = Game()


running = True

while running:

    screen.blit(backround, (0,-200))

    if game.is_playing:
        game.update(screen)

    else:
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)
        screen.blit(creator, creator_rect )


    pygame.display.flip()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()
                else:
                    game.start()
                    game.sound_manager.play('click')


        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()
                game.sound_manager.play('click')

    clock.tick(FPS)



