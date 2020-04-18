import pygame
import random
import math
pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

#I got these colours from a picture online
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,32,255)
GREEN = (0,182,0)
PINK = (255,96,208)
ORANGE = (255,160,16)
GREY = (200,200,200)
YELLOW = (255,224,32)  

#this array is for when the background colour changes
BACK_COLOURS = [WHITE, RED, BLUE, GREEN, PINK, ORANGE]

#makes the tab name harpoon
pygame.display.set_caption("harpoon")
#fonts I will use for the following texts
font1 = pygame.font.SysFont('Calibri', 30, True, False) 
font2 = pygame.font.SysFont('Calibri', 20, True, False) 

#texts used on some of the pages
Text_Levels1 = font1.render("LEVELS", True, BLACK) 
Text_Level_Builder1 = font1.render("LEVEL BUILDER", True, BLACK) 
Text_Options1 = font1.render("OPTIONS", True, BLACK) 
Text_Level_Name = font2.render("Level Name:", True, BLACK) 
Text_Level_Creator = font2.render("Level Creator:", True, BLACK)
Text_SFX = font2.render("SFX",True, BLACK)               

#original settings
KLC = RED    #KLC stands for 'killer line colour'
BLC = BLUE   #BLC stands for 'bouncy line colour'
SFX = True
done = False  #this is used to create main loop, once this turns true, loop will stop and window will close

class Button():
    def __init__(self, x, y, width, height, fontsize, word, fill, func): #all the inputs to create a button
        self.x = x      #records buttons x coords for knowing to draw
        self.y = y      #records buttons y coords
        self.width = width   #records buttons width
        self.height = height    #records buttons height
        self.word = word    #records buttons word so that when drawn, the word can be drawn in it
        self.fill = fill    #records colour so that in draw method, can use this to fill button
        self.outline_colour = BLACK  #this is also for the draw function, most of the buttons that will be made have a black outline so if 
        self.func = func  # allows me to give a function to a button
        self.fontsize = fontsize # size of the words in button
        global page
    def draw(self):
        font = pygame.font.SysFont('Calibri', self.fontsize, True, False)  #font of word
        pygame.draw.rect(screen, self.fill, [self.x,self.y,self.width,self.height])  #draws rect from fill, useing x,y,width,height
        pygame.draw.rect(screen, self.outline_colour, [self.x, self.y, self.width, self.height], 3) #draws outline of button
        screen.blit(font.render(self.word,True,BLACK), [self.x + 10, self.y + 10])  #prints the word in the button
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
            elif self.func == "BACK":  #takes a page off stack so goes to previous page
                page.pop()
                return True
            else:
                (self.func)()

class image_button(Button): # child class of button
    def __init__(self,x, y, width, height, fontsize, word, fill, func, image):
        super().__init__(x,y,width,height,fontsize,word,fill,func)  # inheriting the parents attributes
        self.image = pygame.transform.scale(pygame.image.load(image), (self.width - 10,self.height - 10)) # scales the image
    def draw(self):
        pygame.draw.rect(screen, self.fill, [self.x,self.y,self.width,self.height])
        screen.blit(self.image,(self.x + 5, self.y + 5))#shows image
        pygame.draw.rect(screen, self.outline_colour, [self.x, self.y, self.width, self.height], 3)
    def click(self):
        press = pygame.mouse.get_pressed() #so that it does not have to be written down every time used
        #if mouse clicked and in area of button
        if ((press[0] == 1) and (pygame.mouse.get_pos()[0] > self.x) and (pygame.mouse.get_pos()[0] <(self.x + self.width))) and ((pygame.mouse.get_pos()[1] > self.y) and (pygame.mouse.get_pos()[1] < (self.y + self.height)) and (self.func != "")):
            if self.func == "home": #clears the stack and adds start page so only start page there
                page.clear()
                page.append("ST")
            elif self.func == "replay": #re-iniates the game by doing the sequence before the game starts
                page.pop()
                page.append("GA")
            elif self.func == "options": # adds option page and goes there
                page.append("OP")
            elif self.func == "leaderboard": # adds leaderboard page
                page.append("GALE")
