from pygame import *
from spriteClass import GameSprite, Player

''' Colors '''
background = (200, 255, 255)

''' Initialize the game window and clock '''
window = display.set_mode((600, 500))
window.fill(background)
clock = time.Clock()

''' Game Variables '''
game = True

# Initialize sprites
# Initialize sprites
# Initialize sprites with updated sizes for balance
platform_left = Player("img/slider.png", 20, 200, 5, 30, 100)
platform_right = Player("img/slider.png", 550, 200, 5, 30, 100)
ball = GameSprite("img/ball.png", 350, 250, 4, 30, 30)


''' Game Loop '''
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    # Fill background each frame
    window.fill(background)

    # Update player positions
    platform_left.update_left()
    platform_right.update_right()

    # Draw sprites on the window
    platform_left.reset(window)
    platform_right.reset(window)
    ball.reset(window)

    display.update()
    clock.tick(60)
