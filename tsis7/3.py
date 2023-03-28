
import pygame

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 640
screen_height = 480

# Set colors
white = (255, 255, 255)
red = (255, 0, 0)

# Set ball properties
ball_radius = 25
ball_size = (ball_radius * 2, ball_radius * 2)
ball_pos = [screen_width//2, screen_height//2]

# Set movement speed
move_speed = 20

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Move the ball with arrow keys")

# Draw the ball on the screen
ball = pygame.Surface(ball_size)
ball.fill(red)
ball.set_colorkey(red)
pygame.draw.circle(ball, red, (ball_radius, ball_radius), ball_radius)
screen.fill(white)
screen.blit(ball, (ball_pos[0] - ball_radius, ball_pos[1] - ball_radius))

# Update the screen
pygame.display.flip()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if ball_pos[1] - move_speed >= ball_radius:
            ball_pos[1] -= move_speed
    if keys[pygame.K_DOWN]:
        if ball_pos[1] + move_speed <= screen_height - ball_radius:
            ball_pos[1] += move_speed
    if keys[pygame.K_LEFT]:
        if ball_pos[0] - move_speed >= ball_radius:
            ball_pos[0] -= move_speed
    if keys[pygame.K_RIGHT]:
        if ball_pos[0] + move_speed <= screen_width - ball_radius:
            ball_pos[0] += move_speed

    # Redraw the screen with updated ball position
    screen.fill(white)
    screen.blit(ball, (ball_pos[0] - ball_radius, ball_pos[1] - ball_radius))
    pygame.display.flip()

pygame.quit()