import pygame

WIDTH, HEIGHT = (25, 30)
BLOCK_SIZE = 15
INITIAL = [
    (WIDTH // 2, HEIGHT // 2),
    (WIDTH // 2 - 1, HEIGHT // 2),
    (WIDTH // 2 - 2, HEIGHT // 2),
]

pygame.init()
screen = pygame.display.set_mode((WIDTH * BLOCK_SIZE, HEIGHT * BLOCK_SIZE))
clock = pygame.time.Clock()
running = True
snake = INITIAL

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    # Draw the board
    for x in range(0, WIDTH * BLOCK_SIZE, BLOCK_SIZE):
        for y in range(0, HEIGHT * BLOCK_SIZE, BLOCK_SIZE):
            is_light = bool((x // BLOCK_SIZE + y // BLOCK_SIZE) % 2)
            color = "#9CCC65" if is_light else "#66BB6A"
            pygame.draw.rect(screen, color, (x, y, BLOCK_SIZE, BLOCK_SIZE))

    for seg in snake:
        for x, y in snake:
            pygame.draw.rect(screen, "red", (x, y, BLOCK_SIZE, BLOCK_SIZE))

    snake = snake[1:] + [(snake[-1][0] + 1, snake[-1][1])]

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
