import pygame
import os

# Imports a module to allow python to interact with the
# underlying Operation system. We will use this to import the images for the game.
# youtube URL is https://www.youtube.com/watch?v=jO6qQDNa2UY
# timestamp thus far is 56.38


WIDTH, HEIGHT = 900, 500  # Sets the size of the game window.

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My 1st game")  # This will put a title in the game window.

# Set Constants
# =============
# Remember Constants are typically defined in ALL CAPS

WHITE = (255, 255, 255)  # We set the variable WHITE to be this RGB TUPLE so we can easily call it later.
BLACK = (0, 0, 0)  # Just list above we set a constant BLACK with the RGB values 0,0,0.

BORDER = pygame.Rect(WIDTH / 2 - 5, 0, 10, HEIGHT)
# Sets a rectangle in the middle of the screen with width of 10.
# We draw the rectangle in the draw_window function which is defined below.


FPS = 60  # We set this variable so we can tell python how quickly we want the game to run.
# It will be called later in the main game loop - See def main():

VEL = 5  # We set this Velocity variable equal to the speed which we want our ships to move at.

BULLET_VEL = 7  # This sets the speed of the bullets the ship will fire.
MAX_BULLETS = 3  # Sets the maximum number of bullets the player can fire at any given time.

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40  # Defines the width and height of the spaceship sprites

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))

# os.path.join makes the python script work on ALL platforms.
# As not all operating systems will use / for the path of assets/image.png

YELLOW_SPACESHIP_SCALE = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
RED_SPACESHIP_SCALE = pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
# pygame.transform.scale resizes the image to the dimensions given.
# Here we assign the transformed images to new variables

YELLOW_SPACESHIP = pygame.transform.rotate(YELLOW_SPACESHIP_SCALE, 90)
RED_SPACESHIP = pygame.transform.rotate(RED_SPACESHIP_SCALE, -90)


# pygame.transform.rotate will rotate an image around by the angle given CLOCKWISE.


def draw_window(red, yellow):
    # This function will draw all of the things in the game.
    # It will take in the arguments red and yellow which are passed to it.
    WIN.fill(WHITE)  # This will fill the display with the colour WHITE
    pygame.draw.rect(WIN, BLACK, BORDER)
    # This draws a BLACK rectangle on the WIN Surface,
    # it will be in the middle of the screen.
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    # We use BLIT when we want to draw a surface onto the screen.
    # In Python, the sprites we load are known as surfaces.
    # We state the co-ords where we want the sprite to be drawn with
    # 0,0 being TOP LEFT so X goes RIGHT and Y does DOWN
    # It's important to note that the objects are drawn IN ORDER
    # So we have to draw the sprites AFTER the white background fill.
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Because we have defined the red and yellow rectangles and passed these TO the function, we are able
    # To call on the x and ye co-ordinates that have been defined in these 2 rectangles and use them to
    # Position the spaceships to match the x,y co-ordinates of their rectangles.
    pygame.display.update()
    # This will update the display to actually draw the white screen.


def yellow_handle_movement(keys_pressed, yellow):
    # Yellow Ship Controls
    # ====================
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:
        # Check to see if the A key is pressed AND that by moving it, the sprite will not go off the screen to the left.
        yellow.x -= VEL  # Move YellowShip Left
    if keys_pressed[pygame.K_d] and yellow.x + VEL < (BORDER.x - yellow.width):
        # Check to see if the D key is pressed and that be moving it the sprite will not be greater than the x-cord of
        # the black rectangle BORDER in the middle of the screen.
        yellow.x += VEL  # Move YellowShip Right
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:
        # Check to see if the W key is pressed and that if we move the ship UP it won't go off the top of the screen.
        yellow.y -= VEL  # Move YellowShip Up
    if keys_pressed[pygame.K_s] and yellow.y + VEL < (HEIGHT - yellow.height - 15):
        # Check to see if the S key is pressed and that if we move the ship DOWN it won't go off the bottom of the
        # Screen, the Y-coordinate of which is set by the constant HEIGHT
        # Had to subtract an extra 15 pixels for some reason as the edge of the ship keeps going off!
        yellow.y += VEL  # Move YellowShip Down


