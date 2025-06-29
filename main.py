
import pygame
import sys
import numpy as np
from particle import Particle
import random

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Particle Collision Simulator")
clock = pygame.time.Clock()

# Colors
BACKGROUND_COLOR = (0, 0, 0)

# Create particles
particles = []
for _ in range(20):
    radius = random.randint(10, 20)
    mass = radius * 2
    x = random.uniform(radius, WIDTH - radius)
    y = random.uniform(radius, HEIGHT - radius)
    vx = random.uniform(-2, 2)
    vy = random.uniform(-2, 2)
    color = tuple(random.randint(100, 255) for _ in range(3))
    particles.append(Particle(np.array([x, y]), np.array([vx, vy]), radius, mass, color))

# Main loop
running = True
while running:
    clock.tick(60)
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i, p1 in enumerate(particles):
        p1.move()
        p1.wall_collision(WIDTH, HEIGHT)
        for p2 in particles[i + 1:]:
            p1.check_collision(p2)
        p1.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
