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
all_killer_blocks_list = pygame.sprite.Group()
all_bouncy_blocks_list = pygame.sprite.Group()
all_checkpoint_blocks_list = pygame.sprite.Group()
all_final_blocks_list = pygame.sprite.Group()

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
        self.clickedon = False
    def draw(self):
        screen.blit(self.image,(self.x + 5, self.y + 5))
    def click(self):
        press = pygame.mouse.get_pressed()
        R = ""
        if ((press[0] == 1) and (pygame.mouse.get_pos()[0] > self.x) and (pygame.mouse.get_pos()[0] <(self.x + self.width))) and ((pygame.mouse.get_pos()[1] > self.y) and (pygame.mouse.get_pos()[1] < (self.y + self.height)) and (self.func != "")):
            if self.func == "home":
                page.clear()
                page.append("ST")
            elif self.func == "replay":
                page.pop()
                page.append("GA")
            elif self.func == "options":
                page.append("OP")
            elif self.func == "save":
                if self.clickedon == False:
                    self.clickedon = True
                    for i in all_sprites_list:
                        i.selected = False
                    R = R + "[/"
                    R = R + "*" + str(edit_player.image_angle)+"*"+str(edit_player.image)+"*"+str(edit_player.image_file)+"*"+str(edit_player.rect.x)+"*"+str(edit_player.rect.y)+"*"+str(edit_player.select)+"*"+str(edit_player.dragstart)+"*"+str(edit_player.og_x)+"*"+str(edit_player.og_y)+"*"+str(edit_player.drag_og_x)+"*"+str(edit_player.drag_og_y)+"*"+str(edit_player.bottom_right)+"*"+str(edit_player.bar_position)+"*"+str(edit_player.bar_drag)+"*"+str(edit_player.center)
                    R = R + "/][/"
                    for i in all_killer_blocks_list:
                        R = R + "*" + str(i.image_angle)+"*"+str(i.image)+"*"+str(i.image_file)+"*"+str(i.rect.x)+"*"+str(i.rect.y)+"*"+str(i.select)+"*"+str(i.dragstart)+"*"+str(i.og_x)+"*"+str(i.og_y)+"*"+str(i.drag_og_x)+"*"+str(i.drag_og_y)+"*"+str(i.bottom_right)+"*"+str(i.bar_position)+"*"+str(i.bar_drag)+"*"+str(i.center)
                        R = R + "/"
                    R = R + "][/"
                    for i in all_bouncy_blocks_list:
                        R = R + "*" + str(i.image_angle)+"*"+str(i.image)+"*"+str(i.image_file)+"*"+str(i.rect.x)+"*"+str(i.rect.y)+"*"+str(i.select)+"*"+str(i.dragstart)+"*"+str(i.og_x)+"*"+str(i.og_y)+"*"+str(i.drag_og_x)+"*"+str(i.drag_og_y)+"*"+str(i.bottom_right)+"*"+str(i.bar_position)+"*"+str(i.bar_drag)+"*"+str(i.center)
                        R = R + "/"
                    R = R + "][/"
                    for i in all_checkpoint_blocks_list:
                        R = R + "*" + str(i.image_angle)+"*"+str(i.image)+"*"+str(i.image_file)+"*"+str(i.rect.x)+"*"+str(i.rect.y)+"*"+str(i.select)+"*"+str(i.dragstart)+"*"+str(i.og_x)+"*"+str(i.og_y)+"*"+str(i.drag_og_x)+"*"+str(i.drag_og_y)+"*"+str(i.bottom_right)+"*"+str(i.bar_position)+"*"+str(i.bar_drag)+"*"+str(i.center)
                        R = R + "/"
                    R = R + "][/"
                    for i in all_final_blocks_list:
                        R = R + "*" + str(i.image_angle)+"*"+str(i.image)+"*"+str(i.image_file)+"*"+str(i.rect.x)+"*"+str(i.rect.y)+"*"+str(i.select)+"*"+str(i.dragstart)+"*"+str(i.og_x)+"*"+str(i.og_y)+"*"+str(i.drag_og_x)+"*"+str(i.drag_og_y)+"*"+str(i.bottom_right)+"*"+str(i.bar_position)+"*"+str(i.bar_drag)+"*"+str(i.center)
                        R = R + "/"
                    R = R + "]"
                    f = open("C:\\test\level.txt", "a+")
                    f.write(R)
                    print("hello")
                    f.close()
        elif press[0] == 0:
            self.clickedon = False
                
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



