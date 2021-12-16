import pygame

FPS = 120

WIDTH = 1000
HEIGHT = 600

WHITE = (255,255,255)
BLUE = (40, 148, 255)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("第一個遊戲")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50.40))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 200

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BLUE)
    all_sprites.draw(screen)
    pygame.display.update()
pygame.quit()