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
GREY = (200,200,200)
BLACK = (0,0,0)
done = False
klc = RED
blc = BLUE


screen.fill(WHITE)
all_sprites_list = pygame.sprite.Group()
all_blocks_list = pygame.sprite.Group()

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


player = Player("harpoongun.png")
player.rect.x = 300
player.rect.y = 300
all_sprites_list.add(player)
############### DO NOT COPY BEFORE THIS POINT############################################################################################
QUIT = image_button(10, 5, 50, 50, 12, "", WHITE, "home", "quit.png")
#this is the button on which takes player back to home page
SAVE = image_button(65, 5, 50, 50, 12, "", WHITE, "", "save.png")
#this button saves the image and if 

RED_IMAGE = "red.png"          
BLUE_IMAGE = "blue.png"
YELLOW_IMAGE = "yellow.png"
GREY_IMAGE = "grey.png"
PINK_IMAGE = "pink.png"
ORANGE_IMAGE = "orange.png"
#these images are images of blocks with the colour in
klc_image = RED_IMAGE          
blc_image = BLUE_IMAGE
#thes are the original set colours of the klc and blc

screen_drag_start = False
#used to check if the screen is being dragged
screen_drag_start_x = 0
screen_drag_start_y = 0
#position of mouse whe the screen is started to be dragged
zoom = 1
#zoom factor, used for zooming 
KillerBlockKey = pygame.K_k
BouncyBlockKey = pygame.K_b
CheckpointBlockKey = pygame.K_c
FinalBlockKey = pygame.K_f
#original key bindings for creating the blocks

def rotation_bar():
    global bar_position
    pygame.draw.rect(screen, GREY, (-5,400,710,110))
    pygame.draw.rect(screen, WHITE, (180,440,500, 20))
    pygame.draw.rect(screen, BLACK, (180,440,500, 20), 3)

    pygame.draw.rect(screen,WHITE, (bar_position, 5, 15))
    pygame.draw.rect(screen,BLACK, (bar_position, 5, 15), 3)

class Create(Block):
    def __init__(self, image):
        super().__init__(image)
        self.image_angle = 0
        self.image = pygame.transform.rotate(self.OG_image, self.image_angle)
        self.image_file = image
        self.rect.x = 100
        self.rect.y = 100
        self.select = False    #this attribute is to help know if the object has been selected.
        self.dragstart = False  #this attribute is to help know if the object is being dragged.
        self.og_x = 0  #position of top left x coord of object at start when about to be dragged
        self.og_y = 0
        self.drag_og_x = 0
        self.drag_og_y = 0
        self.bottom_right = False
        self.bar_position = [170,430]
        self.bar_drag = False
    def update_image(self):
        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(self.image_file), (self.width,self.height)),self.image_angle)
    def selecter(self):
        pos = pygame.mouse.get_pos()
        if (event.type == pygame.MOUSEBUTTONDOWN):
            if (pos[0] > self.rect.x - 10) and (pos[0] <(self.rect.x + self.width + 10)) and ((pos[1] > self.rect.y - 10) and (pos[1] < (self.rect.y + self.height + 10))):
                for i in all_sprites_list:
                    i.select = False                
                self.select = True
            elif pos[1] > 440:
                pass
            else:
                self.select = False
        if self.select == True:
            pygame.draw.rect(screen, BLACK, [self.rect.x - 5, self.rect.y - 5, self.width + 10, self.height + 10], 2)
            pygame.draw.circle(screen, WHITE, (self.rect.x + self.width + 5, self.rect.y + self.height + 5), 5)             
            pygame.draw.circle(screen, BLACK, (self.rect.x + self.width + 5, self.rect.y + self.height + 5), 5, 1)

    def rotate(self):
        pos = pygame.mouse.get_pos()
        if (event.type == pygame.MOUSEBUTTONDOWN) and pos[0] > self.bar_position[0] and pos[0] < (self.bar_position[0] + 15) and pos[1] > self.bar_position[1] and pos[1] <( self.bar_position[1] + 45) or self.bar_drag ==True:
            self.bar_position[0] = pos[0]
            if self.bar_position [0] > 670:
                self.bar_position[0] = 670
            elif self.bar_position[0] < 170:
                self.bar_position[0] = 170
            self.bar_drag = True
        if event.type == pygame.MOUSEBUTTONUP:
            self.bar_drag = False
        if self.select == True:
            #rotation_bar
            pygame.draw.rect(screen, GREY, (-5,400,710,110))
            pygame.draw.rect(screen, WHITE, (180,440,500, 20))
            pygame.draw.rect(screen, BLACK, (180,440,500, 20), 3)

            pygame.draw.rect(screen,WHITE, (self.bar_position[0],self.bar_position[1], 15, 45))
            pygame.draw.rect(screen,BLACK, (self.bar_position[0],self.bar_position[1], 15, 45), 3)
        
        self.image_angle = ((self.bar_position[0] - 170)/500)*360    
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
            #if math.sqrt((top_left_pos[0] - pos[0])**2 + (top_left_pos[1] - pos[1])**2) < 5:
            #    pass
            #elif math.sqrt((top_right_pos[0] - pos[0])**2 + (top_right_pos[1] - pos[1])**2) < 5:
            #    pass
            if math.sqrt((bottom_right_pos[0] - pos[0])**2 + (bottom_right_pos[1] - pos[1])**2) < 5 or self.bottom_right == True:           #bottom-right corner
                self.width = pos[0] - self.rect.x
                self.height = pos[1] - self.rect.y
                self.bottom_right = True
            #elif math.sqrt((bottom_left_pos[0] - pos[0])**2 + (bottom_left_pos[1] - pos[1])**2) < 5:
            #    pass
        else:
            self.bottom_right = False
