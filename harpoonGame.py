import pygame
pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)

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

#original settings
KLC = RED    #ONLC stand for 'killer line colour'
BLC = BLUE
SFX = True

done = False
exit_button = False
ChangeColourClose = False

class Button:
    def __init__(self, coords, size, fontsize, word):
        self.coords = coords
        self.rect = pygame.Rect(coords, size)
        font = pygame.font.SysFont('Calibri', fontsize, True, False)
        self.word = font.render(word, True, BLACK)
    def draw(self):
        pygame.draw.rect(self.rect)
        screen.blit(self.word, [self.coords[0] + 10, self.coords[1] + 10], 4)
    def click(self):
        pass
class OptionsButton(Button):
    def __init__(self):
        Button.__init__(self, [10,10], [10,10])
    def press(self):
        OptionsPage()

def NextPage(CurrentPage):
    pass
def OptionsPage():
    screen.fill(WHITE)
    Text_Killer_Line_Colour = font2.render("Killer Line Colour", True, BLACK)
    Text_Bouncy_Line_Colour = font2.render("Bouncy Line Colour", True, BLACK)
    fee = Button([10,10], [10,10], 11, "fee")
    Button.draw(fee)
    #screen.blit(Text_Killer_Line_Colour, [250, 125])
    #screen.blit(Text_Bouncy_Line_Colour, [250, 275])
    #screen.blit(Text_Options1, [300, 60])
    #pygame.draw.rect(screen, KLC, [100, 100, 100, 100])           #the coordinates is [x,y,width,height], width (if 0 then fill)
    #pygame.draw.rect(screen, BLACK, [100, 100, 100, 100], 4)
    #pygame.draw.rect(screen, BLC, [100, 250, 100, 100])
    #pygame.draw.rect(screen, BLACK, [100, 250, 100, 100], 4)
    if SFX == True:
        pygame.draw.rect(screen, GREEN, [100, 400, 50, 50])
        pygame.draw.rect(screen, WHITE, [150, 400, 50, 50])
        pygame.draw.rect(screen, BLACK, [100, 400, 100, 50], 4)
    else:
        pygame.draw.rect(screen, WHITE, [100, 400, 50, 50])
        pygame.draw.rect(screen, GREY, [150, 400, 50, 50])
        pygame.draw.rect(screen, BLACK, [100, 400, 100, 50], 4)
    pygame.display.flip()
    clock.tick(20)
def ChangeColourBoxRim(x):
    if x == KLC:
        rim = GREEN
    elif x == BLC:
        rim = RED
    else:
        rim = BLACK
        return rim
    
def ChangeColour(x,y):              #(colour being changed, other colour)
    while not ChangeColourClose:
        screen.fill(WHITE)
        pygame.draw.rect(screen, RED, [100, 100, 100, 100])
        pygame.draw.rect(screen, ChangeColourBoxRim(RED), [100, 100, 100, 100], 4)
        pygame.draw.rect(screen, BLUE, [300, 100, 100, 100])
        pygame.draw.rect(screen, ChangeColourBoxRim(BLUE), [300, 100, 100, 100], 4)
        pygame.draw.rect(screen, GREY, [500, 100, 100, 100])
        pygame.draw.rect(screen, ChangeColourBoxRim(GREY), [500, 100, 100, 100], 4)
        pygame.draw.rect(screen, PINK, [100, 300, 100, 100])
        pygame.draw.rect(screen, ChangeColourBoxRim(PINK), [100, 300, 100, 100], 4)
        pygame.draw.rect(screen, ORANGE, [300, 300, 100, 100])
        pygame.draw.rect(screen, ChangeColourBoxRim(ORANGE), [300, 300, 100, 100], 4)
        pygame.draw.rect(screen, YELLOW, [500, 300, 100, 100])
        pygame.draw.rect(screen, ChangeColourBoxRim(YELLOW), [500, 300, 100, 100], 4)
        pygame.screen.flip()
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.quit:
                done = True
            elif ((event.type == pygame.MOUSEBUTTONDOWN) and (pygame.mouse.get_pos()[0] > 100) and (pygame.mouse.get_pos()[0] <200)) and ((pygame.mouse.get_pos()[1] > 100) and (pygame.mouse.get_pos()[1] < 200)):
                x = RED
            elif ((event.type == pygame.MOUSEBUTTONDOWN) and (pygame.mouse.get_pos()[0] > 300) and (pygame.mouse.get_pos()[0] <400)) and ((pygame.mouse.get_pos()[1] > 100) and (pygame.mouse.get_pos()[1] < 200)):
                x = BLUE
            elif ((event.type == pygame.MOUSEBUTTONDOWN) and (pygame.mouse.get_pos()[0] > 500) and (pygame.mouse.get_pos()[0] <600)) and ((pygame.mouse.get_pos()[1] > 100) and (pygame.mouse.get_pos()[1] < 200)):
                x = GREY
            elif ((event.type == pygame.MOUSEBUTTONDOWN) and (pygame.mouse.get_pos()[0] > 100) and (pygame.mouse.get_pos()[0] <200)) and ((pygame.mouse.get_pos()[1] > 300) and (pygame.mouse.get_pos()[1] < 400)):
                x = PINK
            elif ((event.type == pygame.MOUSEBUTTONDOWN) and (pygame.mouse.get_pos()[0] > 300) and (pygame.mouse.get_pos()[0] <400)) and ((pygame.mouse.get_pos()[1] > 300) and (pygame.mouse.get_pos()[1] < 400)):
                x = ORANGE
            elif ((event.type == pygame.MOUSEBUTTONDOWN) and (pygame.mouse.get_pos()[0] > 500) and (pygame.mouse.get_pos()[0] <600)) and ((pygame.mouse.get_pos()[1] > 300) and (pygame.mouse.get_pos()[1] < 400)):
                x = YELLOW
        

