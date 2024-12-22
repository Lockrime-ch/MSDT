import random
class MyMap:
    def __init__(self, biomes, wight=5, height=5, s="-", average_plast=10):
        self.wight = wight
        self.height = height
        self.biomes = biomes
        self._1()
        self.s = s
        for i in range(average_plast):
            self._2()
        for i in range(4):
            self._4()

    def _1(self):
        a = self.biomes
        self.map = []
        counter = 0

        for i in range((self.wight * self.height) - len(a)):
            a.append(0)
        random.shuffle(a)
        b = a
        for i in range(self.wight):
            a = []
            for j in range(self.height):
                a.append(b[counter])
                counter += 1
            self.map.append(a)

    def _2(self):
        for i in range(self.wight):
            for j in range(self.height):
                a1 = self.map[i][j]
                if a1 != 0:
                    if self.map[i][j - 1] == 0 and j != 0:
                        a1_1 = a1[1]
                        a1_2 = a1[2]
                        b = []
                        for k in range(a1_1):
                            b.append(0)
                        for k in range(a1_2):
                            b.append(a1)
                        try:
                            self.map[i][j - 1] = random.choice(b)
                        except IndexError:
                            pass
                        try:
                            self.map[i][j + 1] = random.choice(b)
                        except IndexError:
                            pass
        self.map2 = []
        for i in range(self.height):
            b = []
            for j in self.map:
                b.append(j[i])
            self.map2.append(b)
        self.map = self.map2

    def _3(self):
        a = self.s
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                if self.map[i][j] == 0:
                    self.map[i][j] = a
                elif self.map[i][j] == a:
                    self.map[i][j] = 0

    def print_me(self):
        self._3()
        for i in self.map:
            b = []
            for j in i:
                b.append(j[0])
            for k in b:
                print(str(k), end="")
                print("\033[37m {}".format(""), end="")
            print()
        self._3()

    def returner(self):
        a = []
        for i in self.map:
            b = []
            for j in i:
                if j != 0:
                    b.append(j[0][-1])
                else:
                    b.append("0")
            a.append(b)
        return a

    def _4(self):
        for i in range(self.wight):
            for j in range(self.height):
                a1 = self.map[i][j]
                if a1 != 0:
                    if self.map[i][j - 1] == 0 and j != 0:

                        try:
                            self.map[i][j - 1] = a1
                        except IndexError:
                            pass
                        try:
                            self.map[i][j + 1] = a1
                        except IndexError:
                            pass
        self.map2 = []
        for i in range(self.height):
            b = []
            for j in self.map:
                b.append(j[i])
            self.map2.append(b)
        self.map = self.map2
if __name__ == "__main__":
    biomes = [("\033[31m{}".format("1"), 3, 2),
             ("\033[32m{}".format("2"), 3, 2),
             ("\033[36m{}".format("3"), 3, 2),
             ("\033[34m{}".format("4"), 3, 2),
             ("\033[35m{}".format("5"), 3, 2)]

    biomes1 = []
    for i in range(300):
        biomes1.append(random.choice(biomes))
    ex = MyMap(biomes1, 1000, 1000, ".", 50)
    ex.print_me()
    # for i in ex.returner():
    #     print(i)
