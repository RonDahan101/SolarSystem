import pygame

from physics import Gravity
from vector import Vector

class Planet:
    def __init__(self, name, mass, radius, pos, velocity, color):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.pos = pos  # Expected as a tuple (x, y)
        self.velocity = velocity  # Expected as a tuple (vx, vy)
        self.color = color

    def __repr__(self):
        return (f"Planet(name={self.name}, mass={self.mass}, "
                f"pos={self.pos}, velocity={self.velocity}, color={self.color})")

    def draw(self, surface):
        info = pygame.display.Info()
        WIDTH, HEIGHT = info.current_w, info.current_h
        new_pos = self.pos * 0.000000005 + Vector((WIDTH - 100) // 2, (HEIGHT // 2))
        pygame.draw.circle(surface, self.color, (new_pos.x, new_pos.y), self.radius * 0 + 10)

    def getPos(self):
        return self.pos

    def setPos(self, new_pos):
        self.pos = new_pos

    def update(self, planets, dt):
        # Calculate gravitational forces and update velocity
        force = Vector(0, 0)
        for planet in planets:
            force += Gravity(self, planet)
        # Update velocity based on the force and mass
        acceleration = force / self.mass
        self.velocity += acceleration * dt
        # Update the planet's position based on its velocity and time delta
        self.pos += self.velocity * dt