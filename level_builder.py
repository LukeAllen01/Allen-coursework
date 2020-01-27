import pygame
import random
pygame.init()

size = (700 , 500)
screen = pygame.display.set_mode([size[0],size[1]])
clock = pygame.time.Clock()

WHITE = (255,255,255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
done = False
klc = RED
blc = BLUE



screen.fill(WHITE)
all_sprites_list = pygame.sprite.Group()

class Block (pygame.sprite.Sprite):
    def __init__(self, image, width = 50, height = 50):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.OG_image = pygame.transform.scale(pygame.image.load(image), (self.width,self.height))
        self.center = self.OG_image.get_rect().center
        self.rect = self.OG_image.get_rect(center = self.center)
        self.image_angle = random.randrange(0,360)
        self.image = pygame.transform.rotate(self.OG_image, self.image_angle)



############### DO NOT COPY BEFORE THIS POINT
RED_IMAGE = pygame.transform.scale(pygame.image.load("red.png"), (50,50))
BLUE_IMAGE = pygame.transform.scale(pygame.image.load("blue.png"), (50,50))
YELLOW_IMAGE = pygame.transform.scale(pygame.image.load("yellow.png"), (50,50))
GREY_IMAGE = pygame.transform.scale(pygame.image.load("grey.png"), (50,50))
PINK_IMAGE = pygame.transform.scale(pygame.image.load("pink.png"), (50,50))
ORANGE_IMAGE = pygame.transform.scale(pygame.image.load("orange.png"), (50,50))
klc_image = RED_IMAGE
blc_image = BLUE_IMAGE

zoom = 1
selected = 0
KillerBlockKey = pygame.K_k
BouncyBlockKey = pygame.K_b
CheckpointBlockKey = pygame.K_c
FinalBlockKey = pygame.K_f

class Create(Block):
    def __init__(self, image):
        super().__init__(self, image)
        self.image_angle = 0
        self.OG_image = image
        
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == KillerBlockKey:
            killer = Create(klc_image)
            all_sprites_list.add(killer)
        elif event.type == pygame.KEYDOWN and event.key == BouncyBlockKey:
            bouncy = Create(blc_image)
            all_sprites_list.add(bouncy)
        elif event.type == pygame.KEYDOWN and event.key == CheckpointBlockKey:
            checkpoint = Create("wood.jpg")
            all_sprites_list.add(checkpoint)
        elif event.type == pygame.KEYDOWN and event.key == FinalBlockKey:
            final = Create("wood.jpg")
            all_sprites_list.add(final)

    all_sprites_list.draw(screen)
    clock.tick(20)

    
    pygame.display.flip()
pygame.quit()

