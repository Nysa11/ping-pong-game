from pygame import *
from spriteClass import GameSprite, Player
import random

''' Colors '''
background = (200, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

''' Initialize the game window and clock '''
window = display.set_mode((600, 500))
display.set_caption("Ping Pong Game")
window.fill(background)
clock = time.Clock()

''' Initialize sprites '''
platform_left = Player("img/slider.png", 50, 200, 5, 30, 100)
platform_right = Player("img/slider.png", 550, 200, 5, 30, 100)
ball = GameSprite("img/ball.png", 350, 250, 4, 30, 30)

# Ball velocity
def reset_ball_speed():
    ball.dx = random.choice([-3, 3])  # Randomly set initial horizontal direction
    ball.dy = random.choice([-3, 3])  # Randomly set initial vertical direction

reset_ball_speed()

''' Game Variables '''
game = True 
score_left = 0
score_right = 0
winning_score = 3
font.init()
font_style = font.Font(None, 50)

''' Game Loop '''
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    # Fill background each frame
    window.fill(background)

    # Display scores
    score_text_left = font_style.render(f"{score_left}", True, black)
    score_text_right = font_style.render(f"{score_right}", True, black)
    window.blit(score_text_left, (150, 20))
    window.blit(score_text_right, (450, 20))

    # Check if either player won
    if score_left >= winning_score:
        win_text = font_style.render("Left Player Wins!", True, green)
        window.blit(win_text, (180, 250))
        display.update()
        time.delay(2000)

    if score_right >= winning_score:
        win_text = font_style.render("Right Player Wins!", True, green)
        window.blit(win_text, (180, 250))
        display.update()
        time.delay(2000)

    # Update player positions
    platform_left.update_left()
    platform_right.update_right()

    # Move the ball
    ball.rect.x += ball.dx
    ball.rect.y += ball.dy

    # Check for collisions with the window edges
    if ball.rect.y <= 0 or ball.rect.y >= 500 - ball.rect.height:
        ball.dy = -ball.dy

    # Check for collisions with the sliders
    if ball.rect.colliderect(platform_left.rect) or ball.rect.colliderect(platform_right.rect):
        ball.dx = -ball.dx
        ball.dx *= 1.1
        ball.dy *= 1.1
    
    if ball.rect.x < 0:
        score_right += 1
        ball.rect.x, ball.rect.y = 350, 250
        reset_ball_speed()

    if ball.rect.x > 600:
        score_left += 1
        ball.rect.x, ball.rect.y = 350, 250 
        reset_ball_speed()

    # Draw sprites on the window
    platform_left.reset(window)
    platform_right.reset(window)
    ball.reset(window)

    display.update()
    clock.tick(60)