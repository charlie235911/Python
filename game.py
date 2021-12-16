import pygame
import random

FPS = 120

WIDTH = 1000
HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (40, 148, 255)

#遊戲初始化 and 創建視窗
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("拔水母頭遊戲")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 900 
        self.rect.y = 500

    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += 2
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= 2
        if key_pressed[pygame.K_UP]:
            self.rect.y -= 2
        if key_pressed[pygame.K_DOWN]:
            self.rect.y += 2
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class Jellyfish(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height)

all_sprites = pygame.sprite.Group()
for i in range(8):
    jellyfish = Jellyfish()
    all_sprites.add(jellyfish)
player = Player()
all_sprites.add(player)


#遊戲迴圈
running = True
while running:
    clock.tick(FPS)
    #取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #更新遊戲
    all_sprites.update()

    #畫面顯示
    screen.fill(BLUE)
    all_sprites.draw(screen)
    pygame.display.update()
pygame.quit()