#main loop
while not done:
    #start page
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, [250, 55, 200, 90], 4) 
    pygame.draw.rect(screen, BLACK, [250, 155, 200, 90], 4)
    pygame.draw.rect(screen, BLACK, [250, 255, 200, 90], 4)
    pygame.draw.rect(screen, BLACK, [250, 355, 200, 90], 4)
    screen.blit(Text_Harpoon_Game, [242,0])
    screen.blit(Text_Continuous2,[255, 60])
    screen.blit(Text_Levels2,[255, 160])
    screen.blit(Text_Level_Builder2,[255, 260])
    screen.blit(Text_Options2,[255, 360])
    pygame.display.flip()
    Pass = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT or exit_button == True:
            done = True 
    #continuous 
        elif ((event.type == pygame.MOUSEBUTTONDOWN) and (pygame.mouse.get_pos()[0] > 250) and (pygame.mouse.get_pos()[0] <450)) and ((pygame.mouse.get_pos()[1] > 55) and (pygame.mouse.get_pos()[1] < 145)):
            pass
    #levels
        elif ((event.type == pygame.MOUSEBUTTONDOWN) and (pygame.mouse.get_pos()[0] > 250) and (pygame.mouse.get_pos()[0] <450)) and ((pygame.mouse.get_pos()[1] > 155) and (pygame.mouse.get_pos()[1] < 245)):
            pass
    #level_builder
        elif ((event.type == pygame.MOUSEBUTTONDOWN) and (pygame.mouse.get_pos()[0] > 250) and (pygame.mouse.get_pos()[0] <450)) and ((pygame.mouse.get_pos()[1] > 255) and (pygame.mouse.get_pos()[1] < 345)):
            screen.fill(WHITE)
            screen.blit(Text_Level_Builder1, [10,10])
            screen.blit(Text_Level_Name, [10, 40])
            pygame.draw.rect(screen, BLACK, [200, 40, 200, 20], 2)
            screen.blit(Text_Level_Creator, [10, 70])
            pygame.draw.rect(screen, BLACK, [200, 70, 200, 20], 2)
            gravity = False
            if gravity == True:
                pygame.draw.rect(screen, GREEN, [200, 100, 50, 50])
                pygame.draw.rect(screen, WHITE, [250, 100, 50, 50])
                pygame.draw.rect(screen, BLACK, [200, 100, 100, 50], 4)
            else:
                pygame.draw.rect(screen, WHITE, [200, 100, 50, 50])
                pygame.draw.rect(screen, GREY, [250, 100, 50, 50])
                pygame.draw.rect(screen, BLACK, [200, 100, 100, 50], 4)
            pygame.display.flip()
            clock.tick(20)
            if ((event.type == pygame.MOUSEBUTTONDOWN) and (pygame.mouse.get_pos()[0] > 1) and (pygame.mouse.get_pos()[0] <1)) and ((pygame.mouse.get_pos()[1] > 1) and (pygame.mouse.get_pos()[1] <1 )):
                pass
    #options
        elif ((event.type == pygame.MOUSEBUTTONDOWN) and (pygame.mouse.get_pos()[0] > 250) and (pygame.mouse.get_pos()[0] <450)) and ((pygame.mouse.get_pos()[1] > 355) and (pygame.mouse.get_pos()[1] < 445)):
            OptionsPage()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if ((event.type == pygame.MOUSEBUTTONDOWN) and (pygame.mouse.get_pos()[0] > 100) and (pygame.mouse.get_pos()[0] <200)) and ((pygame.mouse.get_pos()[1] > 100) and (pygame.mouse.get_pos()[1] < 200)):
                    ChangeColour(KLC, BLC)
                elif ((event.type == pygame.MOUSEBUTTONDOWN) and (pygame.mouse.get_pos()[0] > 100) and (pygame.mouse.get_pos()[0] <200)) and ((pygame.mouse.get_pos()[1] > 250) and (pygame.mouse.get_pos()[1] < 350)):
                    ChangeColour(BLC, KLC)
                elif ((event.type == pygame.MOUSEBUTTONDOWN) and (pygame.mouse.get_pos()[0] > 100) and (pygame.mouse.get_pos()[0] <200)) and ((pygame.mouse.get_pos()[1] > 250) and (pygame.mouse.get_pos()[1] < 350)):
                    if SFX == True:
                        SFX = False
                    else:
                        SFX = True
pygame.quit()
