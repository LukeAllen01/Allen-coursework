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
KLC = RED
BLC = BLUE

screen.fill(WHITE)
all_sprites_list = pygame.sprite.Group()

class Block (pygame.sprite.Sprite):
    def __init__(self, width = 20, height = 20, image = "wood.jpg", image_size = (100,100)):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.OG_image = pygame.transform.scale(pygame.image.load(image), image_size)
        self.center = self.OG_image.get_rect().center
        self.rect = self.OG_image.get_rect(center = self.center)
        self.image_angle = random.randrange(0,360)
        self.image = pygame.transform.rotate(self.OG_image, self.image_angle)



############### DO NOT COPY BEFORE THIS POINT
zoom = 1
selected = 0
KillerBlockKey = pygame.K_k
BouncyBlockKey = pygame.K_b
CheckpointBlockKey = pygame.K_c
FinalBlockKey = pygame.K_f

class Create(Block):
    def __init__(self, Type):
        super().__init__(self)
        self.image_angle = 0
        if Type == "killer":
            self.colour = KLC
            self.OG_image = rect(screen, KLC, 
        elif Type == "bouncy":
            self.colour = BLC
        elif Type == "checkpoint":
            self.OG_image = pygame.transform.scale(pygame.image.load("wood.jpg", (self.width, self.height)))
        elif Type == "final":
            self.OG_image = pygame.transform.scale(pygame.image.load("wood.jpg", (self.width, self.height)))
        
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == KillerBlockKey:
            killer = Create("killer")
            all_sprites_list.add(killer)
        elif event.type == pygame.KEYDOWN and event.key == BouncyBlockKey:
            bouncy = Create("bouncy")
            all_sprites_list.add(bouncy)
        elif event.type == pygame.KEYDOWN and event.key == CheckpointBlockKey:
            checkpoint = Create("checkpoint")
            all_sprites_list.add(checkpoint)
        elif event.type == pygame.KEYDOWN and event.key == FinalBlockKey:
            final = Create("final")
            all_sprites_list.add(final)

    all_sprites_list.draw(screen)
    clock.tick(20)

    
    pygame.display.flip()
pygame.quit()

