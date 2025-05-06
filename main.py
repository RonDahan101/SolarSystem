import pygame
import sys
from planet import Planet
from colors import *

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System")

# Clock for controlling frame rate
clock = pygame.time.Clock()

def initilizePlanet():
    # Create a planet instance
    planets = []
    earth = Planet("Earth", 5.972e24, 10, (WIDTH // 2, HEIGHT // 2), (0, 0), GREEN)
    planets.append(earth)
    return planets

def main():
    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill(WHITE)
    pygame.draw.circle(background, RED, (100, 100), 10)
    planets = initilizePlanet()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen
        screen.blit(background, (0, 0))

        for planet in planets:
            planet.draw(screen)
            planet.setCoord((planet.getCoord()[0] + 1, planet.getCoord()[1] + 1))

        # Update display
        pygame.display.flip()

        # Cap frame rate
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
