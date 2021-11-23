import pygame
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BROWN = (150, 75, 00)
YELLOW = (255, 255, 00)
pygame.init()
x = 0
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
xoffset = 5
yoffset = 5
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLUE)
 
    # --- Drawing code should go here
    x -= xoffset
    if x < 0 or x > 550:
        xoffset = xoffset * -1

    pygame.draw.rect(screen, GREEN, [0, 400, 700, 200 ])
    pygame.draw.rect(screen,  BROWN, [150, 200, 400, 400], 0)
    pygame.draw.rect(screen, YELLOW, [215, 325, 275, 400])
    pygame.draw.ellipse(screen, YELLOW, [x,20,150,100], 0)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
# Close the window and quit.
pygame.quit()