############### DO NOT COPY BEFORE THIS POINT############################################################################################
#player = Player("harpoongun.png")
#player.rect.x = 300
#player.rect.y = 300
#all_sprites_list.add(player)
#player.center = [325,325]
#player.image_angle = 0
#player.image = pygame.transform.rotate(player.OG_image, player.image_angle)
#player.rect = player.image.get_rect(center = player.center)

def BOOL(value):
    if value == "False":
        bool(value)
        value = False
    elif value == "True":
        bool(value)
    return value
        
def splitus(txt):
    first_split_txt = []
    second_split_txt = []
    piece = []
    aster = []
    dash = []
    for i in range(0, len(txt)):   #marks the "/"
        if txt[i] == "/":
            dash.append(i)

    for i in range(0,len(dash)-1):
        first_split_txt.append(txt[dash[i] + 1: dash[i+1]])

    for a in range(0, len(first_split_txt)):
        for b in range (0, len(first_split_txt[a])):
            if first_split_txt[a][b] == "*":
                aster.append(b)
        for c in range(0,len(aster)-1):
            piece.append(first_split_txt[a][aster[c]+1:aster[c+1]])
        second_split_txt.append(piece)
        piece = []
        aster = []
    return second_split_txt
        
def load():
    global all_sprites_list
    global all_killer_blocks_list
    global all_bouncy_blocks_list
    global all_checkpoint_blocks_list
    global all_final_blocks_list
    all_sprites_list.empty()
    all_killer_blocks_list.empty()
    all_bouncy_blocks_list.empty()
    all_checkpoint_blocks_list.empty()
    all_final_blocks_list.empty()
    asterix_pos = []
    slashes_pos = []
    end_brackets = []
    start_brackets = []
    marker = 0
    f = open("C:\\test\level.txt", "r")
    A = f.read()                                # A means all text
    counter = 0
    for i in range(0,len(A)):
        if A[i] == "[" and counter == 0:
            start_brackets.append(i)
            counter = counter + 1
        elif A[i] == "[" and counter != 0:
            counter = counter + 1
        elif A[i] == "]" and counter == 1:
            end_brackets.append(i)
            counter = counter - 1
        elif A[i] == "]" and counter != 1:
            counter = counter - 1

    P = A[start_brackets[0] + 1 : end_brackets[0]] #text to do with each section,   # P means player
    K = A[start_brackets[1] + 1 : end_brackets[1]]                                  # K means killer blocks
    B = A[start_brackets[2] + 1 : end_brackets[2]]                                  # B means bouncy blocks
    C = A[start_brackets[3] + 1 : end_brackets[3]]                                 # C means checkpoint blocks
    F = A[start_brackets[4] + 1 : end_brackets[4]]                                 # F means final blocks        [0]
    
    P = splitus(P)
    K = splitus(K)
    B = splitus(B)
    C = splitus(C)
    F = splitus(F)

    #initialising the player
    edit_player = Create("harpoongun.png")
    edit_player.image_angle = int(float(P[0][0]))     #before first
    edit_player.image = pygame.transform.rotate(edit_player.OG_image, edit_player.image_angle) # first and second
    edit_player.image_file = "harpoongun.png"
    edit_player.rect.x = int(P[0][3])
    edit_player.rect.y = int(P[0][4])
    edit_player.select = BOOL(P[0][5])
    edit_player.dragstart = BOOL(P[0][6])
    edit_player.og_x =  int(P[0][7])
    edit_player.og_y =  int(P[0][8])
    edit_player.drag_og_x = int( P[0][9])
    edit_player.drag_og_y =  int(P[0][10])
    edit_player.bottom_right = BOOL(P[0][11])
    edit_player.bar_position = [170,430]  
    edit_player.bar_drag = BOOL(P[0][13])
    edit_player.center = [0.5*edit_player.width + edit_player.rect.x,0.5*edit_player.height + edit_player.rect.y]
    all_sprites_list.add(edit_player)
    
    for i in range(0, len(K)):
        Killer_block = Create(klc_image)
        Killer_block.image_angle = int(float(K[i][0]))     #before first
        Killer_block.image = pygame.transform.rotate(Killer_block.OG_image, Killer_block.image_angle) # first and second
        Killer_block.image_file = klc_image
        Killer_block.rect.x = int(K[i][3])
        Killer_block.rect.y = int(K[i][4])
        Killer_block.select = BOOL(K[i][5])
        Killer_block.dragstart = BOOL(K[i][6])
        Killer_block.og_x =  int(K[i][7])
        Killer_block.og_y =  int(K[i][8])
        Killer_block.drag_og_x = int( K[i][9])
        Killer_block.drag_og_y =  int(K[i][10])
        Killer_block.bottom_right = BOOL(K[i][11])
        Killer_block.bar_position = [170,430]  
        Killer_block.bar_drag = BOOL(K[i][13])
        Killer_block.center = [0.5*Killer_block.width + Killer_block.rect.x,0.5*Killer_block.height + Killer_block.rect.y]
        all_sprites_list.add(Killer_block)
        all_killer_blocks_list.add(Killer_block)

    for i in range(0, len(B)):
        Bouncy_block = Create(klc_image)
        Bouncy_block.image_angle = int(float(B[i][0]))     #before first
        Bouncy_block.image = pygame.transform.rotate(Bouncy_block.OG_image, Bouncy_block.image_angle) # first and second
        Bouncy_block.image_file = blc_image
        Bouncy_block.rect.x = int(B[i][3])
        Bouncy_block.rect.y = int(B[i][4])
        Bouncy_block.select = BOOL(B[i][5])
        Bouncy_block.dragstart = BOOL(B[i][6])
        Bouncy_block.og_x =  int(B[i][7])
        Bouncy_block.og_y =  int(B[i][8])
        Bouncy_block.drag_og_x = int( B[i][9])
        Bouncy_block.drag_og_y =  int(B[i][10])
        Bouncy_block.bottom_right = BOOL(B[i][11])
        Bouncy_block.bar_position = [170,430]  
        Bouncy_block.bar_drag = BOOL(B[i][13])
        Bouncy_block.center = [0.5*Bouncy_block.width + Bouncy_block.rect.x,0.5*Bouncy_block.height + Bouncy_block.rect.y]
        all_sprites_list.add(Bouncy_block)
        all_bouncy_blocks_list.add(Bouncy_block)

    for i in range(0, len(C)):
        Checkpoint_block = Create(klc_image)
        Checkpoint_block.image_angle = int(float(C[i][0]))     #before first
        Checkpoint_block.image = pygame.transform.rotate(Checkpoint_block.OG_image, Checkpoint_block.image_angle) # first and second
        Checkpoint_block.image_file = "wood.jpg"
        Checkpoint_block.rect.x = int(C[i][3])
        Checkpoint_block.rect.y = int(C[i][4])
        Checkpoint_block.select = BOOL(C[i][5])
        Checkpoint_block.dragstart = BOOL(C[i][6])
        Checkpoint_block.og_x =  int(C[i][7])
        Checkpoint_block.og_y =  int(C[i][8])
        Checkpoint_block.drag_og_x = int( C[i][9])
        Checkpoint_block.drag_og_y =  int(C[i][10])
        Checkpoint_block.bottom_right = BOOL(C[i][11])
        Checkpoint_block.bar_position = [170,430]  
        Checkpoint_block.bar_drag = BOOL(C[i][13])
        Checkpoint_block.center = [0.5*Checkpoint_block.width + Checkpoint_block.rect.x,0.5*Checkpoint_block.height + Checkpoint_block.rect.y]
        all_sprites_list.add(Checkpoint_block)
        all_checkpoint_blocks_list.add(Checkpoint_block)

    for i in range(0, len(F)):
        Final_block = Create(klc_image)
        Final_block.image_angle = int(float(F[i][0]))     #before first
        Final_block.image = pygame.transform.rotate(Final_block.OG_image, Final_block.image_angle) # first and second
        Final_block.image_file = "wood.jpg"
        Final_block.rect.x = int(F[i][3])
        Final_block.rect.y = int(F[i][4])
        Final_block.select = BOOL(F[i][5])
        Final_block.dragstart = BOOL(F[i][6])
        Final_block.og_x =  int(F[i][7])
        Final_block.og_y =  int(F[i][8])
        Final_block.drag_og_x = int(F[i][9])
        Final_block.drag_og_y =  int(F[i][10])
        Final_block.bottom_right = BOOL(F[i][11])
        Final_block.bar_position = [170,430]  
        Final_block.bar_drag = BOOL(F[i][13])
        Final_block.center = [0.5*Final_block.width + Final_block.rect.x,0.5*Final_block.height + Final_block.rect.y]
        all_sprites_list.add(Final_block)
        all_final_blocks_list.add(Final_block)

