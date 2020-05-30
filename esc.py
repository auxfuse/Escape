import constants

# Variables
player_x = 600
player_y = 350


# Creating starfield background in PGZ
def draw():
    screen.blit(images.backdrop, (0, 0))
    screen.blit(images.mars, (50, 50))
    screen.blit(images.astronaut, (player_x, player_y))
    screen.blit(images.ship, (550, 300))


# Game loop
def game_loop():
    global player_x, player_y
    if keyboard.right:
        player_x += 5
    elif keyboard.left:
        player_x -= 5
    if keyboard.up:
        player_y -= 10
    elif keyboard.down:
        player_y += 10

clock.schedule_interval(game_loop, 0.03)