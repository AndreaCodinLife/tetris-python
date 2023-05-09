import pyxel
#import main
import pygame
import random

matrice = [[0 for i in range(10)] for j in range(22)]  # Matrice du jeu
##################################### Classes Tetrominos #########################################
class tetromino_o:  # Carré jaune
    def __init__(self):
        self.pos = [4, 0]
        self.color = 10
        self.shape = [[[1, 1], [1, 1]]]
        self.stuck = False
        self.rot = 0

    def rotate(self):
        pass

    def affichage(self):
        # Ajouter la pièce au centre de la matrice du jeu (sur la ligne 0)
        for i in range(len(self.shape[self.rot][0])):
            for j in range(len(self.shape[self.rot])):
                global matrice
                #Ajouter la pièce à la matrice à la position de la pièce self.pos[0] et self.pos[1]
                matrice[self.pos[0]+j][self.pos[1]+i] = self.shape[self.rot][j][i]

    def supprimer(self):
        for i in range(len(self.shape[self.rot][0])):
            for j in range(len(self.shape[self.rot])):
                global matrice
                #Ajouter la piéce à la matrice à la position de la piéce self.pos[0] et self.pos[1]
                matrice[self.pos[0]+j][self.pos[1]+i] = 0


class tetromino_i:  # barre bleu
    def __init__(self):
        self.pos = [3, 0]
        self.color = 12
        self.shape = [[[2], [2], [2], [2]], [[2, 2, 2, 2]]]
        self.rot = 0
        self.stuck = False
    
    def rotate(self):
        if self.rot == len(self.shape)-1:
            self.rot = 0
        else:
            self.rot += 1
        print(self.rot)


    def affichage(self):
        # Ajouter la pièce au centre de la matrice du jeu (sur la ligne 0)
        for i in range(len(self.shape[self.rot][0])):
            for j in range(len(self.shape[self.rot])):
                global matrice
                #Ajouter la pièce à la matrice à la position de la pièce self.pos[0] et self.pos[1]
                matrice[self.pos[0]+j][self.pos[1]+i] = self.shape[self.rot][j][i]

    def supprimer(self):
        for i in range(len(self.shape[self.rot][0])):
            for j in range(len(self.shape[self.rot])):
                matrice[self.pos[0]+j][self.pos[1]+i] = 0


class tetromino_s:  # s rouge
    def __init__(self):
        self.pos = [3, 0]
        self.color = 8
        self.shape = [[[0, 0, 0], [0, 1, 1], [1, 1, 0]], [[0, 1, 0], [0, 1, 1], [0, 0, 1]], [[0, 0, 0], [0, 1, 1], [1, 1, 0]], [[0, 1, 0], [0, 1, 1], [0, 0, 1]]]
        self.rot = 0
        self.stuck = False
        
    def rotate(self):
        if self.rot == len(self.shape)-1:
            self.rot = 0
        else:
            self.rot += 1
        print(self.rot)


    def affichage(self):
        # Ajouter la pièce au centre de la matrice du jeu (sur la ligne 0)
        for i in range(len(self.shape[self.rot][0])):
            for j in range(len(self.shape[self.rot])):
                global matrice
                #Ajouter la pièce à la matrice à la position de la pièce self.pos[0] et self.pos[1]
                matrice[self.pos[0]+j][self.pos[1]+i] = self.shape[self.rot][j][i]

    def supprimer(self):
        for i in range(len(self.shape[self.rot][0])):
            for j in range(len(self.shape[self.rot])):
                matrice[self.pos[0]+j][self.pos[1]+i] = 0


class tetromino_z:  # z vert
    def __init__(self):
        self.pos = [3, 0]
        self.color = 11
        self.shape = [[[0, 0, 0], [4, 4, 0], [0, 4, 4]], [[0, 0, 4], [0, 4, 4], [0, 4, 0]], [[0, 0, 0], [4, 4, 0], [0, 4, 4]], [[0, 0, 4], [0, 4, 4], [0, 4, 0]]]
        self.rot = 0
        self.stuck = False
        
    def rotate(self):
        if self.rot == len(self.shape)-1:
            self.rot = 0
        else:
            self.rot += 1
        print(self.rot)


    def affichage(self):
        # Ajouter la pièce au centre de la matrice du jeu (sur la ligne 0)
        for i in range(len(self.shape[self.rot][0])):
            for j in range(len(self.shape[self.rot])):
                global matrice
                #Ajouter la pièce à la matrice à la position de la pièce self.pos[0] et self.pos[1]
                matrice[self.pos[0]+j][self.pos[1]+i] = self.shape[self.rot][j][i]

    def supprimer(self):
        for i in range(len(self.shape[self.rot][0])):
            for j in range(len(self.shape[self.rot])):
                matrice[self.pos[0]+j][self.pos[1]+i] = 0