mode = "build"

QUIT = image_button(10, 5, 50, 50, 12, "", WHITE, "home", "quit.png")
#this is the button on which takes player back to home page
SAVE = image_button(65, 5, 50, 50, 12, "", WHITE, "save", "save.png")
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
        self.rect.x = 100      #start x position
        self.rect.y = 100      #start y position
        self.select = False    #this attribute is to help know if the object has been selected.
        self.dragstart = False  #this attribute is to help know if the object is being dragged.
        self.og_x = 0  #position of top left x coord of object when object is starting to get dragged
        self.og_y = 0  #position of top left y coord of object when object is starting to get dragged
        self.drag_og_x = 0  #position of mouse x coord of object when object is starting to get dragged
        self.drag_og_y = 0  #position of mouse y coord of object when object is starting to get dragged
        self.bottom_right = False  #tells us whether the oject is being enlarged
        self.bar_position = [170,430]  #it is the position of the rotation bar to mark what angle the image is turned at
        self.bar_drag = False  #tells us whether the rotation bar is being dragged
        self.center = [0.5*self.width + self.rect.x,0.5*self.height + self.rect.y]
    def update_image(self):
        global zoom
        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(self.image_file), (int(self.width*zoom) ,int(self.height*zoom))),self.image_angle)
        self.rect = self.image.get_rect(center = self.center)
        #updates the image so that it is the dimenstions that it should be due to the image changing 
    def selecter(self):
        pos = pygame.mouse.get_pos()
        if (event.type == pygame.MOUSEBUTTONDOWN):
            if (pos[0] > self.rect.x - 10) and (pos[0] <(self.rect.x + self.width + 10)) and ((pos[1] > self.rect.y - 10) and (pos[1] < (self.rect.y + self.height + 10))): #if this object is clicked on
                for i in all_sprites_list: #deselects all objects
                    i.select = False                
                self.select = True #selects this singular object
            elif pos[1] > 440: # within the bar rotation area
                pass
            else:
                self.select = False #as mouse has clicked elswhere, deselects object
        if self.select == True:
            pygame.draw.rect(screen, BLACK, [self.rect.x - 5, self.rect.y - 5, self.width + 10, self.height + 10], 2)   #draws box around it
            pygame.draw.circle(screen, WHITE, (self.rect.x + self.width + 5, self.rect.y + self.height + 5), 5)       #      
            pygame.draw.circle(screen, BLACK, (self.rect.x + self.width + 5, self.rect.y + self.height + 5), 5, 1)    # draws a a hollow black circle on bottom right of box for object to be enlarged.

    def rotate(self):
        pos = pygame.mouse.get_pos()
        #self.rect = self.image.get_rect(center = self.center)
        if (event.type == pygame.MOUSEBUTTONDOWN) and self.select == True and pos[0] > self.bar_position[0] and pos[0] < (self.bar_position[0] + 15) and pos[1] > self.bar_position[1] and pos[1] <( self.bar_position[1] + 45) or self.bar_drag ==True:
            #if object selected and its rotation bar is clicked on or if previoulsy known to being dragged
            self.bar_position[0] = pos[0]   #the rotation bar's x coords = the mouse's
            if self.bar_position [0] > 670:  #the drag button's x is max of 670
                self.bar_position[0] = 670
            elif self.bar_position[0] < 170: #the drag button's x is min of 170 
                self.bar_position[0] = 170
            self.bar_drag = True  #now know to be being dragged
        if event.type == pygame.MOUSEBUTTONUP:
            self.bar_drag = False    #stops dragging the button if mouse left click is released
        if self.select == True:
            #rotation_bar
            pygame.draw.rect(screen, GREY, (-5,400,710,110))
            pygame.draw.rect(screen, WHITE, (180,440,500, 20))
            pygame.draw.rect(screen, BLACK, (180,440,500, 20), 3)   #drawing the rotation bar

            pygame.draw.rect(screen,WHITE, (self.bar_position[0],self.bar_position[1], 15, 45))
            pygame.draw.rect(screen,BLACK, (self.bar_position[0],self.bar_position[1], 15, 45), 3)  #drawing the drag button on the rotation bar
        
            self.image_angle = ((self.bar_position[0] - 170)/500)*360  #changing the angle of the image as the drag button is dragged
    def drag(self):
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and self.select == True and self.dragstart == False and (pos[0] > self.rect.x + 5) and (pos[0] <(self.rect.x + self.width - 5)) and ((pos[1] > self.rect.y + 5) and (pos[1] < (self.rect.y + self.height - 5))):
        #this checks if object is selected, clicked on and not started dragging yet
            self.dragstart = True   #tells us it has started dragging
            self.drag_og_x = pos[0]   #position of mouse x coord of object when object is starting to get dragged
            self.drag_og_y = pos[1]   #position of mouse y coord of object when object is starting to get dragged
            self.og_x = self.rect.x   #position of top left x coord of object when object is starting to get dragged
            self.og_y = self.rect.y   #position of top left y coord of object when object is starting to get dragged
        if self.dragstart == True:    #checks if the object has started to be dragged
            self.rect.x = self.og_x + (pos[0] - self.drag_og_x) #changes the position of object to that of original x coord + change in x mouse position
            self.rect.y = self.og_y + (pos[1] - self.drag_og_y) #changes the position of object to that of original y coord + change in y mouse position
        if event.type == pygame.MOUSEBUTTONUP: #if mouse leftclick is released
            self.dragstart = False      #drag is stopped
            
    def size(self):
        pos = pygame.mouse.get_pos()   #this is just so that I do not have to say pygame.mouse.get_pos() every time it is used
        pressed = pygame.mouse.get_pressed()    #this is just so that I do not have to say pygame.mouse.get_pressed() every time it is used
        bottom_right_pos = (self.rect.x + self.width + 5, self.rect.y + self.height + 5) #position of the bottom right corner (of selected circle)
        
        if pressed[0] == 1 and self.select == True and self.image_file != "harpoongun.png":
            if math.sqrt((bottom_right_pos[0] - pos[0])**2 + (bottom_right_pos[1] - pos[1])**2) < 5 or self.bottom_right == True: #this checks the circular area within the small circular using the equation of the circle
                self.width = pos[0] - self.rect.x  #changes width to the new width##changes size of width to new size by minusing of the top right corner x coords from the mouse x coords because the mouse x coords where roughly origonally the bottom_right x coords
                self.height = pos[1] - self.rect.y  #changes the height to the new height
                self.bottom_right = True #tells us that the bottom right corner is being held down to increase size of object
        else:
            self.bottom_right = False  #tells us that the bottom right corner is not being held down to increase size of object
        self.center = [0.5*self.width + self.rect.x,0.5*self.height + self.rect.y]
    def shrink(self):
        global zoom
        zoom = zoom - 0.01
        self.rect.x = self.rect.x*zoom
        self.rect.y = self.rect.x*zoom
        self.center[0] = self.center[0]*zoom
        self.center[1] = self.center[1]*zoom        
    def grow(self):
        global zoom
        zoom = zoom + 0.01
        self.rect.x = self.rect.x*zoom
        self.rect.y = self.rect.x*zoom
        self.center[0] = self.center[0]*zoom
        self.center[1] = self.center[1]*zoom
        
