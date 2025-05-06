import pygame

class Planet:
    def __init__(self, name, mass, radius, coord, velocity, color):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.coord = coord  # Expected as a tuple (x, y)
        self.velocity = velocity  # Expected as a tuple (vx, vy)
        self.color = color

    def __repr__(self):
        return (f"Planet(name={self.name}, mass={self.mass}, "
                f"coord={self.coord}, velocity={self.velocity}, color={self.color})")

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.coord, self.radius)

    def getCoord(self):
        return self.coord

    def setCoord(self, new_coord):
        self.coord = new_coord

    # def update_position(self, dt):
    #     # Update the planet's position based on its velocity and time delta
    #     x, y = self.coord
    #     vx, vy = self.velocity
    #     x += vx * dt
    #     y += vy * dt
    #     self.coord = (x, y)