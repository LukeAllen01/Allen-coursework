import pygame
import random
import math
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

class Button():
    def __init__(self, x, y, width, height, fontsize, word, fill, func):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.word = word
        self.fill = fill
        self.outline_colour = BLACK
        self.clicked = False
        self.func = func
        self.fontsize = fontsize
        self.wait = 0
        global page
    def draw(self):
        font = pygame.font.SysFont('Calibri', self.fontsize, True, False)
        pygame.draw.rect(screen, self.fill, [self.x,self.y,self.width,self.height])
        pygame.draw.rect(screen, self.outline_colour, [self.x, self.y, self.width, self.height], 3)
        screen.blit(font.render(self.word,True,BLACK), [self.x + 10, self.y + 10])
    def click(self):
        global KLC
        global BLC
        global SFX
        global number_of_pages
        if ((event.type == pygame.MOUSEBUTTONDOWN) and (pygame.mouse.get_pos()[0] > self.x) and (pygame.mouse.get_pos()[0] <(self.x + self.width))) and ((pygame.mouse.get_pos()[1] > self.y) and (pygame.mouse.get_pos()[1] < (self.y + self.height)) and (self.func != "")):
            if self.func == "":
                pass
            elif (self.func[:3] == "ADD"): #adding a page onto stack
                page.append(self.func[4:])
                number_of_pages = number_of_pages + 1
            elif self.func == "klc" and self.fill != BLC: #changing the klc when different colour clicked
                KLC = self.fill
            elif self.func == "blc" and self.fill != KLC: #changing the blc when different colour clicked
                BLC = self.fill
            elif self.func == "sfx":
                if SFX == True:
                    SFX = False
                else:
                    SFX = True
            elif self.func == "BACK":
                page.pop()
                return True
            else:
                (self.func)()
                
class image_button(Button):
    def __init__(self,x,y,width,height,fontsize,word,fill,func,image):
        super().__init__(x,y,width,height,fontsize,word,fill,func)
        self.image = pygame.transform.scale(pygame.image.load(image), (self.width - 10,self.height - 10))
        pygame.draw.rect(screen, self.fill, [self.x,self.y,self.width,self.height])
        pygame.draw.rect(screen, self.outline_colour, [self.x, self.y, self.width, self.height], 3)
    def draw(self):
        screen.blit(self.image,(self.x + 5, self.y + 5))
    def click(self):
        press = pygame.mouse.get_pressed()
        if ((press[0] == 1) and (pygame.mouse.get_pos()[0] > self.x) and (pygame.mouse.get_pos()[0] <(self.x + self.width))) and ((pygame.mouse.get_pos()[1] > self.y) and (pygame.mouse.get_pos()[1] < (self.y + self.height)) and (self.func != "")):
            if self.func == "home":
                page.clear()
                page.append("ST")
            elif self.func == "replay":
                page.pop()
                page.append("GA")
            elif self.func == "options":
                page.append("OP")
                
SETTINGS = image_button(645, 5, 50, 50, 12, "", WHITE, "options", "settings.png")

