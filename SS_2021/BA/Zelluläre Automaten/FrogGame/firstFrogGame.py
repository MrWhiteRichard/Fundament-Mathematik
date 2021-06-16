import pygame
import os
import random
import time
from collections import defaultdict

from pygame.locals import *

sourceFileDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(sourceFileDir)

game_velocity = 27 # ab 40 wird das Spiel erst ziemlich anspruchsvoll ;)

pygame.init()
# pygame.mixer.init()
# pygame.mixer.music.load("Sounds/music.wav")
# pygame.mixer.music.set_volume(0.2)
# pygame.mixer.music.play()

pygame.display.set_caption("Frog Game")

pygame.font.init()
numflyfont = pygame.font.SysFont('Calibri', 13)
numflysurface = numflyfont.render('Number of flies left: ', False, (255, 100, 0))
gameoverfont = pygame.font.SysFont('Calibri', 45)
gameoversurface = gameoverfont.render('GAME OVER', False, (255, 100, 0))
tryagainfont = pygame.font.SysFont('Calibri', 35)
tryagainsurface = tryagainfont.render('Click Return to try again', False, (255, 100, 0))
winnerfont = pygame.font.SysFont('Calibri', 45)
winnersurface = winnerfont.render('WINNER', False, (255, 100, 0))
descriptionfont1 = pygame.font.SysFont('Calibri', 13)
descriptionsurface1 = descriptionfont1.render('Press one of the arrow keys to catch a fly, press spacebar to dive under water and escape from the stork. But watch out, you can only take one action at a time and each costs you energy.', False, (255,100,0))
descriptionfont2 = pygame.font.SysFont('Calibri', 13)
descriptionsurface2 = descriptionfont2.render('Fortunately eating flies gives you new energy - the goal is to catch \'em all. If you lose a live, just press the return key to start again!', False, (255,100,0))


tonguelength = 9
tongue_velocity = 5
health = 30

black = (0,0,0)
white = (255, 255, 255)
grey = (210, 210, 210)
green = (0, 255, 0, 10)
red = (255, 0, 0)
dark_red = (120, 0, 0)
light_red = (255, 110, 110)
water_blue = (156, 211, 219)
light_green = (160, 255, 160)

permeability = 1

cell_size = 4
rows = 120
cols = 220

directions = {'left': [0,-1], 'right': [0,1], 'up': [-1,0], 'down':[1,0], 'northeast':[-1,1], 'northwest':[-1,-1], 'southeast': [1,-1], 'southwest': [1,1]}

slurpSound = pygame.mixer.Sound("Sounds/slurp.wav")
splashSound = pygame.mixer.Sound("Sounds/splash.wav") # Music used from https://www.FesliyanStudios.com
gameoverSound = pygame.mixer.Sound("Sounds/mixkit-retro-arcade-game-over-470.wav")
winnerSound = pygame.mixer.Sound("Sounds/mixkit-game-level-completed-2059.wav")


grid_width = cell_size * cols 
grid_height = cell_size * rows

window_size = [int(grid_width) + 150, int(grid_height) + 95]
screen = pygame.display.set_mode(window_size)






class Stork:
    def __init__(self, part, direction):
        self.part = part
        self.direction = direction
        if part in ('outer', 'black'):
            self.color = black
        elif part == 'white':
            self.color = white
        elif part == 'shaded':
            self.color = grey
        elif part == 'darksnabel':
            self.color = red
        elif part == 'lightsnabel':
            self.color = light_red


class Frog:
    def __init__(self, part, direction, tonguestate = 0, uppertongue = False, originaltongue = False):
        self.part = part
        if part == 'body':
            self.color = green
        elif part == 'outer':
            self.color = black
        elif part == 'inner':
            self.color = black
        elif part == 'white':
            self.color = white
        elif part == 'tongue':
            self.color = red
            self.tonguestate = tonguestate
            self.uppertongue = uppertongue
            self.originaltongue = originaltongue
        self.direction = direction

    def lowerTonguestate(self):
        self.tonguestate -= 1


class Fly:
    def __init__(self, part, direction):
        self.part = part
        if part == 'body':
            self.color = black
        else:
            self.color = white
        self.direction = direction

    
    def change_direction(self):
        self.direction = [- self.direction[0], -self.direction[1] ]


