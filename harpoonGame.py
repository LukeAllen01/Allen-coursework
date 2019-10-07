import pygame
import random
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
GREY = (170,170,170)
YELLOW = (255,224,32)   #I got these colours from a picture online 

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

class Button:
    def __init__(self, x, y, width, height, fontsize, word, fill, func):
        font = pygame.font.SysFont('Calibri', fontsize, True, False)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.word = font.render(word, True, BLACK)
        self.fill = fill
        self.outline_colour = BLACK
        self.clicked = False
        self.func = func
        global page
    def draw(self):
        pygame.draw.rect(screen, self.fill, [self.x,self.y,self.width,self.height])
        pygame.draw.rect(screen, self.outline_colour, [self.x, self.y, self.width, self.height], 4)
        screen.blit(self.word, [self.x + 10, self.y + 10])
    def click(self):
        if ((event.type == pygame.MOUSEBUTTONDOWN) and (pygame.mouse.get_pos()[0] > self.x) and (pygame.mouse.get_pos()[0] <(self.x + self.width))) and ((pygame.mouse.get_pos()[1] > self.y) and (pygame.mouse.get_pos()[1] < (self.y + self.height)) and (self.func != "") and (self.func[:4] != "FUNC")):
            page.append(self.func)
        if ((event.type == pygame.MOUSEBUTTONDOWN) and (pygame.mouse.get_pos()[0] > self.x) and (pygame.mouse.get_pos()[0] <(self.x + self.width))) and ((pygame.mouse.get_pos()[1] > self.y) and (pygame.mouse.get_pos()[1] < (self.y + self.height)) and (self.func != "") and (self.func[:4] == "FUNC")):
            global KLC
            global BLC
            if self.func == "FUNC-CC-KLC" and self.fill != BLC:
                KLC = self.fill
            elif self.func == "FUNC-CC-BLC" and self.fill != KLC:
                BLC = self.fill
class wood:
    def __init__(self, t, coords):
        global Wooden_Blocks
        self.t = t
        self.coords = coords
        Wooden_Blocks.append(pygame.transform.rotate(pygame.transform.scale(pygame.image.load("wood.jpg"), (100, 100)), random.randrange(0,360)))
    def draw(self):
        if start == True:
            Wooden_Blocks[self.t][1][1] += score
        screen.blit(Wooden_Blocks[self.t],(self.coords[0],self.coords[1]))
###############################################################             GENERAL                 ######################################################################################

page = ["ST"]

SP_Harpoon_game = Button(232,-10,0,0,35,"Harpoon Game",WHITE, "")
SP_Continuous = Button( 250, 55, 200, 90,22, "Continuous", WHITE, "CO")
SP_Levels = Button(250,155,200,90,22,"Levels",WHITE, "LV")
SP_Level_builder = Button(250,255,200,90,22, "Level Builder", WHITE,"LB")
SP_Options = Button(250,355,200,90,22, "Options", WHITE, "OP")
def StartPage():
    screen.fill(WHITE)
    #SP means start page
    SP_Harpoon_game.draw()
    SP_Continuous.draw()
    SP_Levels.draw()
    SP_Level_builder.draw()
    SP_Options.draw()
    pygame.display.flip()
    
BACK = Button(595,445,100,50,20,"BACK",WHITE,"BACK")
gravity = False
###############################################################             END OF GENERAL          ######################################################################################
###############################################################             CONTINUOUS              ######################################################################################
t = None
start = False
speed = 0
coords = [[None,None], [None,None], [None,None], [None,None]] # coords of the blocks
harpoon_gun_img = pygame.transform.scale(pygame.image.load("harpoongun.png"), (200,200))
for i in range(len(coords)):
    coords[i][0] = random.randrange(0,600)
    coords[i][1] = i*100
Wooden_Blocks = []
wood_objects = [wood(0, coords[0]),wood(1, coords[1]),wood(2, coords[2]), wood(3, coords[3])]
def update_object_coords():
    wood.coords = coords
def ContinuousPage():
    screen.fill(WHITE)
    if start == False:
        screen.blit(harpoon_gun_img, (250,500))
    update_object_coords()
    for i in wood_objects:
        i.draw()

###############################################################             END OF CONTINUOUS       ######################################################################################
###############################################################             LEVELS                  ######################################################################################
def LevelsPage():
    pass
