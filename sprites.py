import pygame
import random
import math

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

class Block (pygame.sprite.Sprite):
    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.OG_image = pygame.Surface([width,height])
        self.image_angle = random.randrange(0,360)
        self.image = pygame.transform.rotate(self.OG_image, self.image_angle)
        self.rect = self.image.get_rect()
    def spin(self):
        self.image_angle += 2
        self.image = pygame.transform.rotate(self.OG_image, self.image_angle)
    def move(self):
        angle = self.image_angle
        self.rect.x += math.sin(self.image_angle)*speed
        self.rect.y += math.cos(self.image_angle)*speed
        

pygame.init()

speed = 10
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width,screen_height])

block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

for i in range(4):
    block = Block(20,15)
    block.rect.x = random.randrange(0,650)
    block.rect.y = i*100
    block.OG_image = pygame.transform.scale(pygame.image.load("wood.jpg"), (100, 100))
    block_list.add(block)
    all_sprites_list.add(block)

player = Block(20, 20)
player.rect.x = 50
player.rect.y = 50

player.OG_image = pygame.transform.scale(pygame.image.load("harpoongun.png"), (50,50))
all_sprites_list.add(player)

spin = False
move = False
done = False
clock = pygame.time.Clock()
score = 0

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        player.spin()
        spin = True
    elif (spin == True and event.type != pygame.KEYDOWN and event.key == pygame.K_SPACE) or (move == True):
        spin = False
        move = True
        player.move()

    
    screen.fill(white)
    
    block_hit_list = pygame.sprite.spritecollide(player,block_list,True)
    
    for block in block_hit_list:
        score += 1
        print(score)
    
    all_sprites_list.draw(screen)
    
    clock.tick(20)
    
    pygame.display.flip()

pygame.quit()
    