class CellularAutomaton:
    def __init__(self, health = 0, under_water = False):
        self.under_water = under_water
        self.full = pygame.image.load("Grafiken/full.png")
        self.full.set_alpha(128)
        self.empty = pygame.image.load("Grafiken/empty.png")
        self.empty.set_alpha(128)
        self.lives = 3
        self.health = health
        self.health_displayed = health
        self.numflies = 0
        self.storks = defaultdict(list)
        self.frogs = defaultdict(list)
        self.flies = defaultdict(list)
        self.paused = False
        self.game_over = False
        self.winner = False

    def drawHearts(self):
        if self.lives >= 1:
            screen.blit(self.full, (20,20))
        else:
            screen.blit(self.empty, (20,20))
        if self.lives >= 2:
            screen.blit(self.full, (80,20))
        else:
            screen.blit(self.empty, (80,20))
        if self.lives == 3:
            screen.blit(self.full, (140,20))
        else:
            screen.blit(self.empty, (140,20))

    def drawLife(self):
        for i in range(100):
            color = ( (100-i)*240/100, 255, (100-i)*240/100)
            pygame.draw.rect(screen, color, [20+7*i, window_size[1]-80, 7, 20])
        if self.health_displayed < self.health:
            self.health_displayed = min(self.health, self.health_displayed + 1)
        elif self.health_displayed > self.health:
            self.health_displayed = max(self.health, self.health_displayed - 1)
        pygame.draw.rect(screen, black, [20+7*int(self.health_displayed), window_size[1]-80, 5, 20])
        
    def drawFlyStanding(self):
        screen.blit(numflysurface, (window_size[0]-140,window_size[1]-100))
        flycountfont = pygame.font.SysFont('Calibri', 15)
        flycountsurface = flycountfont.render(str(self.numflies), False, (255, 100, 0)) 
        screen.blit(flycountsurface, (window_size[0]-30, window_size[1]-100))  
        
    def writeDescription(self):
        screen.blit(descriptionsurface1, (10,window_size[1]-50))   
        screen.blit(descriptionsurface2, (10,window_size[1]-25)) 
    

    def isOccupied(self, row, col):
        if (row, col) in self.storks or (row, col) in self.frogs or (row, col) in self.flies:
            return True
        else:
            return False

    def willBeOccupied(self, row, col):
        for direction, dir in directions.items():
            if (( (row+dir[0])%rows, (col+dir[1])%cols ) in self.storks and self.storks[( (row+dir[0])%rows, (col+dir[1])%cols )][0].direction == direction) or (( (row+dir[0])%rows, (col+dir[1])%cols ) in self.flies and self.flies[( (row+dir[0])%rows, (col+dir[1])%cols )][0].direction == direction) or (( (row+dir[0])%rows, (col+dir[1])%cols ) in self.frogs and self.frogs[( (row+dir[0])%rows, (col+dir[1])%cols )][0].direction == direction):
                return True
        return False

    def appendStork(self, Stork, row, col):
        if (row, col) not in self.storks.keys():
            self.storks[(row, col)].append(Stork)
        
    def appendFrog(self, Frog, row, col):
        self.frogs[(row,col)].append(Frog)

    def appendFly(self, Fly, row, col):
        self.flies[(row, col)].append(Fly)
        self.numflies += 1

    def updateStorks(self):
        updated = CellularAutomaton()
        for (row, col), cell in self.storks.items():
            for stork in cell:
                updated.appendStork(stork, (row+stork.direction[0])%rows, (col+stork.direction[1])%cols)
                for dir in directions.values():
                    if (( (row-dir[0])%rows, (col-dir[1])%cols ) in self.frogs and self.frogs[( (row-dir[0])%rows, (col-dir[1])%cols )][0].direction == dir):
                        if not self.paused:
                            self.paused = True
                            pygame.mixer.music.fadeout(500)
                            pygame.mixer.Sound.play(gameoverSound)
        return updated.storks

    def updateFrogs(self):
        updated = CellularAutomaton()
        for (row, col), cell in self.frogs.items():
            for frog in cell:
                updated.appendFrog(frog, (row+frog.direction[0])%rows, (col+frog.direction[1])%cols)
        return updated.frogs

    def updateflies(self):
        updated = CellularAutomaton()
        for (row, col), cell in self.flies.items():
            for fly in cell:
                if self.isOccupied((row+fly.direction[0])%rows, (col+fly.direction[1])%cols) or self.willBeOccupied((row+fly.direction[0])%rows, (col+fly.direction[1])%cols):
                        fly.change_direction()
                        updated.appendFly(fly, (row+2*fly.direction[0])%rows, (col+2*fly.direction[1])%cols)
                        continue
                updated.appendFly(fly, (row+fly.direction[0])%rows, (col+fly.direction[1])%cols)
        return updated.flies

    def update(self):
        storks = self.updateStorks()
        if not self.paused:
            self.frogs = self.updateFrogs()
            self.flies = self.updateflies()
            self.storks = storks
        else:
            self.lives -= 1

   
    def updateTongueStorks(self):
        updated = CellularAutomaton()
        for (row, col), cell in self.storks.items():
            for stork in cell:
                updated.appendStork(stork, (row+stork.direction[0])%rows, (col+stork.direction[1])%cols)
                for dir in directions.values():
                    if (( (row-dir[0])%rows, (col-dir[1])%cols ) in self.frogs and self.frogs[( (row-dir[0])%rows, (col-dir[1])%cols )][0].direction == dir):
                        if not self.paused:
                            self.paused = True
                            # pygame.mixer.music.fadeout(500)
                            pygame.mixer.Sound.play(gameoverSound)
        return updated.storks

    def updateTongueFrogs(self, dir):
        updated = CellularAutomaton()
        for (row, col), cell in self.frogs.items():
            for frog in cell:
                if frog.part == 'tongue':
                    if frog.tonguestate <= 0 and not frog.originaltongue:
                        continue   
                    else:
                        if frog.uppertongue == True:
                            updated.appendFrog(Frog('tongue', frog.direction, tonguestate=frog.tonguestate-2, uppertongue=True), (row + frog.direction[0] + tongue_velocity*dir[0]) % rows, (col + frog.direction[1] + tongue_velocity*dir[1]) % cols)
                            for i in range(1,tongue_velocity):
                                updated.appendFrog(Frog('tongue', frog.direction, tonguestate=frog.tonguestate-2, uppertongue=False), (row + frog.direction[0] + i*dir[0]) % rows, (col + frog.direction[1] + i*dir[1]) % cols)
                            frog.uppertongue = False
                        frog.tonguestate -= 1                
                updated.appendFrog(frog, (row+frog.direction[0])%rows, (col+frog.direction[1])%cols)
        return updated.frogs

    def updateTongueflies(self, dir):
        updated = CellularAutomaton()
        for (row, col), cell in self.flies.items():
            for fly in cell:
                if ((row+fly.direction[0])%rows, (col+fly.direction[1])%cols ) in self.flies.keys() or ((row+fly.direction[0])%rows, (col+fly.direction[1])%cols ) in self.frogs.keys() or ((row+2*fly.direction[0])%rows, (col+2*fly.direction[1])%cols ) in self.flies.keys() or ((row+2*fly.direction[0])%rows, (col+2*fly.direction[1])%cols ) in self.frogs.keys():
                    if any(neighbor.part == 'tongue' for neighbor in self.frogs[((row+fly.direction[0])%rows, (col+fly.direction[1])%cols )]) or any(neighbor.part == 'tongue' for neighbor in self.frogs[((row+2*fly.direction[0])%rows, (col+2*fly.direction[1])%cols )]):
                        self.health = min(100, self.health + 10)
                        self.numflies -=1
                        if self.numflies == 0:
                            self.winner = True
                            pygame.mixer.Sound.play(winnerSound)
                        continue
                    elif any(neighbor.part == 'outer' for neighbor in self.frogs[((row+fly.direction[0])%rows, (col+fly.direction[1])%cols )]):
                        fly.change_direction()
                        updated.appendFly(fly, (row+2*fly.direction[0])%rows, (col+2*fly.direction[1])%cols)
                        continue
                updated.appendFly(fly, (row+fly.direction[0])%rows, (col+fly.direction[1])%cols)
        return updated.flies

    def updateTongue(self, dir):
        storks = self.updateTongueStorks()
        if not self.paused:
            self.frogs = self.updateTongueFrogs(dir)
            self.flies = self.updateTongueflies(dir)
            self.storks = storks
        else:
            self.lives -= 1



    def updateUnderWaterStorks(self):
        updated = CellularAutomaton()
        for (row, col), cell in self.storks.items():
            for stork in cell:
                updated.appendStork(stork, (row+stork.direction[0])%rows, (col+stork.direction[1])%cols)
        return updated.storks

    def updateUnderWaterFrogs(self):
        updated = CellularAutomaton()
        for (row, col), cell in self.frogs.items():
            for frog in cell:
                updated.appendFrog(frog, (row+frog.direction[0])%rows, (col+frog.direction[1])%cols)
        return updated.frogs

    def updateUnderWaterflies(self):
        updated = CellularAutomaton()
        for (row, col), cell in self.flies.items():
            for fly in cell:
                if self.isOccupied((row+fly.direction[0])%rows, (col+fly.direction[1])%cols) or self.willBeOccupied((row+fly.direction[0])%rows, (col+fly.direction[1])%cols):
                        fly.change_direction()
                        updated.appendFly(fly, (row+2*fly.direction[0])%rows, (col+2*fly.direction[1])%cols)
                        continue
                updated.appendFly(fly, (row+fly.direction[0])%rows, (col+fly.direction[1])%cols)
        return updated.flies

    def updateUnderWater(self):
        self.frogs = self.updateUnderWaterFrogs()
        self.flies = self.updateUnderWaterflies()
        self.storks = self.updateUnderWaterStorks()

    def changeFrogsDirection(self, direction):
        for cell in self.frogs.values():
            for frog in cell:
                frog.direction = direction

    def changeStorksDirection(self, direction):
        for cell in self.storks.values():
            cell[0].direction = direction


    def reviveOriginalTongues(self):
        for cell in self.frogs.values():
                    for frog in cell:
                        if frog.part == 'tongue' and frog.originaltongue:                          
                            frog.tonguestate =2*tonguelength
                            frog.uppertongue = True

    def draw(self):
        screen.fill(black)
        if not self.game_over and not self.winner:
            pygame.draw.rect(screen, water_blue, [0, 0, grid_width, grid_height])

            for (row, col), cell in self.frogs.items():
                for frog in cell:
                    color = frog.color
                    if color == red:
                        if self.under_water:
                            color = (156*(10-permeability)/10 + color[0]*permeability/10, 211*(10-permeability)/10 + color[1]*permeability/10, 219*(10-permeability)/10 + color[2]*permeability/10)
                        pygame.draw.rect(screen, color, [cell_size * col , cell_size * row, cell_size, cell_size])
                        break
                    elif color == green:
                        color = ( (100-self.health)*240/100, 255, (100-self.health)*240/100)
                    if self.under_water:
                        color = (156*(10-permeability)/10 + color[0]*permeability/10, 211*(10-permeability)/10 + color[1]*permeability/10, 219*(10-permeability)/10 + color[2]*permeability/10)
                    pygame.draw.rect(screen, color, [cell_size * col, cell_size * row, cell_size, cell_size])

            for (row, col), cell in self.flies.items():
                for fly in cell:
                    color = fly.color
                    pygame.draw.rect(screen, color, [cell_size * col, cell_size * row, cell_size, cell_size])

            for (row, col), cell in self.storks.items():
                for stork in cell:
                    color = stork.color
                    pygame.draw.rect(screen, color, [cell_size * col, cell_size * row, cell_size, cell_size])

            self.drawHearts()
            self.drawLife()
            self.drawFlyStanding()
            self.writeDescription()
        elif self.game_over:
            screen.blit(gameoversurface, (100,100))
            screen.blit(tryagainsurface, (100, 200))
        else: 
            screen.blit(winnersurface, (100,100))
            screen.blit(tryagainsurface, (100, 200))          

    def startWithNewLife(self):
        self.paused = False
        self.under_water = True
        self.health = max(CA.health, 30)
        self.removeTongues()


    def removeTongues(self):
        for (row, col), cell in self.frogs.items():
            for frog in cell:
                if frog.part == 'tongue' and not frog.originaltongue:
                    cell.remove(frog)
        self.reviveOriginalTongues()


    def startNewRound(self):
        global counter1, counter2, t
        self.game_over = False
        self.winner = False
        self.lives = 3
        self.health = 30
        self.numflies = 0
        self.storks = defaultdict(list)
        self.frogs = defaultdict(list)
        self.flies = defaultdict(list)
        self.paused = False
        self.makeLevelOne()
        counter1 = 0
        counter2 = 0
        t = 0



    def createFrog(self, direction, row, col):
        outer = [ [-6,0], [7,0], [-6,1], [7,1], [-7,2], [6,2], [-8,3], [7,3], [-8,4], [6,4], [-8,5], [7,5], [3,5], [-7,6], [7,6], [-3,6], [2,6], [4,6], [-6,7], [-5,7], [-4,7], [-2,7], [1,7], [4,7], [7,7], [-1,8], [0,8], [5,8], [6,8]]
        white = [ [4,0], [5,0], [6,0], [5,1], [6,1], [-6,2], [-5,2], [-4,2], [-7,3], [-6,3], [-5,3], [-4,3], [-3,3], [-7,4], [-4,4], [-3,4], [-7,5], [-4,5], [-3,5], [-6,6], [-5,6], [-4,6]]
        inner = [ [0,1], [0,2], [0,3], [0,4], [2,4], [-6,4], [-5,4], [-1,5], [2,5], [-6,5], [-5,5], [5,6] ]
        body = [ [i, 0] for i in range(-5, 4) if i != 0 ] + [ [i, 1] for i in range(-5, 5) if i != 0 ] + [ [i, 2] for i in range(-3, 6) if i != 0 ] + [ [i, 3] for i in range(-2, 7) if i != 0 ] + [ [i, 4] for i in range(-2, 6) if i != 0 and i != 2] + [ [-2,5], [0,5], [1,5], [4,5], [5,5], [6,5], [-2,6], [-1,6], [0,6], [1,6], [6,6], [-1,7], [0,7], [5,7], [6,7]]
        cells = {'outer': outer, 'white': white, 'inner': inner, 'body': body}
        for type in cells:
            for cell in cells[type]:
                self.appendFrog(Frog(type, direction), row+cell[0], col+cell[1])
                if cell[1] != 0:
                    self.appendFrog(Frog(type, direction), row+cell[0], col-cell[1])
        self.appendFrog(Frog('tongue', direction, tonguestate = 2*tonguelength, uppertongue = True, originaltongue=True), row, col)

    def createStork(self, direction, row, col):
        outer = [ [0,0], [0,1], [0,2], [-1,1], [-2,2], [-3,3], [-3,4], [-4,5], [-4,6], [-4,7], [-4,8], [-4,9], [-4,10], [-4,11], [-3,12], [-4,13], [-5,13],[-6,12], [-7,11], [-8,11], [-9,11], [-10, 12], [-11,13], [-11,14], [-11,15], [-10,16], [-9,17], [-9,18], [-9,19], [-9,20], [-9,21], [-8,22], [-8,23], [-7,24], [-6,24], [-6,23], [-6,22], [-6,21], [-6,20], [-6,19], [-5,17], [-5,16], [-4,15], [-3,15], [-2,15], [-1,14], [0,14], [1,13], [2,12], [2,11], [3,10], [4,10], [5,10], [6,10], [7,10], [8,9], [7,9], [6,8], [7,7], [6,7], [5,6], [6,5], [5,5], [4,4], [3,4], [2,4], [1,3] ]
        white = [ [-2,4], [-2,5], [-3,5], [-3,6]] + [[i,j] for i in range(-3,3) for j in range(7,10)] + [[-2,10], [-3,10], [-1,11], [-2,11], [-3,11], [-1,12], [-2,12], [-2,13], [-3,13]] + [[i,14] for i in range(-10, -2)] + [[-7,13], [-8,13], [-9,13], [-7,15], [-9,15], [-10,15], [-8,16], [-9, 16]]
        shaded = [ [-1,2], [0,3], [-1,3], [-2,3], [0,4], [-1,4], [3,5], [2,5], [1,5], [2,6], [1,6], [0,6], [-1,6], [4,7], [3,7], [3,8], [5,9], [4,9], [3,9], [1,11], [0,11], [1,12], [0,12], [0,13], [-1,13], [-2,14], [-6,13], [-7,12], [-8,12], [-9,12], [-10,13]]
        black = [[-8, 15], [1,4], [0,5], [-1,5], [-2,6], [4,5], [4,6], [3,6], [5,7], [5,8], [4,8], [6,9], [2,10], [1,10], [0,10], [-1,10], [-5,15], [-6,15], [-6,18]]
        dark_snabel = [ [-6,16], [-7,16], [-6,17]]
        light_snabel = [[i, j] for i in range(-8, -6) for j in range(17,22)] + [ [-7,22], [-7,23]]

        cells = {'outer': outer, 'white': white, 'shaded': shaded, 'black': black, 'darksnabel': dark_snabel, 'lightsnabel': light_snabel}
        for type in cells:
            for cell in cells[type]:
                self.appendStork(Stork(type, direction), row+cell[0], col+cell[1])

    def makeLevelOne(self):
        # self.createFrog([0, -1], 30, 60)
        # self.createFrog([-1, 0], 90, 140)
        self.createFrog([-1, 0], 62, 70)

        self.createStork([1,0], 100,100)

        self.appendFly(Fly('body', [1, 0]), 93, 50)
        self.appendFly(Fly('body', [0, -1]), 99, 50)
        self.appendFly(Fly('body', [0, -1]), 20, 50)
        self.appendFly(Fly('body', [0, 1]), 9, 55)
        self.appendFly(Fly('body', [0, 1]), 60, 55)
        self.appendFly(Fly('body', [0, 1]), 21, 65)
        self.appendFly(Fly('body', [0, 1]), 12, 59)
        self.appendFly(Fly('body', [0, 1]), 6, 55)
        self.appendFly(Fly('body', [0, 1]), 13, 56)
        self.appendFly(Fly('body', [0, 1]), 84, 10)
        self.appendFly(Fly('body', [0, 1]), 15, 75)
        self.appendFly(Fly('body', [0, 1]), 8, 75)
        self.appendFly(Fly('body', [0, 1]), 7, 95)
        self.appendFly(Fly('body', [0, 1]), 26, 55)
        self.appendFly(Fly('body', [0, 1]), 17, 65)
        self.appendFly(Fly('body', [0, -1]), 64, 90)
        self.appendFly(Fly('body', [0, -1]), 19, 50)
        self.appendFly(Fly('body', [1, 0]), 17, 50)

