import random
import pygame
#deport Seth
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#define some variables
y, y2 = 175, 175
yball = 20
yoffset, xoffset, = 3, 3
y_speed, y2_speed, x_speed = 0, 0, 0
xball = random.random() * 500
plint = 0
x = 0
pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Obb")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
pygame.mixer.init()
pygame.mixer.music.load("shakira.mp3")
pygame.mixer.music.play(-1,0.0)
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    
    # --- Game logic should go here

    #Game win or lose
    if xball <= 10 and (yball >= y - 10 and yball <= y + 200 ) or (xball >= 670 and (yball >= y2 - 10 and yball <= y2 + 200 )):
        xoffset = xoffset * -1
    elif xball <= 0:
        done = True
        answer = "You Lose"
    elif xball >= 685:
        done = True 
        answer = "you win"
    #stop the paddles going off the screen
    if y <= 0:
        y += 5
    elif y >= 300:
        y -= 5  
    if y2 <= 0:
        y2 += 5
    elif y2 >= 300:
        y2 -= 5
    # User pressed down on a key
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
             x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
        
    # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
        if event.type == pygame.QUIT:
            done = True
    # User 2 pressed down on a key
        elif event.type == pygame.KEYDOWN:
        # Figure out if it was an wasd key. If so
        # adjust speed.
            if event.key == pygame.K_w:
                y2_speed = -3
            elif event.key == pygame.K_s:
                y2_speed = 3
 
    # User 2 let up on a key
        elif event.type == pygame.KEYUP:
        # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_w or event.key == pygame.K_s:
                y2_speed = 0
    #Ai code for the second paddle
    
    # --- Screen-clearing code goes here
    # Move the objects according to the speed vector.
    y += y_speed
    y2 += y2_speed
    xball += xoffset
    yball += yoffset
    if xball < 0 or xball >= 685:
        xoffset = xoffset * -1
    if yball < 0 or yball >= 485:
        yoffset = yoffset * -1
    yoffset += 0.01
    xoffset += 0.01
    
    # Here, we clear the screen to white. Don't put other drawing commandsw
    # above this, or they will be erased with this command.
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    pygame.draw.rect(screen, WHITE, [x, y, 10, 200 ])
    pygame.draw.rect(screen, WHITE, [690, y2, 700, 200 ])
    pygame.draw.line(screen, WHITE, [350,0], [350, 500], 6)
    pygame.draw.ellipse(screen, RED, [xball,yball,25,25], 0)
    # --- Go ahead and update the screen with what we've drawn.
    
    pygame.display.flip()
    
    # --- Limit to 60 frames per second
    clock.tick(60)
print(answer, "没有共产党就没有新中国 没有共产党就没有新中国 共产党辛劳为民族 共产党他一心救中国他指给了人民解放的道路 他领导中国走向光明 他坚持了抗战八年多 他改善了人民生活 他建设了敌后根据地 他实行了民主好处多 没有共产党就没有新中国 没有共产党就没有新中国")
# Close the window and quit.
pygame.quit()