global keys
keys = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
#list of keys used for when typing a word in the game

class TextBox(Button):
    def __init__(self, x, y, width, height, fontsize, word, fill, func):
        super().__init__(x,y,width,height,fontsize,word,fill,func)
        self.selected = False
        self.wait = 0
    def type(self):
        if self.wait == 0 and self.selected == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE: #if backspace then word = word  take away a letter
                    self.word = self.word[:(len(self.word)-1)]
                elif event.key == pygame.K_SPACE:
                    self.word = self.word + " "  #when it is a space space is added to the word
                elif event.key != pygame.K_RETURN:
                    self.word = self.word + keys[event.key - 97] #letter a is equivelant to value 97 when pressed
                self.wait = 3  #if a single key is pressed it might add it on more than once if the key is pressed for longer than a twentieth of a second
        else:
            self.wait = self.wait - 1 # takes away a wait period every time nothing happens
    def click(self):
        if ((event.type == pygame.MOUSEBUTTONDOWN) and (pygame.mouse.get_pos()[0] > self.x) and (pygame.mouse.get_pos()[0] <(self.x + self.width))) and ((pygame.mouse.get_pos()[1] > self.y) and (pygame.mouse.get_pos()[1] < (self.y + self.height))):
            for i in TextBoxes: # makes all textboxes unselected
                i.selected = False  
            self.selected = True #makes this textbox selected
    def draw(self):
        font = pygame.font.SysFont('Calibri', self.fontsize, True, False)
        thickness = 3
        if self.selected == True:
            thickness = 5       #makes boarder of textbox thicker if selected
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
        self.spin_direction = 1
    def spin(self):
        self.image_angle += speed*self.spin_direction
        #this adds the variable speed onto image_angle, speed will increase
        self.image = pygame.transform.rotate(self.OG_image, self.image_angle)
        #this is the image that will end up on the screen, (turned by the image_angle)
        self.rect = self.image.get_rect(center = self.center)
        #this is what makes the image look like it is turning via its center
    def move(self):
        rad = math.radians(self.image_angle)
        #radian version of angle as that is version needed for library math.
        self.rect.x += math.sin(rad)*speed*-1                                                       
        self.rect.y += math.cos(rad)*speed*-1
        #moving the object in direction it is pointing
        self.center = (self.center[0] + math.sin(rad)*speed*-1, self.center[1] + math.cos(rad)*speed*-1)
        # changing the position of the center, so that it is in motion with the harpoon


###############################################################             GENERAL                 ######################################################################################

page = ["ST"] # tells system which page its on
number_of_pages = 1 #number of elements in page

#all the buttons within the start page
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
#button used for multiple pages when you want user to be able to go to previous page
SETTINGS = image_button(600, 50, 50, 50, 12, "", WHITE, "options", "settings.png")
#used on pages where you want user to be able to go to settings

###############################################################             END OF GENERAL          ######################################################################################
###############################################################             CONTINUOUS              ######################################################################################
#player name page buttons
PNP_button = TextBox(350,230, 250, 40, 20, "", WHITE, "")
ENTER_button = Button(300,350,100,50,22,"ENTER", GREY, "ADD_GA")
Player_name_words = font2.render("Player name:", True, BLACK)
PNP_button.selected = True
Text_To_Start = font1.render("press space to start", True, BLACK) 

TextBoxes = [PNP_button] # used for all textboxes
def PlayerNamePage(): # draws all buttons for this page and checks to see if user has typed nything or clicked the enter button
    screen.fill(WHITE)
    screen.blit(Player_name_words, [200, 240])
    ENTER_button.draw()
    PNP_button.draw()
    BACK.draw()
    PNP_button.type()
    ENTER_button.click()

speed = 10 #speed that page is scrolling and 
background_colour = [255,255,255] # used to change the background colour

