class Camera:
    def __init__(self, x=0, y=0, blocked=False):
        self.x = x
        self.y = y
        self.blocked = blocked

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

    def block(self):
        self.blocked = True

    def unblock(self):
        self.blocked = False

    def get_block(self):
        return self.blocked


cam = Camera()
