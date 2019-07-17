import pygame
pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)

time.sleep(60)

BLACK = (255, 255, 255)
WHITE = (0,0,0)

pygame.display.set_caption("harpoon")
pygame.font.SysFont('Calibri', 25, True, BLACK)

done = False
exit_button == False

#main loop
while not done:
    #start page
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, [250, 55, 200, 90]) #the coordinates I think is [x,y,width,height]
    pygame.draw.rect(screen, BLACK, [250, 155, 200, 90])
    pygame.draw.rect(screen, BLACK, [250, 255, 200, 90])
    pygame.draw.rect(screen, BLACK, [250, 355, 200, 90])
    font = pygame.font.SysFont('Calibri', 32, True, False)
    text1 = font.render("CONTINUOUS", True, WHITE)
    text2 = font.render("LEVELS", True, WHITE)
    text3 = font.render("LEVEL BUILDER", True, WHITE)
    text4 = font.render("OPTIONS", True, WHITE)
    screen.blit(text1,[255, 60])
    screen.blit(text2,[255, 160])
    screen.blit(text3,[255, 260])
    screen.blit(text4,[255, 360])
    for event in pygame.event.get():
        if event.type == event.QUIT or exit_button == True:
            done = True 
    #continuous 
        elif ((pygame.mouse.get_pos()[0] > 250) and (pygame.mouse.get_pos()[0] <450)) and ((pygame.mouse.get_pos()[1] > 55) and (pygame.mouse.get_pos()[1] < 145)):
            pass
    #levels
        elif ((pygame.mouse.get_pos()[0] > 250) and (pygame.mouse.get_pos()[0] <450)) and ((pygame.mouse.get_pos()[1] > 155) and (pygame.mouse.get_pos()[1] < 245)):
            pass
    #level_builder
        elif ((pygame.mouse.get_pos()[0] > 250) and (pygame.mouse.get_pos()[0] <450)) and ((pygame.mouse.get_pos()[1] > 255) and (pygame.mouse.get_pos()[1] < 345)):
            pass
    #options
        elif ((pygame.mouse.get_pos()[0] > 250) and (pygame.mouse.get_pos()[0] <450)) and ((pygame.mouse.get_pos()[1] > 355) and (pygame.mouse.get_pos()[1] < 445)):
            pass
