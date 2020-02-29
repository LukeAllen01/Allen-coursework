import pygame
import random
import math
pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,32,255)
GREEN = (0,182,0)
PINK = (255,96,208)
ORANGE = (255,160,16)
GREY = (200,200,200)
YELLOW = (255,224,32)   #I got these colours from a picture online 

BACK_COLOURS = [WHITE, RED, BLUE, GREEN, PINK, ORANGE]

pygame.display.set_caption("harpoon")
pygame.font.SysFont('Calibri', 25, True, BLACK)
font1 = pygame.font.SysFont('Calibri', 30, True, False) 
font2 = pygame.font.SysFont('Calibri', 20, True, False) 

Text_Continuous1 = font1.render("CONTINUOUS", True, BLACK) 
Text_Continuous2 = font2.render("CONTINUOUS", True, BLACK) 
Text_Levels1 = font1.render("LEVELS", True, BLACK) 
Text_Levels2 = font2.render("LEVELS", True, BLACK) 
Text_Level_Builder1 = font1.render("LEVEL BUILDER", True, BLACK) 
Text_Level_Builder2 = font2.render("LEVEL BUILDER", True, BLACK) 
Text_Options1 = font1.render("OPTIONS", True, BLACK) 
Text_Options2 = font2.render("OPTIONS", True, BLACK)
Text_Harpoon_Game = font1.render("HARPOON GAME", True, BLACK) 
Text_Level_Name = font2.render("Level Name:", True, BLACK) 
Text_Level_Creator = font2.render("Level Creator:", True, BLACK)
Text_Gravity = font2.render("Gravity:", True, BLACK)
Text_SFX = font2.render("SFX",True, BLACK)

#original settings
KLC = RED    #ONLC stand for 'killer line colour'
BLC = BLUE
SFX = True

done = False
exit_button = False
ChangeColourClose = False

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
global keys
keys = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
class TextBox(Button):
    def __init__(self, x, y, width, height, fontsize, word, fill, func):
        super().__init__(x,y,width,height,fontsize,word,fill,func)
        self.selected = False
    def type(self):
        if self.wait == 0 and self.selected == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.word = self.word[:(len(self.word)-1)]
                elif event.key == pygame.K_SPACE:
                    self.word = self.word + " "
                elif event.key != pygame.K_RETURN:
                    self.word = self.word + keys[event.key - 97]
                self.wait = 3
        else:
            self.wait = self.wait - 1
    def click(self):
        if ((event.type == pygame.MOUSEBUTTONDOWN) and (pygame.mouse.get_pos()[0] > self.x) and (pygame.mouse.get_pos()[0] <(self.x + self.width))) and ((pygame.mouse.get_pos()[1] > self.y) and (pygame.mouse.get_pos()[1] < (self.y + self.height))):
            for i in TextBoxes:
                i.selected = False
            self.selected = True
    def draw(self):
        font = pygame.font.SysFont('Calibri', self.fontsize, True, False)
        thickness = 3
        if self.selected == True:
            thickness = 5
        pygame.draw.rect(screen, self.fill, [self.x,self.y,self.width,self.height])
        pygame.draw.rect(screen, self.outline_colour, [self.x, self.y, self.width, self.height], thickness)
        screen.blit(font.render(self.word,True,BLACK), [self.x + 10, self.y + 10])
            

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


###############################################################             GENERAL                 ######################################################################################

page = ["ST"]
number_of_pages = 1
wait = 0
ALL_BUTTONS = []

SP_Harpoon_game = Button(232,-10,0,0,35,"Harpoon Game",WHITE, "")
SP_Continuous = Button( 250, 55, 200, 90,22, "Continuous", WHITE, "ADD_CO")
SP_Levels = Button(250,155,200,90,22,"Levels",WHITE, "ADD_LV")
SP_Level_builder = Button(250,255,200,90,22, "Level Builder", WHITE,"ADD_LB")
SP_Options = Button(250,355,200,90,22, "Options", WHITE, "ADD_OP")
SP_Buttons = [SP_Harpoon_game,SP_Continuous,SP_Levels,SP_Level_builder,SP_Options]
def StartPage():
    screen.fill(WHITE)
    #SP means start page
    for i in SP_Buttons:
        i.draw()
    pygame.display.flip()
    