def transition(x): #where x is the colour to be transitioned to
    global move
    if x == GREY:  #for when transitioning to grey all the objects should shade
        move = False
        for i in all_sprites_list:
            for t in range(100):
                i.image.set_alpha(t)   #makes them become more and more shaded quickly
            
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
    #what these do is make the numbers of the background colour closer to that of the new colour,
    #as it is only changing values by 1 each time it become much more of a gradual effect of over a couple of seconds
        
#making all the buttons for the deathscreen
death_screen = Button(200, 50, 300, 400, 20, "", WHITE, "")
REPLAY = image_button(225, 300, 50, 50, 20, "", WHITE, "replay", "replay.png")
HOME = image_button(325, 300, 50, 50, 20, "", WHITE, "home", "home.jpg")
LEADERBOARD = image_button(425, 300, 50, 50, 20, "", WHITE, "leaderboard", "list.png")
background_colour_pointer = 0
scores = [0] #this is used to keep track of the top scores for the leaderboard
scores_added = False #this is used to check wheter the score has been added to the leaderboards

def deathscreen(): #draws all button for deathscreen and checks if they have been clicked
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
    #draws on deathscreen the score and the best score

def add_to_scores(score, name):  #adds the score of the round to the scores list and in order
    global scores
    fin = False #used to see if the position is found
    if len(scores) == 0:
        scores.append(score)
    else:
        for x in range(0, len(scores)-1):
            if score > scores[x][0] and fin == False: #once the new score is larger than a score, it is added to scores in that position
                scores.insert(x, (score, name))
                fin = True #makes sure that score is not added repetitively
    
def leaderboard(): ############ in progress
    death_screen.draw()
    SETTINGS.draw()
    SETTINGS.click()
    for x in range(0,9):
        lettering = (str(x + 1) + "   " + str(scores[x][0]) + "   " + str(scores[x][1]))
        word = font1.render(lettering, True, BLACK)
        screen.blit(word, [220, 60 + 20*x])
        
