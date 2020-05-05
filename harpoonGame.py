#version 2.0 05/05/2020
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

#This is object code for most sprites - including player, wooden blocks, final blocks, killer blocks, blouncy blocks 
class Block (pygame.sprite.Sprite):
    def __init__(self, image, width = 50, height = 50):
        #width and height are for how large you want the block
        pygame.sprite.Sprite.__init__(self)
        self.width = width                                                              #this and next is so that I can use/change these attributes in methods of this object
        self.height = height
        self.OG_image = pygame.transform.scale(pygame.image.load(image), (self.width,self.height))
        self.image_angle = random.randrange(0,360)                                     #used to make the image the angle that it is meant to be turned
        self.image = pygame.transform.rotate(self.OG_image, self.image_angle)          #this is the original image, which i use when the object is turned (as if constantly changing same image, it will deform)
        self.center = self.OG_image.get_rect().center                                  #this is used to change the image x,y coords
        self.rect = self.OG_image.get_rect(center = self.center)                       #this is used to reposition the image so that when turned it, turns around center

        


class Create(Block):
    def __init__(self, image):
        super().__init__(image)
        self.image_angle = 0
        self.image = pygame.transform.rotate(self.OG_image, self.image_angle)
        self.image_file = image
        self.rect.x = 100      #start x position
        self.rect.y = 100      #start y positionw
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
            elif self.func == "enter":
                if page[1] == "CO":
                    page.append("GA")
                elif page[1] == "LB":
                    page.append("LBLB")
            elif self.func == "BACK":  #takes a page off stack so goes to previous page
                page.pop()
                return True
            else:
                (self.func)()

class image_button(Button): # child class of button
    def __init__(self,x, y, width, height, fontsize, word, fill, func, image):
        super().__init__(x,y,width,height,fontsize,word,fill,func)  # inheriting the parents attributes
        self.image = pygame.transform.scale(pygame.image.load(image), (self.width - 10,self.height - 10)) # scales the image
        pygame.draw.rect(screen, self.fill, [self.x,self.y,self.width,self.height])
        pygame.draw.rect(screen, self.outline_colour, [self.x, self.y, self.width, self.height], 3)
        self.clickedon = False #this is to make sure that the save action is not repeated within 1 click
    def draw(self):
        screen.blit(self.image,(self.x + 5, self.y + 5))#shows image
    def click(self):
        press = pygame.mouse.get_pressed() #so that it does not have to be written down every time used
        R = "" #this is to the string that would be saved into computer
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
        elif self.wait > 0:
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
        screen.blit(font.render(self.word,True,BLACK), [self.x + 5, self.y + 5])
            


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
ENTER_button = Button(300,350,100,50,22,"ENTER", GREY, "enter")
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
    ENTER_button.draw()
##    Level_Gravity.draw()
    Level_Name.click()
    Level_Creator.click()
    ENTER_button.click()
    Level_Name.type()
    Level_Creator.type()
    BACK.draw()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_k:
        print("ADSF")
##    if gravity == True:
##        pygame.draw.rect(screen, GREEN, [200, 100, 50, 50])
##        pygame.draw.rect(screen, WHITE, [250, 100, 50, 50])
##        pygame.draw.rect(screen, BLACK, [200, 100, 100, 50], 4)
##    else:
##        pygame.draw.rect(screen, WHITE, [200, 100, 50, 50])
##        pygame.draw.rect(screen, GREY, [250, 100, 50, 50])
##        pygame.draw.rect(screen, BLACK, [200, 100, 100, 50], 4)

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

#def transform():w
    
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
        elif page[-1] == "LBLB":
            all_sprites_list = pygame.sprite.Group()
            all_killer_blocks_list = pygame.sprite.Group()
            all_bouncy_blocks_list = pygame.sprite.Group()
            all_checkpoint_blocks_list = pygame.sprite.Group()
            all_final_blocks_list = pygame.sprite.Group()
            page.pop()
            page.append("LBLC")
            task = False
        elif page[-1] == "LBLC":
            if event.type == pygame.KEYDOWN and task == False:
                if event.key == KillerBlockKey: #when the key that is assigned to making a killer line is pressed, originally k is pressed
                    killer = Create(klc_image)  #a object called killer is created, with image of kl
                    all_killer_blocks_list.add(killer) 
                    all_sprites_list.add(killer)   #killer is added to all_blocks_list and all_sprites_list
                elif event.key == BouncyBlockKey:  #when the key that is assigned to making a killer line is pressed, originally k is pressed
                    bouncy = Create(blc_image)   #a object called bouncy is created, with image of bl
                    all_bouncy_blocks_list.add(bouncy)
                    all_sprites_list.add(bouncy)   #bouncy is added to all_blocks_list and all_sprites_list
                elif event.key == CheckpointBlockKey:  #when the key that is assigned to making a killer line is pressed, originally k is pressed
                    checkpoint = Create("wood.jpg")  #a object called checkpoint is created, with image of wooden block
                    all_checkpoint_blocks_list.add(checkpoint)
                    all_sprites_list.add(checkpoint)   #checkpoint is added to all_blocks_list and all_sprites_list
                elif event.key == FinalBlockKey:  #when the key that is assigned to making a killer line is pressed, originally k is pressed
                    final = Create("wood.jpg")   #a object called final is created, with image of a final wooden block
                    all_final_blocks_list.add(final)
                    all_sprites_list.add(final)   #final is added to all_blocks_list and all_sprites_list
                elif event.key == pygame.K_UP:
                    for i in all_sprites_list:
                        i.grow()
                elif event.key == pygame.K_DOWN:
                    for i in all_sprites_list:
                        i.shrink()
                task = True
            elif event.type == pygame.KEYUP:
                task = False
            screen.fill(WHITE)
            SETTINGS.draw()
            SAVE.draw()
            QUIT.draw()#buttons are drawn
            BACK.draw()
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
            all_sprites_list.draw(screen)
        BACK.click()
    pygame.display.flip() #shows the virtual screen
    clock.tick(20)  #this is refresh rate per second
pygame.quit()
