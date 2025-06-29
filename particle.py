
import numpy as np
import pygame

class Particle:
    def __init__(self, position, velocity, radius, mass, color):
        self.position = position
        self.velocity = velocity
        self.radius = radius
        self.mass = mass
        self.color = color

    def move(self):
        self.position += self.velocity

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position.astype(int), self.radius)

    def wall_collision(self, width, height):
        if self.position[0] - self.radius <= 0 or self.position[0] + self.radius >= width:
            self.velocity[0] *= -1
        if self.position[1] - self.radius <= 0 or self.position[1] + self.radius >= height:
            self.velocity[1] *= -1

    def check_collision(self, other):
        delta = other.position - self.position
        distance = np.linalg.norm(delta)
        min_dist = self.radius + other.radius

        if distance < min_dist:
            # Normalize delta vector
            normal = delta / distance if distance != 0 else np.array([1.0, 0.0])
            
            # Resolve overlap
            overlap = min_dist - distance
            self.position -= normal * (overlap / 2)
            other.position += normal * (overlap / 2)

            # Relative velocity
            rel_vel = self.velocity - other.velocity
            vel_along_normal = np.dot(rel_vel, normal)

            # Skip if moving apart
            if vel_along_normal > 0:
                return

            # Apply impulse (elastic collision)
            impulse = (2 * vel_along_normal) / (self.mass + other.mass)
            self.velocity -= impulse * other.mass * normal
            other.velocity += impulse * self.mass * normal

