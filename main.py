import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System")

# Define colors
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Initial circle position
x, y = WIDTH // 2, HEIGHT // 2
radius = 50
speed = 5

def main():
    global x, y
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get pressed keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= speed
        if keys[pygame.K_RIGHT]:
            x += speed
        if keys[pygame.K_UP]:
            y -= speed
        if keys[pygame.K_DOWN]:
            y += speed

        # Clear screen
        screen.fill(WHITE)

        # Draw circle at current position
        pygame.draw.circle(screen, BLUE, (x, y), radius)

        # Update display
        pygame.display.flip()

        # Cap frame rate
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