##        
#edit_player = Create("harpoongun.png")
#all_sprites_list.add(edit_player)



load()


def screen_drag():
    global screen_drag_start  #this allows screen_drag_start to be used inside and out of the function##this is good because then it can be set to a singular value beforehand and not changed everytime the funciton is called
    global screen_drag_start_x  #this allows screen_drag_start_x to be used inside and out of the function
    global screen_drag_start_y  #this allows screen_drag_start_y to be used inside and out of the function
    x = 0
    for i in all_sprites_list:
        if i.select == True:
            x = x + 1   #x is number of selected blocks
    pos = pygame.mouse.get_pos()
    if x == 0 and event.type == pygame.MOUSEBUTTONDOWN :   #checks that no items are selected and the mouse left-click has been pressed down
        screen_drag_start = True      #tells us the screen(i.e. all the objects) are starting to be dragged
        screen_drag_start_x = pos[0]  #tells us the start x for when the screen is begging to be dragged
        screen_drag_start_y = pos[1]  #tells us the start x for when the screen is begging to be dragged
        for i in all_sprites_list:
            i.og_x = i.rect.x     #procreates drag function but for every individual block
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
        if event.type == pygame.KEYDOWN and event.key == KillerBlockKey: #when the key that is assigned to making a killer line is pressed, originally k is pressed
            killer = Create(klc_image)  #a object called killer is created, with image of kl
            all_killer_blocks_list.add(killer) 
            all_sprites_list.add(killer)   #killer is added to all_blocks_list and all_sprites_list
        elif event.type == pygame.KEYDOWN and event.key == BouncyBlockKey:  #when the key that is assigned to making a killer line is pressed, originally k is pressed
            bouncy = Create(blc_image)   #a object called bouncy is created, with image of bl
            all_bouncy_blocks_list.add(bouncy)
            all_sprites_list.add(bouncy)   #bouncy is added to all_blocks_list and all_sprites_list
        elif event.type == pygame.KEYDOWN and event.key == CheckpointBlockKey:  #when the key that is assigned to making a killer line is pressed, originally k is pressed
            checkpoint = Create("wood.jpg")  #a object called checkpoint is created, with image of wooden block
            all_checkpoint_blocks_list.add(checkpoint)
            all_sprites_list.add(checkpoint)   #checkpoint is added to all_blocks_list and all_sprites_list
        elif event.type == pygame.KEYDOWN and event.key == FinalBlockKey:  #when the key that is assigned to making a killer line is pressed, originally k is pressed
            final = Create("wood.jpg")   #a object called final is created, with image of a final wooden block
            all_final_blocks_list.add(final)
            all_sprites_list.add(final)   #final is added to all_blocks_list and all_sprites_list
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            for i in all_sprites_list:
                i.grow()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            for i in all_sprites_list:
                i.shrink()
    screen.fill(WHITE)
    SETTINGS.draw()
    SAVE.draw()
    QUIT.draw()   #buttons are drawn
    SAVE.click()
    QUIT.click()
    SETTINGS.click()
    for i in all_sprites_list:
        i.drag()
        i.size()
        i.rotate()
        i.update_image()
        i.selecter()          #all objects are checked to be draged, re-sized, rotated, or selected, and image updates
    screen_drag()
    all_sprites_list.draw(screen)   #all blocks and buttons added to screen
    clock.tick(20)
    pygame.display.flip()
pygame.quit()