def red_handle_movement(keys_pressed, red):
    # Red Ship Controls
    # =================
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > (BORDER.x + red.width):
        # Check to see if the Left Arrow key is pressed.
        red.x -= VEL  # Move RedShip Left
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL < (WIDTH - red.width):
        # Check to see if the Right Arrow key is pressed AND that the ship won't move off the screen.
        red.x += VEL  # Move RedShip Right
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:
        # Check to see if the UP Arrow key is pressed.
        # AND check that the Ship will now be moved OFF the top of the screen
        red.y -= VEL  # Move RedShip Up
    if keys_pressed[pygame.K_DOWN] and red.y + VEL < (HEIGHT - red.height - 15):
        # Check to see if the Down Arrow key is pressed.
        # AND that the ship won't be moved off the bottom of the screen
        # Had to subtract an extra 15 pixels for some reason as the edge of the ship keeps going off!
        red.y += VEL  # Move RedShip Down


def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    # Pygame uses rectangles to place borders around objects which are then used for collision detection.
    # Here we have defined 2 rectangles, one for each ship.

    red_bullets = []  # Sets up an empty list which will store information about the bullets the red ship fires.
    yellow_bullets = []  # Sets up an empty list which will store information about the bullets the yellow ship fires.

    clock = pygame.time.Clock()  # Defines a variable clock which is equal to Pygame's internal Clock.
    run = True  # Set run to True! Let's run the game :)
    while run:  # While Run is equal to TRUE we do the following...
        clock.tick(FPS)
        # A WHILE loop executes a block of code while a certain condition is true.
        # The clock.tick controls the SPEED of the while loop according to the FPS variable we set.
        # With FPS set to 60, the while loop will be forced to run 60 times per second.
        for event in pygame.event.get():
            # This will get us a list of events in pygame and loop through them.
            # We can then check what these events were and then do something with them.

            if event.type == pygame.QUIT:
                run = False
        # This checks to see if the user quit the game, if they have, run is set to FALSE and the game loop stops.

        # Check for bullets being fired
        # =============================
            if event.type == pygame.KEYDOWN:
                # This checks to see if any of the events that have happened are a key being pushed down.

                # Red Ship fires a bullet
                # =======================
                
                if event.key == pygame.K_SPACE and len(red_bullets) < MAX_BULLETS:
                    # Event.key will return the VALUE of the key that was pressed.
                    # So this checks to see if the Key that was pressed is the FORWARD SLASH Key.
                    # It also checks to see how many bullets are currently stored in the Yellow Bullet list.
                    # If the number of Bullets stored in the list is bigger than the MAX_BULLETS constant then it wont run.
                    bullet = pygame.Rect(red.x, red.y + (red.height / 2) - 2, 10, 5)
                    # This spawns a bullet which is a pygame rectangle
                    #   The rectangle will be placed in the middle of the red ship.
                    # The width will be 10 pixels & the height 5 pixels.
                    red_bullets.append(bullet)
                    # We use append to add the bullet to the red_bullets list.

                # Yellow Ship Fires a bullet
                # ==========================

                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    # Event.key will return the VALUE of the key that was pressed.
                    # So this checks to see if the Key that was pressed is the Left Control Key.
                    # It also checks to see how many bullets are currently stored in the Yellow Bullet list.
                    # If the number of Bullets stored in the list is bigger than the MAX_BULLETS constant then it wont run.
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + (yellow.height / 2) - 2, 10, 5)
                    # This spawns a bullet which is a pygame rectangle
                    # The rectangle will be placed in the middle of the yellow ship.
                    # The width will be 10 pixels & the height 5 pixels.
                    yellow_bullets.append(bullet)
                    # We use append to add the bullet to the yellow_bullets list.


         # Debugging - Bullet List Test
            print(yellow_bullets, red_bullets)  # Prints the bullet list in the console.

        # Check for ships being moved about
        # =================================
        keys_pressed = pygame.key.get_pressed()
        # This will tell us what keys are being pressed and assign it to this variable.
        # It returns a sequence of True/False values on the state of all the keys being pressed.
        # These are stored in an Array.
        # We can check to see if a particular key is being checked by looking in the array to see if the value for
        # That key is true.

        yellow_handle_movement(keys_pressed, yellow)  # Calls our function to handle the YELLOW ship
        red_handle_movement(keys_pressed, red)  # Calls our function to handle the RED ship

        draw_window(red, yellow)
        # Calls the draw window function to draw the things in the game.
        # Passes red and yellow to the draw window function.
    pygame.quit()


if __name__ == "__main__":
    main()
    # This uses the special variable __name__ to check to see if THIS file is being executed
    # or if it's been imported into another script.
    # We only want the main function to run if the user ran THIS script,
    # we do not want it to run if this script was imported into another one.
    # So this checks to see if this script was run directly and, if it was, runs the main function.
