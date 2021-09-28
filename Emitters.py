import pygame
from pygame.locals import *

from main import *

class EmitterShapes(Enum):
    CIRCLE = 1
    CONE = 2
    POINT = 3
    CROSS = 4
    X = 5
    SNOWFLAKE = 6

# A particle has  -  position, vector... speed, life, color, transparency, size
class ParticleBase():
    def __init__(self, speed, life, color, startTransparency, size):
        self.speed = speed
        self.life = life
        self.color = color
        self.startTransparency = startTransparency
        self.size = size

    def getAttributes(self):
        return self.speed, self.life, self.color, self.startTransparency, self.size

class Particle():
    def __init__(self, position, vector, particleBase):
        self.position = position
        self.vector = vector
        self.speed, self.life, self.color, self.startTransparency, self.size = particleBase.getAttributes()

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.position), self.size)

class EmitterBase():
    def __init__(self, x, y, eR, particleBase, eS):
        self.particles = []
        
        self.x = x
        self.y = y
        self.emissionRate = eR
        
        self.particleBase = particleBase

        self.emissionShape = eS

    def emitParticle(self, vector):
        particle = Particle([self.x, self.y], vector, self.particleBase)
        
        self.particles.append(particle)

    def update(self):
        for particle in self.particles:
            particle.update()

    def draw(self,screen):
        for particle in self.particles:
            particle.draw(screen)

class PointEmitter(EmitterBase):
    def emit(self):
        pass