class tetromino_l:  # l orange
    def __init__(self):
        self.pos = [3, 0]
        self.color = 9
        self.shape = [[[0, 5, 0], [0, 5, 0], [0, 5, 5]], [[0, 0, 0], [0, 0, 5], [5, 5, 5]], [[5, 5, 0], [0, 1, 0], [0, 1, 0]], [[0, 0, 0], [1, 1, 1], [1, 0, 0]]]
        self.rot = 0
        self.stuck = False
    
    def rotate(self):
        if self.rot == len(self.shape):
            self.rot = 0
        else:
            self.rot += 1
        print(self.rot)


    def affichage(self):
        # Ajouter la pièce au centre de la matrice du jeu (sur la ligne 0)
        for i in range(len(self.shape[self.rot][0])):
            for j in range(len(self.shape[self.rot])):
                global matrice
                #Ajouter la pièce à la matrice à la position de la pièce self.pos[0] et self.pos[1]
                matrice[self.pos[0]+j][self.pos[1]+i] = self.shape[self.rot][j][i]

    def supprimer(self):
        for i in range(len(self.shape[self.rot][0])):
            for j in range(len(self.shape[self.rot])):
                matrice[self.pos[0]+j][self.pos[1]+i] = 0


class tetromino_j:  # j rose
    def __init__(self):
        self.pos = [3, 0]
        self.color = 14
        self.shape = [[[0, 0, 6], [0, 0, 6], [0, 6, 6]], [[0, 0, 0], [6, 6, 6], [0, 0, 6]], [[0, 6, 6], [0, 6, 6], [0, 6, 0]], [[0, 0, 0], [6, 0, 0], [6,6,6]],]
        self.rot = 0
        self.stuck = False
    def rotate(self):
        if self.rot == len(self.shape)-1:
            self.rot = 0
        else:
            self.rot += 1
        print(self.rot)

    def affichage(self):
        # Ajouter la pièce au centre de la matrice du jeu (sur la ligne 0)
        for i in range(len(self.shape[self.rot][0])):
            for j in range(len(self.shape[self.rot])):
                global matrice
                #Ajouter la pièce à la matrice à la position de la pièce self.pos[0] et self.pos[1]
                matrice[self.pos[0]+j][self.pos[1]+i] = self.shape[self.rot][j][i]

    def supprimer(self):
        for i in range(len(self.shape[self.rot][0])):
            for j in range(len(self.shape[self.rot])):
                matrice[self.pos[0]+j][self.pos[1]+i] = 0


class tetromino_t:  # t violet
    def __init__(self):
        self.pos = [3, 1]
        self.color = 2
        self.shape = [[[7, 7, 7], [0, 7, 0], [0, 0, 0]], [[0, 7,0], [0, 7, 7], [0, 7, 0]], [[0, 7,0], [1, 7, 0], [0, 7, 0]]]
        self.rot = 0
        self.stuck = False

    def rotate(self):
        if self.rot == len(self.shape)-1:
            self.rot = 0
        else:
            self.rot += 1
        print(self.rot)


    def affichage(self):
        # Ajouter la pièce au centre de la matrice du jeu (sur la ligne 0)
        for i in range(len(self.shape[self.rot][0])):
            for j in range(len(self.shape[self.rot])):
                global matrice
                #Ajouter la pièce à la matrice à la position de la pièce self.pos[0] et self.pos[1]
                matrice[self.pos[0]+j][self.pos[1]+i] = self.shape[self.rot][j][i]

    def supprimer(self):
        for i in range(len(self.shape[self.rot][0])):
            for j in range(len(self.shape[self.rot])):
                global matrice
                #Ajouter la piéce à la matrice à la position de la piéce self.pos[0] et self.pos[1]
                matrice[self.pos[0]+j][self.pos[1]+i] = 0

