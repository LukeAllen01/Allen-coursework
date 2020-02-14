import pygame
import random
import math
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)


def deathscreen():
    pygame.draw.rect(screen, BLACK, 200,50, 300, 400, 2)
    

#This is object code for most sprites - including player, wooden blocks, final blocks, killer blocks, blouncy blocks 
class Block (pygame.sprite.Sprite):
    def __init__(self, image, width = 50, height = 50):
        #width and height are for how large you want the block
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        #this and next is so that I can use/change these attributes in methods of this object
        self.height = height
        self.OG_image = pygame.transform.scale(pygame.image.load(image), (self.width,self.height))
        self.image_angle = random.randrange(0,360)
        #used to make the image the angle that it is meant to be turned
        self.image = pygame.transform.rotate(self.OG_image, self.image_angle)
        #this is the original image, which i use when the object is turned (as if constantly changing same image, it will deform)
        self.center = self.OG_image.get_rect().center
        #this is used to change the image x,y coords
        #this is used to reposition the image so that when turned it, turns around center
        self.rect = self.OG_image.get_rect(center = self.center)

class Player (Block):
    def __init__(self, image):
        Block.__init__(self, image)   
    def spin(self):
        self.image_angle += speed
        #this adds the variable speed onto image_angle, speed will increase
        self.image = pygame.transform.rotate(self.OG_image, self.image_angle)
        #this is the image that will end up on the screen, (turned by the image_angle)
        self.rect = self.image.get_rect(center = self.center)
        #this is what makes the image look like it is turning via its center
    def move(self):
        rad = math.radians(self.image_angle)                                                                #radian version of angle as that is version needed for library math.
        self.rect.x += math.sin(rad)*speed*-1                                                               #
        self.rect.y += math.cos(rad)*speed*-1                                                               #moving the object in direction it is pointing
        self.center = (self.center[0] + math.sin(rad)*speed*-1, self.center[1] + math.cos(rad)*speed*-1)    # changing the position of the center, so that it is in motion with the harpoon

def fade():
    move = False
    for i in all_sprites_list:
        for x in range(100):
            i.image.set_alpha(x)
            
    if background_colour[0] > 200:
        background_colour[0] = background_colour[0] -1
    elif background_colour[0] < 200:
        background_colour[0] = background_colour[0] + 1
    if background_colour[1] > 200:
        background_colour[1] = background_colour[0] -1
    elif background_colour[1] < 200:
        background_colour[1] = background_colour[0] + 1
    if background_colour[2] > 200:
        background_colour[2] = background_colour[0] -1
    elif background_colour[2] < 200:
        background_colour[2] = background_colour[0] + 1

background_colour = [255,255,255] 
speed = 10                                                                             #starting speed of harpoon
screen_width = 700                                                                     #size of the screen
screen_height = 500
screen = pygame.display.set_mode([screen_width,screen_height])
    #setting up screen
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
player = Player("harpoongun.png")
player.rect.x = 325
player.rect.y = 300
player.center = (325,300)
player.OG_image = pygame.transform.scale(pygame.image.load("harpoongun.png"), (50,50))
all_sprites_list.add(player)

spin = False
move = False
done = False
spinable = True
start = False
clock = pygame.time.Clock()
score = 0

while done == False:
    #this makes a continuous loop until done equals True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #this sees what all the inputs are and if one is to close window then stops loop
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and spinable == True:
        player.spin()
        spin = True
    #this detects whether a key is pressed, if that key is SPACE bar and whether player is allowed to spin
    elif (spin == True and event.type != pygame.KEYDOWN) or (move == True):
        spin = False
        move = True
        spinable = False
        start = True
        player.move()
    #this detects if no key is pressed and spin = True, or it was moving last loop
    speed = score//5 + 5
    #increases speed
    screen.fill(background_colour)
    
    blocks_hit = pygame.sprite.spritecollide(player,blocks,False)
    #adds any blocks that have been hit by the player to blocks_hit
    if len(blocks_hit) > 0:
        #checks if anything has been hit
        if blocks_hit[-1] == block_list[target]:
            #checks if the last block entered was the targeted block
            block_list[target].rect.x = random.randrange(0, 650)
            block_list[target].rect.y -= 800
            #puts the block higher that it looks like a constant stream of blocks
            target -= 1
            if target == -1:
                target = 3
            #changes target to next one
            score += 1
            #add 1 to score
            print(score)
            spinable = True
            #allow player to spin again
            move = False
            #stops player from moving
        else:
            done = True
        # for moment this stops game if wrong block hit
    if start == True:
        for sprite in all_sprites_list:
            sprite.rect.y += (speed-4)
            sprite.center = (sprite.center[0], sprite.center[1] + (speed-4))
    #makes all srites move down screen by spped
    if (player.rect.x > 720 or player.rect.x < -20 or player.rect.y > 520 or player.rect.y < -20):
        fade()
        #if player hits side of screen they dead
    for i in blocks:
        if i.rect.y > 520:
            i.rect.y = i.rect.y - 800
            i.rect.x = randomrange(0,650)
    all_sprites_list.draw(screen)
    #shows all sprites
    word = font.render("score:" + str(score), True, BLACK)
    #writes score on top right corner
    screen.blit(word, (600, 10))
    #makes word appear there
    clock.tick(20)
    pygame.display.flip()

pygame.quit()
    
