import pygame
import random
pygame.init()

size = (700 , 500)
screen = pygame.display.set_mode([size[0],size[1]])
clock = pygame.time.Clock()

WHITE = (255,255,255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0,0,0)
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
RED_IMAGE = "red.png"
BLUE_IMAGE = "blue.png"
YELLOW_IMAGE = "yellow.png"
GREY_IMAGE = "grey.png"
PINK_IMAGE = "pink.png"
ORANGE_IMAGE = "orange.png"
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
        super().__init__(image)
        self.image_angle = 0
        self.image = pygame.transform.rotate(self.OG_image, self.image_angle)
        self.rect.x = 10
        self.rect.y = 10
        self.select = False
        self.dragstart = False
        self.og_x = 0
        self.og_y = 0
        self.drag_og_x = 0
        self.drag_og_y = 0
    def selecter(self):
        if (event.type == pygame.MOUSEBUTTONDOWN):            
            for i in all_sprites_list:
                i.select = False
            if (pygame.mouse.get_pos()[0] > self.rect.x) and (pygame.mouse.get_pos()[0] <(self.rect.x + self.width)) and ((pygame.mouse.get_pos()[1] > self.rect.y) and (pygame.mouse.get_pos()[1] < (self.rect.y + self.height))):
                self.select = True
        if self.select == True:
            pygame.draw.rect(screen, BLACK, [self.rect.x - 5, self.rect.y - 5, self.width + 10, self.height + 10], 2)
            #corners
            pygame.draw.circle(screen, WHITE, (self.rect.x - 5, self.rect.y - 5), 5)                                        #top-left
            pygame.draw.circle(screen, WHITE, (self.rect.x - 5, self.rect.y + self.height + 5), 5)                          #bottom-left
            pygame.draw.circle(screen, WHITE, (self.rect.x + self.width + 5, self.rect.y - 5), 5)                           #top-right
            pygame.draw.circle(screen, WHITE, (self.rect.x + self.width + 5, self.rect.y + self.height + 5), 5)             #bottom-right

            pygame.draw.circle(screen, BLACK, (self.rect.x - 5, self.rect.y - 5), 5, 1)                             
            pygame.draw.circle(screen, BLACK, (self.rect.x - 5, self.rect.y + self.height + 5), 5, 1)
            pygame.draw.circle(screen, BLACK, (self.rect.x + self.width + 5, self.rect.y - 5), 5, 1)
            pygame.draw.circle(screen, BLACK, (self.rect.x + self.width + 5, self.rect.y + self.height + 5), 5, 1)
            #sides
            pygame.draw.circle(screen, WHITE, (int(self.rect.x - 3 + 0.5*self.width), self.rect.y - 5), 5)
            pygame.draw.circle(screen, WHITE, (self.rect.x - 5, int(self.rect.y + 0.5*self.height - 3)), 5)
            pygame.draw.circle(screen, WHITE, (int(self.rect.x + 0.5*self.width + 3), self.rect.y + self.height + 5), 5)
            pygame.draw.circle(screen, WHITE, (self.rect.x + self.width + 5, int(self.rect.y + 0.5*self.height + 3)), 5)

            pygame.draw.circle(screen, BLACK, (int(self.rect.x - 3 + 0.5*self.width), self.rect.y - 5), 5, 1)
            pygame.draw.circle(screen, BLACK, (self.rect.x - 5, int(self.rect.y + 0.5*self.height - 3)), 5, 1)
            pygame.draw.circle(screen, BLACK, (int(self.rect.x + 0.5*self.width + 3), self.rect.y + self.height + 5), 5, 1)
            pygame.draw.circle(screen, BLACK, (self.rect.x + self.width + 5, int(self.rect.y + 0.5*self.height + 3)), 5, 1)
    def drag(self):
        if event.type == pygame.MOUSEBUTTONDOWN and self.select == True and self.dragstart == False and (pygame.mouse.get_pos()[0] > self.rect.x) and (pygame.mouse.get_pos()[0] <(self.rect.x + self.width)) and ((pygame.mouse.get_pos()[1] > self.rect.y) and (pygame.mouse.get_pos()[1] < (self.rect.y + self.height))):
            self.dragstart = True
            self.drag_og_x = pygame.mouse.get_pos()[0]
            self.drag_og_y = pygame.mouse.get_pos()[1]
            self.og_x = self.rect.x
            self.og_y = self.rect.y
        if self.dragstart == True:
            self.rect.x = self.og_x + (pygame.mouse.get_pos()[0] - self.drag_og_x)
            self.rect.y = self.og_y + (pygame.mouse.get_pos()[1] - self.drag_og_y)
        if event.type == pygame.MOUSEBUTTONUP:
            self.dragstart == False
            
        
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
    screen.fill(WHITE)        
    for i in all_sprites_list:
        i.selecter()
        i.drag()
    all_sprites_list.draw(screen)
    clock.tick(20)

    
    pygame.display.flip()
pygame.quit()