##################################### FIN CLASSE TETROMINOS #########################################
tetrominos = [tetromino_l()]
tetrominos2=[tetromino_l()]

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
            global tetrominos,tetrominos2
            global matrice
            ##Gravité
            #toutes les secondes, le block qui a self.stuck = False, ajouter 1 à son y
            if pyxel.frame_count % 60 == 0:
                for tetromino in tetrominos:
                    if tetromino.stuck == False:
                        #                      CARRÉ                                                    Barre verticale                                                                     Barre horizontale    
                        if (tetromino.pos[0] < 18 and tetromino.color == 10) or (tetromino.pos[0] < 16 and tetromino.color == 12 and tetromino.rot == 0) or (tetromino.pos[0] < 19 and tetromino.color == 12 and tetromino.rot == 1) or (tetromino.pos[0] <17  and tetromino.color == 9 and (tetromino.rot == 0 or tetromino.rot==3)) or (tetromino.pos[0] <17  and tetromino.color == 9 and tetromino.rot == 1) or (tetromino.pos[0] <18  and tetromino.color == 9 and tetromino.rot == 4):
                            tetromino.supprimer()
                            tetromino.pos[0] += 1
                        else:
                            tetrominos2.pop(0)
                            #tetromino.stuck = True
                        print(tetromino.pos)
            # afficher le triomino en cours
                #get the tetromino that is not stuck
            for tetromino in tetrominos:
                if tetromino.stuck == False:
                    if pyxel.btnp(pyxel.KEY_DOWN):
                        tetromino.rotate()
                    if pyxel.btnp(pyxel.KEY_LEFT) and tetromino.pos[1] > 0:
                        tetromino.supprimer()
                        tetromino.pos[1] -= 1
                    if pyxel.btnp(pyxel.KEY_RIGHT) and tetromino.pos[1] < 8:
                        tetromino.supprimer()
                        tetromino.pos[1] += 1
                    if pyxel.btnp(pyxel.KEY_SPACE):
                        #tetrominos pos y et pos x jusqu'a une collision avec un autre tetromino ou le bas
                        while tetromino.stuck == False:
                            tetromino.supprimer()
                            tetromino.pos[0] += 1
                            if tetrominos2==[]:
                                tetromino.stuck = True
                            #Faire le check des cases en dessous
                    tetromino.affichage()
                            


            for tetromino in tetrominos:
                tetromino.affichage() #NE PAS TOUCHER A CETTE LIGNE !!!
                #if all the blocks in the tetromino are stuck, create a new one
                check = 0
                if tetromino.stuck == False:
                    check = 1
            if check == 0:
                ls = [tetromino_i(), tetromino_o(), tetromino_t(), tetromino_s(), tetromino_z(), tetromino_j(), tetromino_l()]
                idx = random.randint(0, 6)
                tetrominos.append(ls[idx])

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
                        pyxel.rect(i*10+50, j*10, 10, 10,10)
                        pyxel.blt(i*10+50 +1, j*10 +1,0,0,8,8,8)
                    elif matrice[j][i] == 2:
                        pyxel.rect(i*10+50, j*10, 10, 10, 12)
                        pyxel.blt(i*10+50 +1, j*10 +1,0,8,8,8,8)
                    elif matrice[j][i] == 3:
                        pyxel.rect(i*10+50, j*10, 10, 10, 8)
                        pyxel.blt(i*10+50 +1, j*10 +1,0,16,8,8,8)
                    elif matrice[j][i] == 4:
                        pyxel.rect(i*10+50, j*10, 10, 10, 11)
                        pyxel.blt(i*10+50 +1, j*10 +1,0,24,8,8,8)
                    elif matrice[j][i] == 5:
                        pyxel.rect(i*10+50, j*10, 10, 10, 9)
                        pyxel.blt(i*10+50 +1, j*10 +1,0,32,8,8,8)
                    elif matrice[j][i] == 6:
                        pyxel.rect(i*10+50, j*10, 10, 10, 14)
                        pyxel.blt(i*10+50 +1, j*10 +1,0,40,8,8,8)
                    elif matrice[j][i] == 7:
                        pyxel.rect(i*10+50, j*10, 10, 10, 2)
                        pyxel.blt(i*10+50 +1, j*10 +1,0,48,8,8,8)
            ############################### FIN JEU #########################################
        

pygame.mixer.init()
pygame.mixer.Channel(0).play(pygame.mixer.Sound('main_theme.mp3'), -1)
App()