############### DO NOT COPY BEFORE THIS POINT
QUIT = image_button(10, 5, 50, 50, 12, "", WHITE, "home", "quit.png")
SAVE = image_button(65, 5, 50, 50, 12, "", WHITE, "", "save.png")

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
        self.rect.x = 100
        self.rect.y = 100
        self.select = False
        self.dragstart = False
        self.og_x = 0
        self.og_y = 0
        self.drag_og_x = 0
        self.drag_og_y = 0
    def selecter(self):
        pos = pygame.mouse.get_pos()
        if (event.type == pygame.MOUSEBUTTONDOWN):            
            if (pos[0] > self.rect.x) and (pos[0] <(self.rect.x + self.width)) and ((pos[1] > self.rect.y) and (pos[1] < (self.rect.y + self.height))):
                for i in all_sprites_list:
                    i.select = False                
                self.select = True
        if self.select == True:
            pygame.draw.rect(screen, BLACK, [self.rect.x - 5, self.rect.y - 5, self.width + 10, self.height + 10], 2)
            #corners                     #top-right
            pygame.draw.circle(screen, WHITE, (self.rect.x + self.width + 5, self.rect.y + self.height + 5), 5)             #bottom-right

            #pygame.draw.circle(screen, BLACK, (self.rect.x - 5, self.rect.y - 5), 5, 1)                             
            #pygame.draw.circle(screen, BLACK, (self.rect.x - 5, self.rect.y + self.height + 5), 5, 1)
            #pygame.draw.circle(screen, BLACK, (self.rect.x + self.width + 5, self.rect.y - 5), 5, 1)
            pygame.draw.circle(screen, BLACK, (self.rect.x + self.width + 5, self.rect.y + self.height + 5), 5, 1)
            #sides
            #pygame.draw.circle(screen, WHITE, (int(self.rect.x - 3 + 0.5*self.width), self.rect.y - 5), 5)
            #pygame.draw.circle(screen, WHITE, (self.rect.x - 5, int(self.rect.y + 0.5*self.height - 3)), 5)
            #pygame.draw.circle(screen, WHITE, (int(self.rect.x + 0.5*self.width + 3), self.rect.y + self.height + 5), 5)
            #pygame.draw.circle(screen, WHITE, (self.rect.x + self.width + 5, int(self.rect.y + 0.5*self.height + 3)), 5)

            #pygame.draw.circle(screen, BLACK, (int(self.rect.x - 3 + 0.5*self.width), self.rect.y - 5), 5, 1)
            #pygame.draw.circle(screen, BLACK, (self.rect.x - 5, int(self.rect.y + 0.5*self.height - 3)), 5, 1)
            #pygame.draw.circle(screen, BLACK, (int(self.rect.x + 0.5*self.width + 3), self.rect.y + self.height + 5), 5, 1)
            #pygame.draw.circle(screen, BLACK, (self.rect.x + self.width + 5, int(self.rect.y + 0.5*self.height + 3)), 5, 1)

    def drag(self):
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and self.select == True and self.dragstart == False and (pos[0] > self.rect.x + 5) and (pos[0] <(self.rect.x + self.width - 5)) and ((pos[1] > self.rect.y + 5) and (pos[1] < (self.rect.y + self.height - 5))):
            self.dragstart = True
            self.drag_og_x = pos[0]
            self.drag_og_y = pos[1]
            self.og_x = self.rect.x
            self.og_y = self.rect.y
        if self.dragstart == True:
            self.rect.x = self.og_x + (pos[0] - self.drag_og_x)
            self.rect.y = self.og_y + (pos[1] - self.drag_og_y)
        if event.type == pygame.MOUSEBUTTONUP:
            self.dragstart = False
            self.bottom_right_x = self.rect.x + self.width + 5
            self.bottom_right_y = self.rect.y + self.height + 5
    def size(self):
        pos = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()
        top_left_pos = (self.rect.x - 5, self.rect.y - 5)
        top_right_pos = (self.rect.x + self.width + 5, self.rect.y - 5)
        bottom_left_pos = (self.rect.x - 5, self.rect.y + self.height + 5)
        bottom_right_pos = (self.rect.x + self.width + 5, self.rect.y + self.height + 5)
        
        if pressed[0] == 1 and self.select == True:
            print("te")
            if math.sqrt((top_left_pos[0] - pos[0])**2 + (top_left_pos[1] - pos[1])**2) < 5:
                pass
            elif math.sqrt((top_right_pos[0] - pos[0])**2 + (top_right_pos[1] - pos[1])**2) < 5:
                pass
            elif math.sqrt((bottom_right_pos[0] - pos[0])**2 + (bottom_right_pos[1] - pos[1])**2) < 5:           #bottom-right corner
                self.width = pos[0] - self.rect.x
                self.height = pos[1] - self.rect.y
            elif math.sqrt((bottom_left_pos[0] - pos[0])**2 + (bottom_left_pos[1] - pos[1])**2) < 5:
                pass
            
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
    SETTINGS.draw()
    SAVE.draw()
    QUIT.draw()
    #SAVE.click()
    #QUIT.click()
    #SETTINGS.click()
    for i in all_sprites_list:
        i.drag()
        i.size()
        i.selecter()
    all_sprites_list.draw(screen)
    if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
        print(pygame.mouse.get_pos())
        print(killer.rect)
    clock.tick(20)

    
    pygame.display.flip()
pygame.quit()

