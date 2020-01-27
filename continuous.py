import pygame
import random
import math
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)


#def deathscreen():

#This is object code for most sprites - including player, wooden blocks, final blocks, killer blocks, blouncy blocks 
class Block (pygame.sprite.Sprite):
    def __init__(self, image, width = 50, height = 50):                                          #width and height are for how large you want the block
        pygame.sprite.Sprite.__init__(self)
        self.width = width                                                                          #this and next is so that I can use/change these attributes in methods of this object
        self.height = height
        self.OG_image = pygame.transform.scale(pygame.image.load(image), (self.width,self.height))  #this is the original image, which i use when the object is turned (as if constantly changing same image, it will deform)
        self.center = self.OG_image.get_rect().center                                               #this is used to reposition the image so that when turned it, turns around center
        self.rect = self.OG_image.get_rect(center = self.center)                                    #this is used to change the image x,y coords
        self.image_angle = random.randrange(0,360)                                                  #used to make the image the angle that it is meant to be turned
        self.image = pygame.transform.rotate(self.OG_image, self.image_angle)

class Player (Block):
    def __init__(self, width, height, image):
        Block.__init__(self, width, height, image)   
    def spin(self):
        self.image_angle += speed                                                                           #this adds the variable speed onto image_angle, speed will increase
        self.image = pygame.transform.rotate(self.OG_image, self.image_angle)                               #this is the image that will end up on the screen, (turned by the image_angle)
        self.rect = self.image.get_rect(center = self.center)                                               #this is what makes the image look like it is turning via its center
    def move(self):
        rad = math.radians(self.image_angle)                                                                #radian version of angle as that is version needed for library math.
        self.rect.x += math.sin(rad)*speed*-1                                                               #
        self.rect.y += math.cos(rad)*speed*-1                                                               #moving the object in direction it is pointing
        self.center = (self.center[0] + math.sin(rad)*speed*-1, self.center[1] + math.cos(rad)*speed*-1)    # changing the position of the center, so that it is in motion with the harpoon

speed = 10                                                                             #starting speed of harpoon
screen_width = 700                                                                     #size of the screen
screen_height = 500
screen = pygame.display.set_mode([screen_width,screen_height])                         #setting up screen
font = pygame.font.SysFont('Calibri', 30, True, False)                                 

blocks = pygame.sprite.Group()                                                         #group so that goup collide can be used
block_list = []
trail = []
all_sprites_list = pygame.sprite.Group()


for i in range(4):
    block = Block("wood.jpg")
    block.rect.x = random.randrange(0,650)
    block.rect.y = (i*200) - 400
    block.OG_image = pygame.transform.scale(pygame.image.load("wood.jpg"), (20, 20))
    blocks.add(block)
    block_list.append(block)
    all_sprites_list.add(block)

target = 3
player = Player(50, 50, "harpoongun.png")
player.rect.x = 325
player.rect.y = 300
player.center = (325,300)
player.OG_image = pygame.transform.scale(pygame.image.load("harpoongun.png"), (50,50))
all_sprites_list.add(player)

all_sprites_list.draw(screen)
spin = False
move = False
done = False
spinable = True
start = False
clock = pygame.time.Clock()
score = 0

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and spinable == True:
        player.spin()
        spin = True
    elif (spin == True and event.type != pygame.KEYDOWN) or (move == True):
        spin = False
        move = True
        spinable = False
        start = True
        player.move()

    speed = score//5 + 5
    screen.fill(WHITE)
    
    blocks_hit = pygame.sprite.spritecollide(player,blocks,False)
    if len(blocks_hit) > 0:
        if blocks_hit[-1] == block_list[target]:
            block_list[target].rect.x = random.randrange(0, 650)
            block_list[target].rect.y -= 800
            target -= 1
            if target == -1:
                target = 3
            score += 1
            print(score)
            spinable = True
            move = False
            player.image_angle = random.randrange(0, 360)
        else:
            done = True

    if start == True:
        for sprite in all_sprites_list:
            sprite.rect.y += (speed-4)
            sprite.center = (sprite.center[0], sprite.center[1] + (speed-4))

    if (player.rect.x > 680 or player.rect.x < 0 or player.rect.y > 480 or player.rect.y < 0):
        done = True
        
    all_sprites_list.draw(screen)
    word = font.render("score:" + str(score), True, BLACK)
    screen.blit(word, (600, 10))
    
    clock.tick(20)
    pygame.display.flip()

pygame.quit()
    
