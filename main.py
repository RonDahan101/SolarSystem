import pygame
import sys
from planet import Planet
from colors import *
from vector import Vector
from constants import solar_system_bodies

# Initialize pygame
pygame.init()

# Set up the display
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((WIDTH - 100, HEIGHT- 100))
pygame.display.set_caption("Solar System")

# Clock for controlling frame rate
clock = pygame.time.Clock()

def initilizePlanet():
    # Create a planet instance
    planets_name = ["Earth", "Sun"]
    planets = []
    for name in planets_name:
        planets.append(Planet(
            name,
            solar_system_bodies[name]["mass"],
            solar_system_bodies[name]["radius"],
            Vector(solar_system_bodies[name]["distance"], 0),
            Vector(0, solar_system_bodies[name]["velocity"]),
            solar_system_bodies[name]["color"]
        ))
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
            # planet.update(planets, 60000)

        # Update display
        pygame.display.flip()

        # Cap frame rate
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
