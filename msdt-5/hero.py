class Hero:
    def __init__(self, name, max_health):
        if max_health <= 0:
            raise ValueError('A hero must have at least 1 max health point')
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.dead = False

    def get_health(self):
        return self.health

    def heal(self, value):
        if value <= 0:
            raise ValueError('Cannot heal a hero for a non-positive amount')
        if self.dead:
            raise RuntimeError('Cannot heal a dead hero')
        self.health += value
        if self.health > self.max_health:
            self.health = self.max_health
        return self.get_health()

    def damage(self, value):
        if value <= 0:
            raise ValueError('Cannot damage a hero for a non-positive amount')
        if self.dead:
            raise RuntimeError('Cannot damage a dead hero')
        self.health -= value
        if self.health <= 0:
            self.dead = True
        return self.health

    def revive(self):
        if not self.dead:
            raise RuntimeError('Cannot revive a living hero')
        self.dead = False
        self.health = 1
