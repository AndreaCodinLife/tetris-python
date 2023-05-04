import pyxel
import random

class App:
    def __init__(self):
        pyxel.init(160, 120, title="Tetris Background")
        pyxel.load("tetris.pyxres")
        self.blocks = []
        for i in range(10):
            x = random.randint(0, 160)
            y = random.randint(0, 120)
            self.blocks.append([random.randint(0, 8), x, y])
        pyxel.run(self.update, self.draw)

    def update(self):
        for block in self.blocks:
            block[2] += 1
            if block[2] > 120:
                block[2] = 0
                block[1] = random.randint(0, 152)
            block[2] = block[2] % 120  # wrap around the y-coordinate


    def draw(self):
        pyxel.cls(0)
        for block in self.blocks:
            pyxel.blt(block[1], block[2], 0, block[0] * 8, 0, 8, 8, 0)

App()