def screen_drag():
    global screen_drag_start
    global screen_drag_start_x
    global screen_drag_start_y
    x = 0
    for i in all_blocks_list:
        if i.select == True:
            x = x + 1
    pos = pygame.mouse.get_pos()
    if x == 0 and event.type == pygame.MOUSEBUTTONDOWN :
        screen_drag_start = True
        screen_drag_start_x = pos[0]
        screen_drag_start_y = pos[1]
        for i in all_sprites_list:
            i.og_x = i.rect.x
            i.og_y = i.rect.y
    elif event.type == pygame.MOUSEBUTTONUP and screen_drag_start == True:
        screen_drag_start = False
    if screen_drag_start == True:
        for i in all_sprites_list:
            i.rect.x = i.og_x + (pos[0] - screen_drag_start_x)
            i.rect.y = i.og_y + (pos[1] - screen_drag_start_y)

            
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              done = True
        if event.type == pygame.KEYDOWN and event.key == KillerBlockKey:
            killer = Create(klc_image)
            all_blocks_list.add(killer)
            all_sprites_list.add(killer)
        elif event.type == pygame.KEYDOWN and event.key == BouncyBlockKey:
            bouncy = Create(blc_image)
            all_blocks_list.add(bouncy)
            all_sprites_list.add(bouncy)
        elif event.type == pygame.KEYDOWN and event.key == CheckpointBlockKey:
            checkpoint = Create("wood.jpg")
            all_blocks_list.add(checkpoint)
            all_sprites_list.add(checkpoint)
        elif event.type == pygame.KEYDOWN and event.key == FinalBlockKey:
            final = Create("wood.jpg")
            all_blocks_list.add(final)
            all_sprites_list.add(final)
    screen.fill(WHITE)
    SETTINGS.draw()
    SAVE.draw()
    QUIT.draw()
    #SAVE.click()
    #QUIT.click()
    #SETTINGS.click()
    for i in all_blocks_list:
        i.drag()
        i.size()
        i.rotate()
        i.update_image()
        i.selecter()
    screen_drag()
    all_sprites_list.draw(screen)
    if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
        print(pygame.mouse.get_pos())
        print(killer.rect)
    clicks = 0
    clock.tick(20)
    pygame.display.flip()
pygame.quit()