BACK = Button(595,445,100,50,20,"BACK",WHITE,"BACK")
SETTINGS = image_button(600, 50, 50, 50, 12, "", WHITE, "options", "settings.png")
gravity = False

###############################################################             END OF GENERAL          ######################################################################################
###############################################################             CONTINUOUS              ######################################################################################
PNP_button = TextBox(350,230, 250, 40, 20, "", WHITE, "")
ENTER_button = Button(300,350,100,50,22,"ENTER", GREY, "ADD_GA")
Player_name_words = font2.render("Player name:", True, BLACK)
PNP_button.selected = True
Text_To_Start = font1.render("press space to start", True, BLACK) 


TextBoxes = [PNP_button]
def PlayerNamePage():
    screen.fill(WHITE)
    screen.blit(Player_name_words, [200, 240])
    ENTER_button.draw()
    PNP_button.draw()
    BACK.draw()
    PNP_button.type()
    ENTER_button.click()

speed = 10
background_colour = [255,255,255]

def transition(x):
    if x == GREY:
        move = False
        for i in all_sprites_list:
            for t in range(100):
                i.image.set_alpha(t)
            
    if background_colour[0] > x[0]:
        background_colour[0] = background_colour[0] -1
    elif background_colour[0] < x[0]:
        background_colour[0] = background_colour[0] + 1
    if background_colour[1] > x[1]:
        background_colour[1] = background_colour[1] -1
    elif background_colour[1] < x[1]:
        background_colour[1] = background_colour[1] + 1
    if background_colour[2] > x[2]:
        background_colour[2] = background_colour[2] -1
    elif background_colour[2] < x[2]:
        background_colour[2] = background_colour[2] + 1
        

death_screen = Button(200, 50, 300, 400, 20, "", WHITE, "")
REPLAY = image_button(225, 300, 50, 50, 20, "", WHITE, "replay", "replay.png")
HOME = image_button(325, 300, 50, 50, 20, "", WHITE, "home", "home.jpg")
LEADERBOARD = image_button(425, 300, 50, 50, 20, "", WHITE, "", "list.png")
background_colour_pointer = 0

def deathscreen():
    death_screen.draw()
    SETTINGS.draw()
    SETTINGS.click()
    REPLAY.draw()
    REPLAY.click()
    HOME.draw()
    HOME.click()
    LEADERBOARD.draw()
    LEADERBOARD.click()
    screen.blit(score_word, (300,100))
    screen.blit(bestScore_word, (300, 150))

###############################################################             END OF CONTINUOUS       ######################################################################################
###############################################################             LEVELS                  ######################################################################################
Text_Puzzle = font2.render("Puzzle levels:", True, BLACK) 
Text_SpeedRun = font2.render("Speed run levels:", True, BLACK) 
level1_button = Button(30, 100, 50, 50, 20, "", WHITE, "")
level2_button = Button(325, 100, 50, 50, 20, "", WHITE, "")
level3_button = Button(620, 100, 50, 50, 20, "", WHITE, "")
level4_button = Button(30, 275, 50, 50, 20, "", WHITE, "")
level5_button = Button(325, 275, 50, 50, 20, "", WHITE, "")
level6_button = Button(620, 275, 50, 50, 20, "", WHITE, "")
Levels_buttons = (level1_button, level2_button, level3_button, level4_button, level5_button, level6_button)
def LevelsPage(): 
    screen.fill(WHITE)
    screen.blit(Text_Levels1, [300,10])
    screen.blit(Text_Puzzle, [20,75])
    screen.blit(Text_SpeedRun, [20, 250])
    BACK.draw()
    BACK.click()
    SETTINGS.draw()
    SETTINGS.click()
    for i in Levels_buttons:
        i.draw()
###############################################################             END OF LEVELS           ######################################################################################
###############################################################             LEVEL BUILDER           ######################################################################################
Create_button = Button(275, 100, 150, 100,20,"Create",WHITE,"ADD_LBSP")
Edit_button = Button(275,300, 150, 100,20,"Edit",WHITE,"")
def CreateOrEditPage():
    screen.fill(WHITE)
    Create_button.draw()
    Create_button.click()
    Edit_button.draw()
    