###############################################################             END OF LEVELS           ######################################################################################
###############################################################             LEVEL BUILDER           ######################################################################################
Level_Name = Button(200,40,200,20,11,"",WHITE,"")
Level_Creator = Button(200,70,200,20,11,"",WHITE,"")
Level_Gravity = Button(200,100,100,50,11,"",WHITE,"")
def LevelBuilderStartPage():
    screen.fill(WHITE)
    screen.blit(Text_Level_Builder1, [10,10])
    screen.blit(Text_Level_Name, [10, 40])
    screen.blit(Text_Level_Creator, [10, 70])
    Level_Name.draw()
    Level_Creator.draw()
    Level_Gravity.draw()
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
Killer_Line_Colour = Button(100,100,100,100,11,"", KLC, "CCKL")
Bouncy_Line_Colour = Button(100,250,100,100,11,"", BLC, "CCBL") #unfinished
SFX_Options_button = Button(100,400,100,50,11,"",WHITE,"OPSFX")
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
    Killer_Line_Colour.draw()
    Bouncy_Line_Colour.draw()
    SFX_Options_button.draw()
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
def ChangeColour(x,y):              #(colour being changed, other colour)
    screen.fill(WHITE)
    Change_Colour_Red.outline_colour = ChangeColourBoxRim(RED)
    Change_Colour_Blue.outline_colour = ChangeColourBoxRim(BLUE)
    Change_Colour_Grey.outline_colour = ChangeColourBoxRim(GREY)
    Change_Colour_Pink.outline_colour = ChangeColourBoxRim(PINK)
    Change_Colour_Orange.outline_colour =ChangeColourBoxRim(ORANGE)
    Change_Colour_Yellow.outline_colour =ChangeColourBoxRim(YELLOW)
    if x == KLC:
        Change_Colour_Red.func = "FUNC-CC-KLC"
        Change_Colour_Blue.func = "FUNC-CC-KLC"
        Change_Colour_Grey.func = "FUNC-CC-KLC"
        Change_Colour_Pink.func = "FUNC-CC-KLC"
        Change_Colour_Orange.func = "FUNC-CC-KLC"
        Change_Colour_Yellow.func = "FUNC-CC-KLC"
    elif x == BLC:
        Change_Colour_Red.func = "FUNC-CC-BLC"
        Change_Colour_Blue.func = "FUNC-CC-BLC"
        Change_Colour_Grey.func = "FUNC-CC-BLC"
        Change_Colour_Pink.func = "FUNC-CC-BLC"
        Change_Colour_Orange.func = "FUNC-CC-BLC"
        Change_Colour_Yellow.func = "FUNC-CC-BLC"        
    Change_Colour_Red.draw()
    Change_Colour_Blue.draw()
    Change_Colour_Grey.draw()
    Change_Colour_Pink.draw()
    Change_Colour_Orange.draw()
    Change_Colour_Yellow.draw()
    BACK.draw()

######################################################################      END OF OPTIONS     ###############################################################################################

######################################################################      MAIN LOOP          ###############################################################################################
StartPage()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or exit_button == True:
            done = True
        elif page[-1] == "ST":
            StartPage()
            SP_Harpoon_game.click()
            SP_Continuous.click()
            SP_Levels.click()
            SP_Level_builder.click()
            SP_Options.click()
        elif page[-1] == "BACK":
            page.pop()
            page.pop()
        
        elif page[1] == "CO":
            ContinuousPage()
            
        elif page[1] == "LV":
            LevelsPage()
            
        elif page[1] == "LB":
            LevelBuilderStartPage()
            
        elif page[1] == "OP":
            if len(page) == 2:
                OptionsPage()
                Killer_Line_Colour.click()
                Bouncy_Line_Colour.click()
                SFX_Options_button.click()
                BACK.click()
            elif page[-1] == "CCKL":
                ChangeColour(KLC,BLC)
                Change_Colour_Red.click()
                Change_Colour_Blue.click()
                Change_Colour_Grey.click ()
                Change_Colour_Pink.click()
                Change_Colour_Orange.click()
                Change_Colour_Yellow.click()
                BACK.click()
            elif page[-1] == "CCBL":
                ChangeColour(BLC,KLC)
                Change_Colour_Red.click()
                Change_Colour_Blue.click()
                Change_Colour_Grey.click ()
                Change_Colour_Pink.click()
                Change_Colour_Orange.click()
                Change_Colour_Yellow.click()
                BACK.click()
        pygame.display.flip()
        clock.tick(20)
pygame.quit()
