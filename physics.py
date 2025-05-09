from vector import Vector

def Gravity(planet1, planet2):
    """
    Calculate the gravitational force between two planets.
    """
    G = 6.67430e-11  # Gravitational constant
    distance_vector = planet2.pos - planet1.pos
    distance = distance_vector.magnitude()
    if distance == 0:
        return Vector(0, 0)  # Avoid division by zero
    force_magnitude = G * (planet1.mass * planet2.mass) / (distance ** 2)
    force_direction = distance_vector.normalize()
    return force_direction * force_magnitude