Level_Name = TextBox(200,40,200,20,11,"",WHITE,"")
Level_Creator = TextBox(200,70,200,20,11,"",WHITE,"")
Level_Gravity = TextBox(200,100,100,50,11,"",WHITE,"")
TextBoxes.append(Level_Name)
TextBoxes.append(Level_Creator)
TextBoxes.append(Level_Gravity)

def LevelBuilderStartPage():
    screen.fill(WHITE)
    screen.blit(Text_Level_Builder1, [10,10])
    screen.blit(Text_Level_Name, [10, 40])
    screen.blit(Text_Level_Creator, [10, 70])
    Level_Name.draw()
    Level_Creator.draw()
    Level_Gravity.draw()
    Level_Name.click()
    Level_Creator.click()
    Level_Name.type()
    Level_Creator.type()
    BACK.draw()
    if gravity == True:
        pygame.draw.rect(screen, GREEN, [200, 100, 50, 50])
        pygame.draw.rect(screen, WHITE, [250, 100, 50, 50])
        pygame.draw.rect(screen, BLACK, [200, 100, 100, 50], 4)
    else:
        pygame.draw.rect(screen, WHITE, [200, 100, 50, 50])
        pygame.draw.rect(screen, GREY, [250, 100, 50, 50])
        pygame.draw.rect(screen, BLACK, [200, 100, 100, 50], 4)
    
###############################################################             END OF LEVEL BUILDER    ######################################################################################
###############################################################             OPTIONS                 ######################################################################################
Killer_Line_Colour = Button(100,100,100,100,11,"", KLC, "ADD_OPKL")
Bouncy_Line_Colour = Button(100,250,100,100,11,"", BLC, "ADD_OPBL") #unfinished
SFX_Options_button = Button(100,400,100,50,11,"",WHITE,"sfx")
OP_Buttons = [Killer_Line_Colour, Bouncy_Line_Colour, SFX_Options_button]
def OptionsPage():
    screen.fill(WHITE)
    Killer_Line_Colour.fill = KLC
    Bouncy_Line_Colour.fill = BLC
    Text_Killer_Line_Colour = font2.render("Killer Line Colour", True, BLACK)
    Text_Bouncy_Line_Colour = font2.render("Bouncy Line Colour", True, BLACK)
    screen.blit(Text_Killer_Line_Colour, [250, 125])
    screen.blit(Text_Bouncy_Line_Colour, [250, 275])
    screen.blit(Text_Options1, [300, 60])
    screen.blit(Text_SFX, [250, 400])
    for i in OP_Buttons:
        i.draw()
    if SFX == True:
        pygame.draw.rect(screen, GREEN, [100, 400, 50, 50])
        pygame.draw.rect(screen, WHITE, [150, 400, 50, 50])
    else:
        pygame.draw.rect(screen, WHITE, [100, 400, 50, 50])
        pygame.draw.rect(screen, GREY, [150, 400, 50, 50])
    BACK.draw()

def ChangeColourBoxRim(x):
    if x == KLC:
        rim = GREEN
    elif x == BLC:
        rim = RED
    else:
        rim = BLACK
    return rim

Change_Colour_Red = Button(100,100,100,100, 11, "",RED,"")          
Change_Colour_Blue = Button(300,100,100,100, 11, "",BLUE,"")        
Change_Colour_Grey = Button(500,100,100,100, 11, "",GREY,"")        
Change_Colour_Pink = Button(100,300,100,100, 11, "",PINK,"")        
Change_Colour_Orange = Button(300,300,100,100, 11, "",ORANGE,"")    
Change_Colour_Yellow = Button(500,300,100,100, 11, "",YELLOW,"")
Colour_Buttons = [Change_Colour_Red,Change_Colour_Blue,Change_Colour_Grey,Change_Colour_Pink,Change_Colour_Orange,Change_Colour_Yellow]
def ChangeColour(x,y):              #(colour being changed, other colour)
    screen.fill(WHITE)
    for i in Colour_Buttons:
        i.outline_colour = ChangeColourBoxRim(i.fill)
    if x == KLC:
        for i in Colour_Buttons:
            i.func = "klc"
    elif x == BLC:
        for i in Colour_Buttons:
            i.func = "blc"       
    for i in Colour_Buttons:
        i.draw()
    BACK.draw()