###############################################################             END OF CONTINUOUS       ######################################################################################
###############################################################             LEVELS                  ######################################################################################
#texts and buttons for the level picker page
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
    BACK.draw()

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
    #if gravity == True:
    #    pygame.draw.rect(screen, GREEN, [200, 100, 50, 50])
    #    pygame.draw.rect(screen, WHITE, [250, 100, 50, 50])
    #    pygame.draw.rect(screen, BLACK, [200, 100, 100, 50], 4)
    #else:
    #    pygame.draw.rect(screen, WHITE, [200, 100, 50, 50])
    #    pygame.draw.rect(screen, GREY, [250, 100, 50, 50])
    #    pygame.draw.rect(screen, BLACK, [200, 100, 100, 50], 4)
    
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
while not done: #once done is true, the window will close
    for event in pygame.event.get(): #gets the state of all possible inputs
        if event.type == pygame.QUIT: #closes window if cross is pressed
            done = True
    #For the paging system the page that the game is on is the last element of the stack
    #page, e.g. "ST" means start
    #ST is start page
    #OP is options page --> 
        # OPKL options colour changer pages for killer line
        # OPBL options colour changer pages for bouncy line
    #CO is continusous start up page
        #GA is the contiuous game set up (this is where all constant are assigned to 0 
            #GACO is when playing the acctual game
    #LV
        #LV1
        #LV2
        #LV3
        #LV4
        #LV5
        #LV6
    #LB - create or edit page
        #LBSP - a create new info fill page
        #LBLO - choosing whcih level to edit
            #LBST - the actual level builder page
    if page[-1] == "ST":   #draws the start page if the st is current age/last in the stack
        StartPage()
        for i in SP_Buttons: #checks if any start page buttons are clicked
            i.click()
    elif page[-1][:2] == "OP": #if first part of last element in page is OP
        if len(page[-1]) == 2:
            OptionsPage()
            for i in OP_Buttons:
                i.click()
            number_of_pages = len(page)
            BACK.click()
        elif page[-1][2:] == "KL": #if last to letters of last element "kl"
            ChangeColour(KLC,BLC)  #change KLC colour 
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
        if page[-1][:2] == "GA": #if last 2 letters of last element in page is ga
            if page[-1] == "GA": #if last element is just ga
                #setting up continuous game

                #creating sprite groups so that we can use group collide
                blocks = pygame.sprite.Group()                                                         
                block_list = [] #used to tell which the next block is that the haropoon should be hitting
                trail = []
                all_sprites_list = pygame.sprite.Group()

                #creates wooden blocks
                for i in range(4):
                    block = Block("wood.jpg")
                    block.rect.x = random.randrange(0,650) #this makes the blocks appear in a random x- coord  that is on-screen
                    block.rect.y = (i*200) - 400 #evenly place them out
                    block.OG_image = pygame.transform.scale(pygame.image.load("wood.jpg"), (20, 20))  #changes the image to the wood image
                    blocks.add(block)             #adds this block to blocks, block_list and all_sprites_list
                    block_list.append(block)
                    all_sprites_list.add(block)

                #creates player
                target = 3                    #makes the target the 4th one in blocks (0 to 3 as index)
                player = Player("harpoongun.png")     #creates the player and call it 
                player.rect.x = 325
                player.rect.y = 300                  #changes the player's x and y coords
                player.center = (325,300)           #records center of the player so that when rotating or moving, the image rotates about center.
                player.OG_image = pygame.transform.scale(pygame.image.load("harpoongun.png"), (50,50))
                all_sprites_list.add(player)

                font = pygame.font.SysFont('Calibri', 30, True, False)
                #setting all the constants to their origonal settings
                spin = False  #tells us whether it has started spinning or not
                move = False  #tells us whether it has started moving or not
                spinable = True  #tells us if harpoon is allowed to start spinning (if it has hit correct previous block)
                start = False  #tells us if game has started so that when it does we can make the screen scroll down
                death = False  #know if player died so we can put up deathscreen when he/she has died
                scores_added = False #allows us to know if the score of that round had been added to the scores list or not
                Player_name = PNP_button.word #so that we can know who got the highest score on the leaderboard
                clock = pygame.time.Clock()
                score = 0  #start it at 0
                page.pop()
                background_colour_pointer = 0
                background_colour = [255,255,255]
                page.append("GACO") #make game start

            if page[-1] == "GACO":
                transition(BACK_COLOURS[background_colour_pointer]) #makes the background colour the colour it should be
                screen.fill(background_colour)
                if start == False:
                    screen.blit(Text_To_Start, (30,400)) #puts press space to start onto the screen if the game has not started yet
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
                        death = True
                    # for moment this stops game if wrong block hit
                if start == True:
                    for sprite in all_sprites_list:
                        sprite.rect.y += (speed-4)
                        sprite.center = (sprite.center[0], sprite.center[1] + (speed-4))
                #makes all srites move down screen by speed
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
                if death != True: #writes score at top left of screen if game is playing
                    screen.blit(score_word, (600, 10))
                elif death == True: # if death is true writes score and best score on the centre of the screen
                    move = False
                    if score > bestscore: #checks to see if most recent score is the best score
                        bestscore = score
                    if scores_added == False:
                        add_to_scores(score, Player_name)  # add score to the scores list in order of greatest to smallest
                        scores_added = True #make sure that the same score isnt being constantly added
                    bestScore_word = font.render("best:" + str(bestscore), True, BLACK) #writing best score on deathscreen
                    transition(GREY) #turns game area grey and makes objects fade
                    deathscreen() #loads deathscreen
            elif page[-1] == "GALE":
                leaderboard() #loads the leaderboard if last element in page is gale
                    
                
##################
        else:
            PlayerNamePage() #if none of the other continuous features, the player name page appears
            BACK.click()
        
    elif page[1] == "LV":  #loads level selecter page
        LevelsPage()
            
    elif page[1] == "LB":           
        if page[-1] == "LB":
            CreateOrEditPage() # loads page where user decides if editing a previous leel or creating an entirely new lvel
        elif page[-1] == "LBSP":
            LevelBuilderStartPage() #loads the new level infor fill out page
        else:
            pass
        BACK.click()
    pygame.display.flip() #shows the virtual screen
    clock.tick(20)  #this is refresh rate per second
pygame.quit()
