import random


def enemy_1(self, target, ai_dict):
    if self.distanceTo(target) <= 200:
        self.move((target.x - self.x) / self.distance_to(target),
                  (target.y - self.y) / self.distance_to(target))
    return {}


def enemy_2(self, target, ai_dict):
    if self.distance_to(target) <= 200:
        self.move((target.x - self.x) / (self.distanceTo(target) + 1),
                  (target.y - self.y) / (self.distanceTo(target) + 1))
    else:
        if "idletarget" in ai_dict.keys():
            if random.random() > 0.3:
                self.move(*ai_dict["idletarget"])
        if random.random() > 0.9:
            t = ((0.5 - random.random()), (0.5 - random.random()))
            return {"idletarget": t}
    return {}
