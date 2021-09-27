class EmitterShapes(Enum):
    CIRCLE = 1
    CONE = 2
    POINT = 3
    CROSS = 4
    X = 5
    SNOWFLAKE = 6

# A particle has  -  speed, life, color, transparency, size

class EmitterBase():
    def __init__(self, x, y, eR, eS, particleBase):
        self.particles = []
        
        self.x = x
        self.y = y
        self.emissionRate = eR
        self.emissionShape = eS
        
        self.particleBase = particleBase