#######################################################################################
#######################################################################################
#######################################################################################


CA = CellularAutomaton(health = 30)
CA.makeLevelOne()

    
started = False

clock1 = pygame.time.Clock()

while not started:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and (event.key == K_RETURN or event.key == K_ESCAPE)):
            started = True

    CA.draw()
    clock1.tick(60)

    pygame.display.flip()


clock = True

clock2 = pygame.time.Clock()

t = 0
running = True
counter1 = 0
counter2 = 0
buttons = {K_UP: [-1, 0], K_DOWN: [1, 0], K_RIGHT: [0, 1], K_LEFT: [0, -1]}

# changes = {127: [1,1], 300: [1,0], 480: [-1,1]}

while running: 
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE): # game ends and pygame window is closed
            running = False

    if not CA.paused and not CA.game_over and not CA.winner: # game is running and is updated every timestep
        for event in events:
            if counter1 == 0 and counter2 == 0 and event.type == KEYDOWN and event.key in (K_UP, K_DOWN, K_RIGHT, K_LEFT, K_SPACE):
                if event.key == K_SPACE:
                    counter2 = 60
                    CA.health -= 6
                    CA.under_water = True # used in self.draw(), to make frog disappear
                    if CA.health < 0:
                        CA.paused = True
                        CA.lives -= 1
                        continue
                else:
                    dir = buttons[event.key]
                    counter1 = 2*tonguelength
                    CA.health -= 3
                    if CA.health < 0:
                        CA.paused = True
                        CA.lives -= 1
                        continue
    
        if counter1 == 0 and counter2 == 0:
            CA.update()
        elif counter1 != 0:
            CA.updateTongue(dir)
            if counter1 == 2*tonguelength:
                pygame.mixer.Sound.play(slurpSound)
            if counter1 == 1:
                CA.reviveOriginalTongues()
            counter1 -= 1
        else:
            CA.updateUnderWater()
            if counter2 == 60:
                pygame.mixer.Sound.play(splashSound)
            if counter2 == 1:
                CA.under_water = False
            counter2 -= 1

        t += 1
        if t%100 == 0:
            frog_new_dir = [random.randint(-1,1), random.randint(-1,1)]
            CA.changeFrogsDirection(frog_new_dir)

        if t%127 == 0:
            stork_new_dir = [random.randint(-1,1), random.randint(-1,1)]
            CA.changeStorksDirection(stork_new_dir)
    elif not CA.game_over and not CA.winner: # if frog and stork have collided, player has lost one live and game is paused
        if CA.lives <= 0:
            if not CA.game_over:
                CA.game_over = True
        else:
            for event in events:
                if event.type == KEYDOWN and event.key == K_RETURN:
                    CA.startWithNewLife()
                    if counter1 != 0:
                        counter1 = 0
                    counter2 = 60                    
 
    elif not CA.winner:
        for event in events:
            if event.type == KEYDOWN and event.key == K_RETURN:
                CA.startNewRound()

    else:
        for event in events:
            if event.type == KEYDOWN and event.key == K_RETURN:
                CA.startNewRound()
    
    CA.draw()
    
    if clock:
        clock2.tick(game_velocity)

    pygame.display.flip() 

pygame.quit()