######################################################################      END OF OPTIONS     ###############################################################################################

######################################################################      MAIN LOOP          ###############################################################################################
bestscore = 0

StartPage()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or exit_button == True:
            done = True
    if page[-1] == "ST":
        StartPage()
        for i in SP_Buttons:
            i.click()
    elif page[-1][:2] == "OP":
        if len(page[-1]) == 2:
            OptionsPage()
            for i in OP_Buttons:
                i.click()
            number_of_pages = len(page)
            BACK.click()
        elif page[-1][2:] == "KL":
            ChangeColour(KLC,BLC)
            for i in Colour_Buttons:
                i.click()
            number_of_pages = len(page)
            BACK.click()
        elif page[-1][2:] == "BL":
            ChangeColour(BLC,KLC)
            for i in Colour_Buttons:
                i.click()
            BACK.click()
            
    elif page[1] == "CO":
        if page[-1][:2] == "GA":
            if page[-1] == "GA":
                blocks = pygame.sprite.Group()                                                         #group so that goup collide can be used
                block_list = []
                trail = []
                all_sprites_list = pygame.sprite.Group()

                #creates wooden blocks
                for i in range(4):
                    block = Block("wood.jpg")
                    block.rect.x = random.randrange(0,650)
                    block.rect.y = (i*200) - 400
                    block.OG_image = pygame.transform.scale(pygame.image.load("wood.jpg"), (20, 20))
                    blocks.add(block)
                    block_list.append(block)
                    all_sprites_list.add(block)

                #creates player
                target = 3
                player = Player("harpoongun.png")
                player.rect.x = 325
                player.rect.y = 300
                player.center = (325,300)
                player.OG_image = pygame.transform.scale(pygame.image.load("harpoongun.png"), (50,50))
                all_sprites_list.add(player)

                font = pygame.font.SysFont('Calibri', 30, True, False)

                spin = False
                move = False
                spinable = True
                start = False
                death = False
                clock = pygame.time.Clock()
                score = 0
                page.pop()
                page.append("GACO")

            transition(BACK_COLOURS[background_colour_pointer])
            screen.fill(background_colour)
            if start == False:
                screen.blit(Text_To_Start, (30,400))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and spinable == True:
                player.spin()
                spin = True
                start = True
            #this detects whether a key is pressed, if that key is SPACE bar and whether player is allowed to spin
            elif (spin == True and event.type != pygame.KEYDOWN) or (move == True):
                spin = False
                move = True
                spinable = False
                player.move()
            #this detects if no key is pressed and spin = True, or it was moving last loop
            speed = score//5 + 5
            #increases speed
            
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
                    if (score/5) == (score//5):
                        background_colour_pointer = background_colour_pointer + 1
                else:
                    done = True
                # for moment this stops game if wrong block hit
            if start == True:
                for sprite in all_sprites_list:
                    sprite.rect.y += (speed-4)
                    sprite.center = (sprite.center[0], sprite.center[1] + (speed-4))
            #makes all srites move down screen by spped
            if (player.rect.x > 720 or player.rect.x < -20 or player.rect.y > 520 or player.rect.y < -20):
                death = True
                #if player hits side of screen they dead
            for i in blocks:
                if i.rect.y > 520:
                    i.rect.y = i.rect.y - 800
                    i.rect.x = random.randrange(0,650)
            all_sprites_list.draw(screen)
            #shows all sprites
            score_word = font.render("score:" + str(score), True, BLACK)
            #writes score on top right corner
            if death != True:
                screen.blit(score_word, (600, 10))
            elif death == True:
                move = False
                if score > bestscore:
                    bestscore = score
                bestScore_word = font.render("best:" + str(bestscore), True, BLACK)
                transition(GREY)
                deathscreen()
                
##################
        else:
            PlayerNamePage()
            BACK.click()
        
    elif page[1] == "LV":
        LevelsPage()
            
    elif page[1] == "LB":
        if page[-1] == "LB":
            CreateOrEditPage()
        elif page[-1] == "LBSP":
            LevelBuilderStartPage()
        else:
            pass
        BACK.click()
    pygame.display.flip()
    clock.tick(20)
pygame.quit()
