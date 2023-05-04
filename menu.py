import pyxel
import main
import pygame
import random

global matrice  # Matrice du jeu
matrice = [[0 for i in range(10)] for j in range(22)]  # Matrice du jeu
##################################### Classes Tetrominos #########################################
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
                global matrice
                matrice[j][i+4] = self.shape[j][i]


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

##################################### FIN CLASSE TETROMINOS #########################################


###################### CLASSE DU JEU ######################
class App:
    def __init__(self):
        self.start = False
        pyxel.init(200, 200, title="T'ES TRISTE", fps=60)
        self.menu_items = ["Play", "Help", "Quit"]
        self.selected_item = 0 
        self.menu_color = 7 # white
        self.selected_color = 2 # violet
        self.button_height = 32 
        self.button_width = 70
        #Blocs de tetris qui tombent en arrière plan
        pyxel.load("tetris.pyxres")
        self.blocks = []
        for i in range(30):
            # x random number between 0 and 160 without the numbers between 60 and 100
            x1 = random.randint(5,45)
            x2 = random.randint(140, 190)
            #the first is x1 next is x2 then its x1 again and so on 
            if i % 2 == 0:
                x = x1
            else:
                x = x2
            y = random.randint(0, 190)
            self.blocks.append([random.randint(0, 8), x, y+random.randint(0, 100)])
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.start == False:
            ############################### MENU ##################################
            for block in self.blocks:
                block[2] += 0.5
                if block[2] > 190:
                    #removes the block from the list and adds a new one
                    self.blocks.remove(block)
                    x1 = random.randint(5,65)
                    x2 = random.randint(140, 190)
                    x = random.choice([x1, x2])
                    y = 0
                    self.blocks.append([random.randint(0, 8), x, y])
                block[2] = block[2] % 190  
            if pyxel.btnp(pyxel.KEY_DOWN):
                #play sound effect when pressing down
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('select.wav'))
                self.selected_item = (self.selected_item + 1) % len(self.menu_items)
            elif pyxel.btnp(pyxel.KEY_UP):
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('select.wav'))
                self.selected_item = (self.selected_item - 1) % len(self.menu_items)

            if pyxel.btnp(pyxel.KEY_SPACE):
                if self.menu_items[self.selected_item] == "Play":
                    #On lance le jeu ici
                    print("Bouton Play cliqué")
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound('levelstrt.wav'))
                    pygame.time.delay(1000)
                    pygame.mixer.Channel(0).play(pygame.mixer.Sound('main_theme.mp3'))
                    self.start = True
                    print("Le jeu est lancé")
                elif self.menu_items[self.selected_item] == "Help":
                    print("Bouton Help cliqué")
                elif self.menu_items[self.selected_item] == "Quit":
                    pyxel.quit()
            ############################### FIN MENU ##################################
        elif self.start == True:
            ############################### JEU #########################################
            pass
            ############################### FIN JEU #########################################
            

    def draw(self):
        if self.start == False:
        ############################### MENU #########################################
            pyxel.cls(0)
            for block in self.blocks:
                pyxel.blt(block[1], block[2], 0, block[0] * 8, 0, 8, 8, 0)
            #black rectangle in the middle of the screen to write the title
            pyxel.rect(50, 0, 60, 200, 0)
            #write title
            pyxel.text(85, 20, "Tetris", 1)
            #write ACA Studios in the bottom right corner
            pyxel.text(150, 190, "ACA Studios", 1)
            #write the version number in the bottom left corner
            pyxel.text(10, 190, "v0.1.5", 1)
            for i, item in enumerate(self.menu_items):
                color = self.menu_color
                if i == self.selected_item:
                    color = self.selected_color
                pyxel.rectb(65, 50 + i*self.button_height, self.button_width, self.button_height, color)
                pyxel.text(90, 63 + i*self.button_height, item, 11)
        ############################### FIN MENU #########################################
        elif self.start == True:
            ############################### JEU #########################################
            pyxel.cls(1)
        # affichage de la matrice de jeu 0 en noir 1 en jaune, 2 en bleu, 3 en rouge, 4 en vert, 5 en orange, 6 en rose, 7 en violet
            for i in range(10):
                for j in range(22):
                    global matrice
                    if matrice[j][i] == 0:
                        pyxel.rect(i*10+50, j*10, 10, 10, 0)
                    elif matrice[j][i] == 1:
                        pyxel.rect(i*10+50, j*10, 10, 10, 10)
                    elif matrice[j][i] == 2:
                        pyxel.rect(i*10+50, j*10, 10, 10, 12)
                    elif matrice[j][i] == 3:
                        pyxel.rect(i*10+50, j*10, 10, 10, 8)
                    elif matrice[j][i] == 4:
                        pyxel.rect(i*10+50, j*10, 10, 10, 11)
                    elif matrice[j][i] == 5:
                        pyxel.rect(i*10+50, j*10, 10, 10, 9)
                    elif matrice[j][i] == 6:
                        pyxel.rect(i*10+50, j*10, 10, 10, 14)
                    elif matrice[j][i] == 7:
                        pyxel.rect(i*10+50, j*10, 10, 10, 2)
            # afficher le triomino en cours
            Trio = tetromino_o()
            Trio.affichage()
            print(matrice)
            ############################### FIN JEU #########################################
        

pygame.mixer.init()
pygame.mixer.Channel(0).play(pygame.mixer.Sound('main_theme.mp3'), -1)
App()