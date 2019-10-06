import pygame
import random 
pygame.init()

size = (700,500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

WHITE = (255,255,255)

t = None
start = False
speed = 0
coords = [[None,None], [None,None], [None,None], [None,None]] # coords of the blocks
for i in range(len(coords)):
    coords[i][0] = random.randrange(0,650)
    coords[i][1] = i*100
Wooden_Blocks = []
class wood:
    def __init__(self, t, coords):
        global Wooden_Blocks
        self.t = t
        self.coords = coords
        Wooden_Blocks.append(pygame.transform.scale(pygame.image.load("wood.jpg"), (100, 100)))
    def draw(self):
        if start == True:
            Wooden_Blocks[self.t][1][1] += score
        screen.blit(Wooden_Blocks[self.t],(self.coords[0],self.coords[1]))

wood_objects = [wood(0, coords[0]),wood(1, coords[1]),wood(2, coords[2]), wood(3, coords[3])]
def update_object_coords():
    wood.coords = coords

def ContinuousGame():
    update_object_coords()
    for i in wood_objects:
        i.draw()
screen.fill(WHITE)
ContinuousGame()
pygame.display.flip()
