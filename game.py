import pyxel
import random


class tetromino_o:  # Carré jaune
    def __init__(self):
        self.pos = [4, 0]
        self.color = 10
        self.shape = [[1, 1], [1, 1]]
        self.deg = 0
        self.stuck = False

    def rotate(self):
        pass

    def affichage(self):
        # Ajouter la pièce au centre de la matrice du jeu (sur la ligne 0)
        for i in range(2):
            for j in range(2):
                self.matrice[j][i+4] = self.shape[j][i]


class tetromino_i:  # barre bleu
    def __init__(self):
        self.pos = [3, 0]
        self.color = 12
        self.shape = [[1], [1], [1], [1]]
        self.deg = 0
        self.stuck = False


class tetromino_s:  # s rouge
    def __init__(self):
        self.pos = [3, 0]
        self.color = 8
        self.shape = [[0, 1, 1], [1, 1, 0]]
        self.deg = 0
        self.stuck = False


class tetromino_z:  # z vert
    def __init__(self):
        self.pos = [3, 0]
        self.color = 11
        self.shape = [[1, 1, 0], [0, 1, 1]]
        self.deg = 0
        self.stuck = False


class tetromino_l:  # l orange
    def __init__(self):
        self.pos = [3, 0]
        self.color = 9
        self.shape = [[1, 0], [1, 0], [1, 1]]
        self.deg = 0
        self.stuck = False


class tetromino_j:  # j rose
    def __init__(self):
        self.pos = [3, 0]
        self.color = 14
        self.shape = [[0, 1], [0, 1], [1, 1]]
        self.deg = 0
        self.stuck = False


class tetromino_t:  # t violet
    def __init__(self):
        self.pos = [3, 0]
        self.color = 2
        self.shape = [[1, 1, 1], [0, 1, 0]]
        self.deg = 0
        self.stuck = False

# Create an App class


class App:
    def __init__(self):
        # Initialize Pyxel window
        pyxel.init(width=200, height=200, title="T'ES TRISTE", fps=120)

        # Enable mouse
        pyxel.mouse(True)

        # matrice de 10*22
        self.matrice = [[0 for i in range(10)] for j in range(22)]
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(1)
        # affichage de la matrice de jeu 0 en noir 1 en jaune, 2 en bleu, 3 en rouge, 4 en vert, 5 en orange, 6 en rose, 7 en violet
        for i in range(10):
            for j in range(22):
                if self.matrice[j][i] == 0:
                    pyxel.rect(i*10+50, j*10, 10, 10, 0)
                elif self.matrice[j][i] == 1:
                    pyxel.rect(i*10+50, j*10, 10, 10, 10)
                elif self.matrice[j][i] == 2:
                    pyxel.rect(i*10+50, j*10, 10, 10, 12)
                elif self.matrice[j][i] == 3:
                    pyxel.rect(i*10+50, j*10, 10, 10, 8)
                elif self.matrice[j][i] == 4:
                    pyxel.rect(i*10+50, j*10, 10, 10, 11)
                elif self.matrice[j][i] == 5:
                    pyxel.rect(i*10+50, j*10, 10, 10, 9)
                elif self.matrice[j][i] == 6:
                    pyxel.rect(i*10+50, j*10, 10, 10, 14)
                elif self.matrice[j][i] == 7:
                    pyxel.rect(i*10+50, j*10, 10, 10, 2)
        # afficher le triomino en cours
        Trio = tetromino_o()
        Trio.affichage()
