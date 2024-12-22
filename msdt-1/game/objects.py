import pygame
import camera
import ai_types
import map


class BaseObject(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.Surface((50, 50))
        self.image.fill("GREEN")
        self.rect = self.image.get_rect()
        self.rect.center = (self.x - camera.cam.get_x() + width // 2, self.y - camera.cam.get_y() + height // 2)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_cord(self):
        return self.x, self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_cord(self, x, y):
        self.x = x
        self.y = y

    def distanceTo(self, other):
        return ((self.get_x() - other.get_x()) ** 2 +
                (self.get_y() - other.get_y()) ** 2) ** 0.5

    def update(self):
        self.rect.center = (self.x - camera.cam.get_x() + width // 2, self.y -
                            camera.cam.get_y() + height // 2)


class Player(BaseObject):
    def __init__(self, x, y, speed=5):
        super().__init__(x, y)
        self.speed = speed

    def update(self):
        if not camera.cam.get_block():
            camera.cam.set_cord(*self.get_cord())
        super().update()

    def getSpeed(self):
        return self.speed

    def setSpeed(self, speed):
        self.speed = speed

    def move(self, x, y):
        self.set_cord(self.x + x * self.speed, self.y + y * self.speed)
        """collist = pygame.sprite.spritecollideany(self, all_sprites)
                if pygame.sprite.spritecollideany(self, all_sprites):
                    self.set_cord(self.x - x * self.speed, self.y - y * self.speed)"""


class StaticObject(BaseObject):
    def __init__(self, x, y):
        super().__init__(x, y)


class GroundItem(BaseObject):
    def __init__(self, x, y, type):
        super().__init__(x, y)


class Creature(BaseObject):
    def __init__(self, x, y, ai, speed=3):
        super().__init__(x, y)
        self.ai = ai
        self.ai_dict = {}
        self.speed = speed

    def move(self, x, y):
        self.set_cord(self.x + x * self.speed, self.y + y * self.speed)

    def update(self):
        d = self.ai(self, player, self.ai_dict)
        for i in d.keys():
            self.ai_dict[i] = d[i]
        super().update()


if __name__ == '__main__':
    pygame.init()

    # pygame.display.set_mode((1000, 1000), pygame.RESIZABLE)
    # pygame.display.set_caption("Проект 2.0")
    # pygame.display.set_icon(pygame.image.load("C:/Users/user/PycharmProjects/2.0/pictures/app_icon.bmp"))

    all_sprites = pygame.sprite.Group()
    size = (width, height) = 1024, 512
    screen = pygame.display.set_mode(size)
    running = True
    clock = pygame.time.Clock()
    MOVE_TIMER = pygame.USEREVENT
    pygame.time.set_timer(MOVE_TIMER, 1000 // 50)
    bioms = [("\033[31m{}".format("1"), 3, 2),
             ("\033[32m{}".format("2"), 3, 2),
             ("\033[36m{}".format("3"), 3, 2),
             ("\033[34m{}".format("4"), 3, 2),
             ("\033[35m{}".format("5"), 3, 2)]
    biom_col = {"0": "BLACK", "1": "DARKGREEN", "2": "ORANGE",
                "3": "CHOCOLATE", "4": "PURPLE", "5": "AZURE"}
    mapp = map.MyMap(bioms, 100, 100, ".", 50).reterner()
    print(*mapp)
    for i in range(len(mapp)):
        for j in range(len(mapp)):
            c = biom_col[mapp[i][j]]
            mapp[i][j] = BaseObject((len(mapp) // 2 - i) * 50, (len(mapp) - j) * 50)
            mapp[i][j].image.fill(c)
            all_sprites.add(mapp[i][j])

    player = Player(100, 100)
    square = StaticObject(300, 100)
    square.image.fill('YELLOW')
    bad_guy = Creature(100, 200, ai_types.enemy_2)
    bad_guy.image.fill('RED')
    all_sprites.add(square)
    all_sprites.add(bad_guy)
    all_sprites.add(player)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == MOVE_TIMER:
                movex, movey = 0, 0
                if pygame.key.get_pressed()[pygame.K_UP]:
                    movey -= 1
                if pygame.key.get_pressed()[pygame.K_DOWN]:
                    movey += 1
                if pygame.key.get_pressed()[pygame.K_LEFT]:
                    movex -= 1
                if pygame.key.get_pressed()[pygame.K_RIGHT]:
                    movex += 1
                player.move(movex, movey)
        all_sprites.update()
        screen.fill(pygame.Color('black'))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
