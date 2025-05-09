import pygame

solar_system_bodies = {
    "Sun": {
        "mass": 1.9885e30,
        "radius": 6.9634e8,
        "velocity": 0,
        "distance": 0,
        "color": pygame.Color("yellow")
    },
    "Mercury": {
        "mass": 3.3011e23,
        "radius": 2.4397e6,
        "velocity": 4.79e4,
        "distance": 5.791e10,
        "color": pygame.Color(169, 169, 169)  # Dark Gray
    },
    "Venus": {
        "mass": 4.8675e24,
        "radius": 6.0518e6,
        "velocity": 3.5e4,
        "distance": 1.082e11,
        "color": pygame.Color(218, 165, 32)  # Goldenrod
    },
    "Earth": {
        "mass": 5.97237e24,
        "radius": 6.371e6,
        "velocity": 2.978e4,
        "distance": 1.496e11,
        "color": pygame.Color("blue")
    },
    "Moon": {
        "mass": 7.342e22,
        "radius": 1.7371e6,
        "velocity": 1.022e3,
        "distance": 3.844e8,  # from Earth
        "color": pygame.Color(211, 211, 211)  # Light Gray
    },
    "Mars": {
        "mass": 6.4171e23,
        "radius": 3.3895e6,
        "velocity": 2.41e4,
        "distance": 2.279e11,
        "color": pygame.Color("red")
    },
    "Jupiter": {
        "mass": 1.8982e27,
        "radius": 6.9911e7,
        "velocity": 1.31e4,
        "distance": 7.785e11,
        "color": pygame.Color(210, 180, 140)  # Tan
    },
    "Saturn": {
        "mass": 5.6834e26,
        "radius": 5.8232e7,
        "velocity": 9.7e3,
        "distance": 1.433e12,
        "color": pygame.Color(255, 228, 181)  # Moccasin
    },
    "Uranus": {
        "mass": 8.6810e25,
        "radius": 2.5362e7,
        "velocity": 6.8e3,
        "distance": 2.877e12,
        "color": pygame.Color(173, 216, 230)  # Light Blue
    },
    "Neptune": {
        "mass": 1.02413e26,
        "radius": 2.4622e7,
        "velocity": 5.4e3,
        "distance": 4.503e12,
        "color": pygame.Color(25, 25, 112)  # Midnight Blue
    }
}
