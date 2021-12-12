import pygame
import sys
from os import path
#from camera import *
 
# Initialize the game engine
pygame.init()
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BOOGIEGREEN = (36, 255, 43)

#TILES
WIDTH=1024
HEIGHT=768
TILESIZE=32
GRIDWIDTH = WIDTH/TILESIZE  # 32 squares
GRIDHEIGHT = HEIGHT/TILESIZE # 24 squares
#funny variables
score = 0 
timerfps= 0
timer = 120
timersec = 0
timermin = 0
# Set the height and width of the screen
size = (WIDTH, HEIGHT) # need a whole number of squares so wholly divisible by 32
screen = pygame.display.set_mode(size)

game_folder=path.dirname(__file__)
map_data=[]
with open(path.join(game_folder, 'map.txt'), 'rt')as f:
    for line in f:
        map_data.append(line)

       

        
pygame.key.set_repeat(500,100)  #lets held down key repeat


########make player class  ############


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, TILESIZE):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(BLUE)
        self.rect=self.image.get_rect()
        
        self.x=x
        self.y=y
    def move(self, x_offset, y_offset, walls_list):  #take in walls list, iterate through to check if a wall occup
        #ies the next location. Make flag moving false if so so no movement possible.
        
        moving=True
        
        for wall in walls_list:
            if wall.x==self.x+x_offset and wall.y==self.y+y_offset:
                moving=False
        if moving:
            self.x+=x_offset
            self.y+=y_offset
            
        #print(self.x)

          
    def update(self):
        self.rect.x=self.x*TILESIZE   #multiply the x and y by tilesize to draw on screen
        self.rect.y=self.y*TILESIZE

#######make wall class#############

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, TILESIZE):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect=self.image.get_rect()
        self.x=x
        self.y=y
    def update(self):
        self.rect.x=self.x*TILESIZE   #multiply the x and y by tilesize to draw on screen
        self.rect.y=self.y*TILESIZE

####### make item class###########
class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, TILESIZE):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(BOOGIEGREEN)
        self.rect=self.image.get_rect()
        self.x=x
        self.y=y
    def update(self):
        self.rect.x=self.x*TILESIZE   #multiply the x and y by tilesize to draw on screen
        self.rect.y=self.y*TILESIZE
########make groups########

all_sprites_list = pygame.sprite.Group() #group for all objects
walls_list = pygame.sprite.Group() #group for all walls
item_list = pygame.sprite.Group()
item_hit_list = pygame.sprite.Group()
player=Player(2,3, TILESIZE) #create instance of Player
all_sprites_list.add(player) #add player
#create fonts
outfit = pygame.font.SysFont('Outfit-Bold.ttf', 35)

#########make wall data##############

for row, tiles in enumerate(map_data):  #enumerate returns the index value of the item
    for col, tile in enumerate(tiles):  #enumerate returns the index value of the item
        if tile=="1":
            wall=Wall(col, row, TILESIZE)  #col will be the number of the column, row the number enumerated when the 1 is found
            all_sprites_list.add(wall)
            walls_list.add(wall) #add wall to wall group
        elif tile == "2":
            item =  Item(col, row, TILESIZE)  #col will be the number of the column, row the number enumerated when the 1 is found
            all_sprites_list.add(item)
            item_list.add(item) #add wall to wall group


#########camera########

class Camera:
    def __init__(self, width, height):
        self.camera=pygame.Rect(0,0, width, height)
        self.width=width
        self.height=height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(WIDTH/2)
        y = -target.rect.y + int(HEIGHT/2)
        x=min(0,x) #stops going off on left
        y=min(0,y) #stops going off on top
       # x=max(-1024-2080,x)
        x=max(-(2080-1024),x)
        y=max(-(800-HEIGHT),y)
        
        self.camera = pygame.Rect(x, y, self.width, self.height)


camera=Camera(1,1)
            




##for x in range(0, 32):   ##makes a line of wall objects
##        wall=Wall(x, 23, TILESIZE)
##        all_sprites_list.add(wall)
##        walls_list.add(wall) #add wall to wall group
##
##wall=Wall(10,10,TILESIZE)
##all_sprites_list.add(wall)
##walls_list.add(wall) #add wall to wall group

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
# Loop as long as done == False
while not done:
 
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                player.move(-1,0, walls_list)
            if event.key==pygame.K_RIGHT:
                player.move(1,0,walls_list)
            if event.key==pygame.K_UP:
                player.move(0,-1,walls_list)
            if event.key==pygame.K_DOWN:
                player.move(0,1,walls_list)
 
    

        
    screen.fill(WHITE)
    for x in range(0, WIDTH, TILESIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT)) #draws vertical lines every TILESIZE and going as far as HEIGHT down
    for y in range(0, HEIGHT, TILESIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y)) #draws horizontal lines every TILESIZE and going across as far as WIDTH
    #player.collide_walls(walls_list)
    all_sprites_list.update()
    camera.update(player)
    #draw scoreboard and timer
    pygame.draw.rect(screen, BLUE, [850, 0, 214, 150])
    #draw the scoreboards and the title
    score_board = outfit.render("SCORE: " +  str(score),  True, GREEN)
    Timer = outfit.render("TIME " +  str(timermin ) + ":" + str(timersec),  True, GREEN)
    #highscore_board = outfit.render("HIGHSCORE: " + str(6 * 12 * 20),  True, BLUE)
    screen.blit(score_board, (855, 60))
    screen.blit(Timer, (855, 80))
    for sprite in all_sprites_list:
        screen.blit(sprite.image, camera.apply(sprite))
    #print("player position is tie " + str((player.rect.x/TILESIZE)+1))
    # See if the player block has collided with anything.
    item_hit_list = pygame.sprite.spritecollide(player, item_list, True)
    pygame.display.flip()
    # Check the list of collisions.
    timerfps += 1
    if timerfps == 60:
        timerfps = 0 
        timer -= 1
        timermin = timer // 60
        timersec = timer % 60
    if timer == 0:
        done = True
    for item in item_hit_list:
        score += 20
        pygame.mixer.init()
        pygame.mixer.music.load("Yabadabdoo.mp3")
        pygame.mixer.music.play(1,0.0)
    clock.tick(60)
 
# Be IDLE friendly
pygame.quit()
