import pygame
import random
# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
BLUE = (0, 0, 255)
FUNNY = (69, 42, 69)
CHIMBUS = (80, 0, 80)
PLIMBEY = (145, 141, 12)
BACKGROUND = (23, 255, 247)
PINKY = (230, 41, 173)
BORDER = (63, 65, 69)
colour = RED
#define some variables
x_speed = 0
playerx = 250
xball, yball = 285, 305
answer = "" 
speedtimer = 0
xoffset, yoffset = 3, 3
nonraxoffset, nonrayoffset = 3, 3
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.color = color
        self.rect = self.image.get_rect()
class Ball(pygame.sprite.Sprite):
    ball_hit_list = []
    def __init__(self, color, width, height, speed ):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.speed = speed
        self.rect = self.image.get_rect()
    def powerup(self):
        if self.powerup > 0:
            self.powerup -= 1
class player(pygame.sprite.Sprite):
    def __init__(self, color, width, height,):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
    def abilities(self, speed):
        self.speed = speed
    def powerup(self,num):
        if num > 0:
            num -= 1 
            return 2   
        else:
            return 1

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
Background = Background("cringus.png", [0,100])
# Initialize Pygame
pygame.init()
# Set the height and width of the screen
screen_width = 500
screen_height = 700
screen = pygame.display.set_mode([screen_width, screen_height])
#name the window and play the background music
pygame.display.set_caption("Project Plimble")
pygame.mixer.init()
pygame.mixer.music.load("videogame.mp3")
pygame.mixer.music.play(-1,0.0)
#Make the sprite lists
block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
for i in range(5, 11):
    powerupcolour = random.randint(1,15)
    if i == 5:
        colour = RED
    elif i == 6:
        colour =  BLUE
    elif i == 7:
        colour = BLACK
    elif i == 8:
        colour = FUNNY
    elif i == 9:
        colour = CHIMBUS
    elif i == 10:
        colour = PINKY
    for j in range(14):
        colourblock = colour
        if j == powerupcolour:
            colourblock = PLIMBEY
        # This represents a block
        block = Block(colourblock, 37, 15)
        # Set a location for the block
        block.rect.x = ((j * 39) + 10)
        block.rect.y = (i * 20)
        # Add the block to the list of objects
        block_list.add(block)
        all_sprites_list.add(block)
# Create a player block
player = player(RED, 70, 10)
player.speed = 1
all_sprites_list.add(player)
#create a ball
ball = Ball(RED, 6, 5, 1)
all_sprites_list.add(ball)
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
score = 0
while not done:
    #set Win conditions
    if len(block_list) == 0:
        done = True
        answer = "congratulation"
    #elif yball > 385:
        #done = True
        #answer = "you are awful"
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed
            if event.key == pygame.K_LEFT:
                x_speed = -5
            elif event.key == pygame.K_RIGHT:
             x_speed = 5
            # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                x_speed = 0
        if event.type == pygame.QUIT:
            done = True
    # Clear the screen
    screen.fill(BACKGROUND)
    #set the background image
    screen.blit(Background.image, Background.rect)
    #draw borders
    pygame.draw.rect(screen,BORDER, [0, 0, 10, 700 ])
    pygame.draw.rect(screen,BORDER, [490, 0, 10, 700 ])
    pygame.draw.rect(screen,BORDER, [0, 0, 500, 10 ])
    pygame.draw.rect(screen,BORDER, [0, 690, 500, 10 ])
    #stop the paddles going off the screen
    if  (player.rect.x) - 5 <= 0:
        playerx += 5
        x_speed = 0
    elif player.rect.x + 5>= 430:
        playerx -= 5 
        x_speed = 0
    #Make the paddle and the ball move
    playerx += (x_speed * player.speed)
    player.rect.x = playerx
    player.rect.y = 600
    xball -= xoffset 
    yball -= yoffset 
    ball.rect.x = xball
    ball.rect.y = yball
    #make the ball bounce off the screen
    if xball < 10 or xball >= 480:
        xoffset = xoffset * -1
    if yball < 10 or yball >= 670:
        yoffset = yoffset * -1
    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(ball, block_list, True)
    #Make ball bounce of padde(change this to spritecollide)
    if ((ball.rect.y > (player.rect.y - 10)) and (ball.rect.y < (player.rect.y + 10))) and ((ball.rect.x > player.rect.x - 10) and (ball.rect.x < player.rect.x + 70)):
        if x_speed == -5:
             xoffset = xoffset * -1
        yoffset = yoffset * -1 
        yball -= yoffset + random.randint(1, 3)
    # Check the list of collisions.
    #Make Powerups
    if len(blocks_hit_list) > 0:
        yoffset = yoffset * -1 
        if blocks_hit_list[0].color == PLIMBEY:
            player.abilities(player.powerup(200))
            speedtimer = 200
    else:
        speedtimer -= 1
    if speedtimer == 0:
        player.abilities(1)
    #add a scoreboard
    for block in blocks_hit_list:
        score += 1
    # Draw all the spites
    all_sprites_list.draw(screen)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # Limit to 60 frames per second
    clock.tick(60)
#display the outcome
print(answer)
pygame.quit()