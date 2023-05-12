import pyxel
import main
import pygame
import random
import time

matrice = [[0 for i in range(10)] for j in range(22)]  # Matrice du jeu
matrice3=[[0 for i in range(10)] for j in range(22)]

score=0
f=open("best_scores.txt", "r")
high_score=int(f.readlines()[0])

vitesse=60
music='original'
##################################### Classes Tetrominos #########################################
class tetromino_o:  # Carré jaune
    def __init__(self):
        self.pos = [0, 4]
        self.color = 10
        self.shape = [[[0+self.pos[0], 0+self.pos[1]], [1+self.pos[0], 0+self.pos[1]], [0+self.pos[0], 1+self.pos[1]], [1+self.pos[0], 1+self.pos[1]]]]
        self.stuck = False
        self.rot = 0
        self.mini=[0,0]
        self.color2=1

    def rotate(self):
        pass

    def affichage(self):
        # Ajouter la pièce au centre de la matrice du jeu (sur la ligne 0)
        self.shape = [[[0+self.pos[0], 0+self.pos[1]], [1+self.pos[0], 0+self.pos[1]], [0+self.pos[0], 1+self.pos[1]], [1+self.pos[0], 1+self.pos[1]]]]
        for i in (self.shape[self.rot]):
            global matrice
            matrice[i[0]][i[1]]=1
            #Ajouter 1 aux coordonnées de la pièce pour la faire apparaitre

    def supprimer(self):
        for i in (self.shape[self.rot]):
            global matrice
            matrice[i[0]][i[1]]=0
            #Ajouter 0 aux coordonnées de la pièce pour la faire disparaitre

class tetromino_i:  # barre bleu
    def __init__(self):
        self.pos = [4, 3]
        self.color = 12
        self.shape = [[[self.pos[0]-3, 0+self.pos[1]], [self.pos[0]-1, 0+self.pos[1]], [self.pos[0]-2, 0+self.pos[1]], [0+self.pos[0], 0+self.pos[1]]], [[0+self.pos[0], 0+self.pos[1]], [0+self.pos[0], 1+self.pos[1]], [0+self.pos[0], 2+self.pos[1]], [0+self.pos[0], 3+self.pos[1]]]]
        self.rot = 0
        self.stuck = False
        self.mini=[8,0]
        self.color2=2
    
    def rotate(self):
        self.supprimer()
        if self.rot == len(self.shape)-1:
            self.rot = 0
        else:
            self.rot += 1
        self.affichage()
        print(self.rot)



    def affichage(self):
        # Ajouter la pièce au centre de la matrice du jeu (sur la ligne 0)
        self.shape=[[[self.pos[0]-3, 0+self.pos[1]], [self.pos[0]-1, 0+self.pos[1]], [self.pos[0]-2, 0+self.pos[1]], [0+self.pos[0], 0+self.pos[1]]], [[0+self.pos[0], 0+self.pos[1]], [0+self.pos[0], 1+self.pos[1]], [0+self.pos[0], 2+self.pos[1]], [0+self.pos[0], 3+self.pos[1]]]]
        try:
            for i in (self.shape[self.rot]):
                global matrice
                matrice[i[0]][i[1]]=2
                #Ajouter 1 aux coordonnées de la pièce pour la faire apparaitre
        except:
            self.supprimer()
            if self.rot != 0:
                self.rot -= 1
                self.affichage()
            else:
                self.rot = len(self.shape)-1
                self.affichage()
            pass

    def supprimer(self):
        for i in (self.shape[self.rot]):
            global matrice
            try:
                matrice[i[0]][i[1]]=0
            except:
                pass


class tetromino_s:  # s rouge
    def __init__(self):
        self.pos = [0, 3]
        self.color = 8
        self.shape = [[[2+self.pos[0], 0+self.pos[1]], [2+self.pos[0], 1+self.pos[1]], [1+self.pos[0], 1+self.pos[1]], [1+self.pos[0], 2+self.pos[1]]], [[0+self.pos[0], 0+self.pos[1]], [1+self.pos[0], 0+self.pos[1]], [1+self.pos[0], 1+self.pos[1]], [2+self.pos[0], 1+self.pos[1]]]]
        self.rot = 0
        self.stuck = False
        self.mini=[16,0]
        self.color2=3
        
    def rotate(self):
        self.supprimer()
        if self.rot == len(self.shape)-1:
            self.rot = 0
        else:
            self.rot += 1
        self.affichage()
        print(self.rot)


    def affichage(self):
        # Ajouter la pièce au centre de la matrice du jeu (sur la ligne 0)
        self.shape=[[[2+self.pos[0], 0+self.pos[1]], [2+self.pos[0], 1+self.pos[1]], [1+self.pos[0], 1+self.pos[1]], [1+self.pos[0], 2+self.pos[1]]], [[0+self.pos[0], 0+self.pos[1]], [1+self.pos[0], 0+self.pos[1]], [1+self.pos[0], 1+self.pos[1]], [2+self.pos[0], 1+self.pos[1]]]]
        try:
            for i in (self.shape[self.rot]):
                global matrice
                matrice[i[0]][i[1]]=3
                #Ajouter 1 aux coordonnées de la pièce pour la faire apparaitre
        except:
            self.supprimer()
            if self.rot != 0:
                self.rot -= 1
                self.affichage()
            else:
                self.rot = len(self.shape)-1
                self.affichage()
            pass

    def supprimer(self):
        for i in (self.shape[self.rot]):
            global matrice
            try:
                matrice[i[0]][i[1]]=0
            except:
                pass


class tetromino_z:  # z vert
    def __init__(self):
        self.pos = [0, 3]
        self.color = 11
        self.shape = [[[1+self.pos[0], 0+self.pos[1]], [1+self.pos[0], 1+self.pos[1]], [2+self.pos[0], 1+self.pos[1]], [2+self.pos[0], 2+self.pos[1]]], [[0+self.pos[0], 2+self.pos[1]], [1+self.pos[0], 2+self.pos[1]], [1+self.pos[0], 1+self.pos[1]], [2+self.pos[0], 1+self.pos[1]]]]
        self.rot = 0
        self.stuck = False
        self.mini=[24,0]
        self.color2=4
        
    def rotate(self):
        self.supprimer()
        if self.rot == len(self.shape)-1:
            self.rot = 0
        else:
            self.rot += 1
        self.affichage()
        print(self.rot)


    def affichage(self):
        # Ajouter la pièce au centre de la matrice du jeu (sur la ligne 0)
        self.shape= [[[1+self.pos[0], 0+self.pos[1]], [1+self.pos[0], 1+self.pos[1]], [2+self.pos[0], 1+self.pos[1]], [2+self.pos[0], 2+self.pos[1]]], [[0+self.pos[0], 2+self.pos[1]], [1+self.pos[0], 2+self.pos[1]], [1+self.pos[0], 1+self.pos[1]], [2+self.pos[0], 1+self.pos[1]]]]
        try:
            for i in (self.shape[self.rot]):
                global matrice
                matrice[i[0]][i[1]]=4
                #Ajouter 1 aux coordonnées de la pièce pour la faire apparaitre
        except:
            self.supprimer()
            if self.rot != 1:
                self.rot -= 1
                self.affichage()
            else:
                self.rot = len(self.shape)-1
                self.affichage()
            pass

    def supprimer(self):
        for i in (self.shape[self.rot]):
            global matrice
            try:
                matrice[i[0]][i[1]]=0
            except:
                pass


class tetromino_l:  # l orange
    def __init__(self):
        self.pos = [0, 3]
        self.color = 9
        self.shape = [[[0+self.pos[0], 0+self.pos[1]], [1+self.pos[0], 0+self.pos[1]], [2+self.pos[0], 0+self.pos[1]], [2+self.pos[0], 1+self.pos[1]]], [[1+self.pos[0], 0+self.pos[1]], [2+self.pos[0], 0+self.pos[1]], [1+self.pos[0], 1+self.pos[1]], [1+self.pos[0], 2+self.pos[1]]], [[0+self.pos[0], 0+self.pos[1]], [0+self.pos[0], 1+self.pos[1]], [1+self.pos[0], 1+self.pos[1]], [2+self.pos[0], 1+self.pos[1]]], [[1+self.pos[0], 2+self.pos[1]], [2+self.pos[0], 2+self.pos[1]], [2+self.pos[0], 1+self.pos[1]], [2+self.pos[0], 0+self.pos[1]]]]
        self.rot = 0
        self.stuck = False
        self.mini=[32,0]
        self.color2=5

    def rotate(self):
        self.supprimer()
        if self.rot == len(self.shape)-1:
            self.rot = 0
        else:
            self.rot += 1
        self.affichage()
        print(self.rot)


    def affichage(self):
        # Ajouter la pièce au centre de la matrice du jeu (sur la ligne 0)
        self.shape= [[[0+self.pos[0], 0+self.pos[1]], [1+self.pos[0], 0+self.pos[1]], [2+self.pos[0], 0+self.pos[1]], [2+self.pos[0], 1+self.pos[1]]], [[1+self.pos[0], 0+self.pos[1]], [2+self.pos[0], 0+self.pos[1]], [1+self.pos[0], 1+self.pos[1]], [1+self.pos[0], 2+self.pos[1]]], [[0+self.pos[0], 0+self.pos[1]], [0+self.pos[0], 1+self.pos[1]], [1+self.pos[0], 1+self.pos[1]], [2+self.pos[0], 1+self.pos[1]]], [[1+self.pos[0], 2+self.pos[1]], [2+self.pos[0], 2+self.pos[1]], [2+self.pos[0], 1+self.pos[1]], [2+self.pos[0], 0+self.pos[1]]]]
        try:
            for i in (self.shape[self.rot]):
                global matrice
                matrice[i[0]][i[1]]=5
                #Ajouter 1 aux coordonnées de la pièce pour la faire apparaitre
        except:
            self.supprimer()
            if self.rot != 0:
                self.rot -= 1
                self.affichage()
            else:
                self.rot = len(self.shape)-1
                self.affichage()
            pass
            

    def supprimer(self):
        for i in (self.shape[self.rot]):
            global matrice
            try:
                matrice[i[0]][i[1]]=0
            except:
                pass
            #Ajouter 0 aux coordonnées de la pièce pour la faire disparaitre


class tetromino_j:  # j rose
    def __init__(self):
        self.pos = [0, 3]
        self.color = 14
        self.shape = [[[0+self.pos[0], 1+self.pos[1]], [1+self.pos[0], 1+self.pos[1]], [2+self.pos[0], 1+self.pos[1]], [2+self.pos[0], 0+self.pos[1]]], [[1+self.pos[0], 0+self.pos[1]], [2+self.pos[0], 0+self.pos[1]], [2+self.pos[0], 1+self.pos[1]], [2+self.pos[0], 2+self.pos[1]]], [[0+self.pos[0], 0+self.pos[1]], [1+self.pos[0], 0+self.pos[1]], [2+self.pos[0], 0+self.pos[1]], [0+self.pos[0], 1+self.pos[1]]], [[1+self.pos[0], 0+self.pos[1]], [1+self.pos[0], 1+self.pos[1]], [1+self.pos[0], 2+self.pos[1]], [2+self.pos[0], 2+self.pos[1]]]]
        self.rot = 0
        self.stuck = False
        self.mini=[40,0]
        self.color2=6

    def rotate(self):
        self.supprimer()
        if self.rot == len(self.shape)-1:
            self.rot = 0
        else:
            self.rot += 1
        self.affichage()
        print(self.rot)

    def affichage(self):
        # Ajouter la pièce au centre de la matrice du jeu (sur la ligne 0)
        self.shape= [[[0+self.pos[0], 1+self.pos[1]], [1+self.pos[0], 1+self.pos[1]], [2+self.pos[0], 1+self.pos[1]], [2+self.pos[0], 0+self.pos[1]]], [[1+self.pos[0], 0+self.pos[1]], [2+self.pos[0], 0+self.pos[1]], [2+self.pos[0], 1+self.pos[1]], [2+self.pos[0], 2+self.pos[1]]], [[0+self.pos[0], 0+self.pos[1]], [1+self.pos[0], 0+self.pos[1]], [2+self.pos[0], 0+self.pos[1]], [0+self.pos[0], 1+self.pos[1]]], [[1+self.pos[0], 0+self.pos[1]], [1+self.pos[0], 1+self.pos[1]], [1+self.pos[0], 2+self.pos[1]], [2+self.pos[0], 2+self.pos[1]]]]
        try:
            for i in (self.shape[self.rot]):
                global matrice
                matrice[i[0]][i[1]]=6
                #Ajouter 1 aux coordonnées de la pièce pour la faire apparaitre
        except:
            self.supprimer()
            if self.rot != 0:
                self.rot -= 1
                self.affichage()
            else:
                self.rot = len(self.shape)-1
                self.affichage()
            pass

    def supprimer(self):
        for i in (self.shape[self.rot]):
            global matrice
            try:
                matrice[i[0]][i[1]]=0
            except:
                pass


class tetromino_t:  # t violet
    def __init__(self):
        self.pos = [1, 3]
        self.color = 2
        self.shape = [[[1+self.pos[0], 0+self.pos[1]], [1+self.pos[0], 1+self.pos[1]], [1+self.pos[0], 2+self.pos[1]], [2+self.pos[0], 1+self.pos[1]]], [[0+self.pos[0], 1+self.pos[1]], [1+self.pos[0], 1+self.pos[1]], [1+self.pos[0], 0+self.pos[1]], [2+self.pos[0], 1+self.pos[1]]], [[0+self.pos[0], 1+self.pos[1]], [1+self.pos[0], 1+self.pos[1]], [1+self.pos[0], 0+self.pos[1]], [1+self.pos[0], 2+self.pos[1]]], [[0+self.pos[0], 0+self.pos[1]], [1+self.pos[0], 0+self.pos[1]], [2+self.pos[0], 0+self.pos[1]], [1+self.pos[0], 1+self.pos[1]]]]
        self.rot = 0
        self.stuck = False
        self.mini=[48,0]
        self.color2=7

    def rotate(self):
        self.supprimer()
        if self.rot == len(self.shape)-1:
            self.rot = 0
        else:
            self.rot += 1
        self.affichage()
        print(self.rot)


    def affichage(self):
        # Ajouter la pièce au centre de la matrice du jeu (sur la ligne 0)
        self.shape=[[[1+self.pos[0], 0+self.pos[1]], [1+self.pos[0], 1+self.pos[1]], [1+self.pos[0], 2+self.pos[1]], [2+self.pos[0], 1+self.pos[1]]], [[0+self.pos[0], 1+self.pos[1]], [1+self.pos[0], 1+self.pos[1]], [1+self.pos[0], 0+self.pos[1]], [2+self.pos[0], 1+self.pos[1]]], [[0+self.pos[0], 1+self.pos[1]], [1+self.pos[0], 1+self.pos[1]], [1+self.pos[0], 0+self.pos[1]], [1+self.pos[0], 2+self.pos[1]]], [[0+self.pos[0], 0+self.pos[1]], [1+self.pos[0], 0+self.pos[1]], [2+self.pos[0], 0+self.pos[1]], [1+self.pos[0], 1+self.pos[1]]]]
        try:
            for i in (self.shape[self.rot]):
                global matrice
                matrice[i[0]][i[1]]=7
                #Ajouter 1 aux coordonnées de la pièce pour la faire apparaitre
        except:
            self.supprimer()
            if self.rot != 0:
                self.rot -= 1
                self.affichage()
            else:
                self.rot = len(self.shape)-1
                self.affichage()
            pass
    def supprimer(self):
        for i in (self.shape[self.rot]):
            global matrice
            try:
                matrice[i[0]][i[1]]=0
            except:
                pass

##################################### FIN CLASSE TETROMINOS #########################################
liste_tetro = [tetromino_i(), tetromino_o(), tetromino_t(), tetromino_s(), tetromino_z(), tetromino_j(), tetromino_l()]
tetrominos = [liste_tetro[random.randint(0, len(liste_tetro) - 1)]]

def lignes_d(x):
    save=[]
    for i in range(x):
        save.append(matrice[i])
    for i in range(x):
        try:
            matrice[i+1]=save[i]
        except:
            pass
    matrice[1]=[0,0,0,0,0,0,0,0,0,0]

def lignes_():
    global score
    sco=0
    a=0
    for i in range (22):
        if 0 not in matrice[i]:
            matrice[i]=[0,0,0,0,0,0,0,0,0,0]
            a+=1
            lignes_d(i)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('ligne.wav'))
    if a>0:
        sco=100
    if sco*a<400:
        score+=sco*a
    if sco*a==400:
            score+=500
def changement_vitesse():
    global score,vitesse
    if 1000<score<2000 :
        vitesse=50
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('vit.wav'))
    if 2000<score<3000 :
        vitesse=40
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('vit.wav'))
    if 3000<score<4000 :
        vitesse=30
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('vit.wav'))
    if 4000<score<5000 :
        vitesse=20
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('vit.wav'))
    if 5000<score :
        vitesse=10
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('vit.wav'))



###################### CLASSE DU JEU ######################
class App:
    def __init__(self):
        global score
        self.start = 'menu'
        pyxel.init(200, 200, title="T'ES TRISTE", fps=60)
        self.menu_items = ["Play", "Help", "Quit"]
        self.selected_item = 0 
        self.menu_color = 7 # white
        self.selected_color = 2 # violet
        self.button_height = 32 
        self.button_width = 70
        self.tetro_futur = []
        self.mem=[]
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
        global score,tetrominos
        global matrice,matrice3,vitesse
        if self.start == 'menu':
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

            if pyxel.btnp(pyxel.KEY_RETURN):
                if self.menu_items[self.selected_item] == "Play":
                    #On lance le jeu ici
                    print("Bouton Play cliqué")
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound('levelstrt.wav'))
                    pygame.time.delay(1000)
                    if music=='original':
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound('Original_theme.mp3'),-1)
                    if music=='metal':
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound('Tetris_metal.mp3'),-1)
                    self.start = 'game'
                    print("Le jeu est lancé")
                elif self.menu_items[self.selected_item] == "Help":
                    print("Bouton Help cliqué")
                elif self.menu_items[self.selected_item] == "Quit":
                    pyxel.quit()
            ############################### FIN MENU ##################################
        elif self.start == 'game':
            ############################### JEU #########################################
            
            if len(self.tetro_futur)<4:
                self.tetro_futur.append(random.randint(0,len(liste_tetro) -1 ))
            
            if pyxel.frame_count % vitesse == 0:
                if score>high_score:
                            with open('best_scores.txt', 'w') as output:
                                output.write(str(score))
                for tetromino in tetrominos:
                    if tetromino.stuck == False:
                        #if tetromino.color==12 and tetromino.rot==0:
                         #   for i in tetromino.shape[tetromino.rot]:
                          #      try:
                           #         if matrice[i[0]+1][i[1]]!=0 and [[i[0]+1][i[1]]] not in tetromino.shape[tetromino.rot] :
                            #            tetromino.stuck=True
                             #   except: 
                              #      pass
                                        

                        #on verifie si on déplace la matrice (shape) du tetromino vers le bas, si dans la matrice du jeu, d'autres tétrominos sont "supprimé" (on peut faire cela en verifiant la somme de tout les nombres de la matrice, si ce nombre est le meme que la matrice précédente alors, le tétromino déscend d'une case, sinon il devient stuck)
                        
                        #nombre de l'addition de la matrice du jeu avant le déplacement du tétromino (pour vérifier si le tétromino peut descendre d'une case)
                        nb_matrice = 0
                        for i in range(20):
                            for j in range(9):
                                nb_matrice += matrice[i][j]
                        #nombre de l'addition de la matrice du jeu après le déplacement du tétromino (pour vérifier si le tétromino peut descendre d'une case)
                        nb_matrice2 = 0
                        matrice2 = matrice
                        #on déplace le tétromino d'une case vers le bas si il ne sort pas de la matrice du jeu (si il ne sort
                        
                        if tetromino.pos[0] < 19:
                            pos = tetromino.pos
                            
                            try:
                                for i in range(22):
                                        for j in range(10):
                                            matrice3[i][j]=matrice[i][j]
                                tetromino.supprimer()
                                tetromino.pos[0] += 1
                                tetromino.affichage()
                                
                                print("tetromino descendu")
                            except:
                                pass
                        else:
                            for i in range(22):
                                        for j in range(10):
                                            matrice[i][j]=matrice3[i][j]
                            if 0<tetromino.pos[0]<=1 and 0<tetromino.pos[1]<=8:
                                    self.start='game_over'
                            tetromino.stuck = True 
                            pygame.mixer.Channel(1).play(pygame.mixer.Sound('stuck.wav'))
                            
                            

                            
                            #on regarge si ça crée une erreur 'list index out of range'
                            
                        #on vérifie si le tétromino peut descendre d'une case
                        for i in range(20):
                            for j in range(9):
                                nb_matrice2 += matrice2[i][j]
                        #si le tétromino ne peut pas descendre d'une case, on le remet à sa position initiale
                        if nb_matrice != nb_matrice2:
                            print("tetromino non descendu essai 2")
                            tetromino.supprimer()
                            tetromino.pos[0] -= 1

                            for i in range(22):
                                        for j in range(10):
                                            matrice[i][j]=matrice3[i][j]
                            
                                
                            if 0<tetromino.pos[0]<=1 and 0<tetromino.pos[1]<=8:
                                    self.start='game_over'
                            tetromino.stuck = True
                            pygame.mixer.Channel(1).play(pygame.mixer.Sound('stuck.wav'))
                            
                        
            # afficher le triomino en cours
                #get the tetromino that is not stuck
            for tetromino in tetrominos:
                if tetromino.stuck == False:
                        
                    if  pyxel.btnp(pyxel.KEY_UP):
                        pass
                    if pyxel.btnp(pyxel.KEY_Q) or pyxel.btnp(pyxel.KEY_D):
                        if not (tetromino.pos[1] == -1 and tetromino.color == 11 and tetromino.rot == 1):
                            tetromino.rotate()

                    if pyxel.btnp(pyxel.KEY_LEFT) and tetromino.pos[1] >= 0 and tetromino.color==11 and tetromino.rot==1 and ([[tetromino.pos[1]-1],[tetromino.pos[0]]] not in tetromino.shape[tetromino.rot] or matrice[tetromino.pos[1]-1][tetromino.pos[0]]==0):
                        tetromino.supprimer()
                        try:
                            tetromino.pos[1] -= 1
                        except:
                            
                            tetromino.pos[1] += 1

                    if pyxel.btnp(pyxel.KEY_LEFT) and tetromino.pos[1] > 0 and ([[tetromino.pos[1]-1],[tetromino.pos[0]]] not in tetromino.shape[tetromino.rot]or matrice[tetromino.pos[1]-1][tetromino.pos[0]]==0) :
                        if not(tetromino.color==11 and tetromino.rot==1):
                            tetromino.supprimer()
                            try:
                                tetromino.pos[1] -= 1
                            except:
                                
                                tetromino.pos[1] += 1
                            
                    if pyxel.btnp(pyxel.KEY_RIGHT) and tetromino.pos[1] <= 8 and tetromino.color==12 and tetromino.rot==0 and ([[tetromino.pos[1]],[tetromino.pos[0]-1]]not in tetromino.shape[tetromino.rot] or matrice[tetromino.pos[1]+1][tetromino.pos[0]]==0) :
                        tetromino.supprimer()
                        try:
                            tetromino.pos[1] += 1
                        except:
                            
                            tetromino.pos[1] -= 1

                    if pyxel.btnp(pyxel.KEY_RIGHT) and tetromino.pos[1] < 8 and ([[tetromino.pos[1]],[tetromino.pos[0]-1]]not in tetromino.shape[tetromino.rot]or matrice[tetromino.pos[1]+1][tetromino.pos[0]]==0) :
                        if tetromino.color==12 and tetromino.rot==0:
                            pass
                        else:
                            tetromino.supprimer()
                            try:
                                tetromino.pos[1] += 1
                            except:
                                
                                tetromino.pos[1] -= 1
                    if pyxel.btnp(pyxel.KEY_SPACE):
                    
                        #tetrominos pos y et pos x jusqu'a une collision avec un autre tetromino ou le bas
                        while tetromino.stuck == False:
                            
                            #vérifier si le tetromino peut descendre d'une case comme dans le for tetromino in tetrominos
                           
                            nb_matrice = 0
                            for i in range(20):
                                for j in range(9):
                                    nb_matrice += matrice[i][j]
                            #nombre de l'addition de la matrice du jeu après le déplacement du tétromino (pour vérifier si le tétromino peut descendre d'une case)
                            nb_matrice2 = 0
                            matrice2 = matrice
                            
                            if tetromino.pos[0] < 19:
                                pos = tetromino.pos
                                
                                try:
                                    for i in range(22):
                                        for j in range(10):
                                            matrice3[i][j]=matrice[i][j]
                                    tetromino.supprimer()
                                    tetromino.pos[0] += 1
                                    tetromino.affichage()
                                    
                                    print("tetromino descendu")
                                except:
                                    pass
                            else: 
                                for i in range(22):
                                        for j in range(10):
                                            matrice[i][j]=matrice3[i][j]
                                if 0<tetromino.pos[0]<=1 and 0<tetromino.pos[1]<=8:
                                    self.start='game_over'
                                tetromino.stuck = True
                                pygame.mixer.Channel(1).play(pygame.mixer.Sound('stuck.wav'))
                                
                                    
                                    
                                

                                #on regarge si ça crée une erreur 'list index out of range'

                            #on vérifie si le tétromino peut descendre d'une case
                            
                            for i in range(20):
                                for j in range(9):
                                    nb_matrice2 += matrice2[i][j]
                            #si le tétromino ne peut pas descendre d'une case, on le remet à sa position initiale
                            if nb_matrice != nb_matrice2:
                                print("tetromino non descendu essai 2")
                                tetromino.supprimer()
                                
                                tetromino.pos[0] -= 1
                                for i in range(22):
                                        for j in range(10):
                                            matrice[i][j]=matrice3[i][j]
                                if 0<tetromino.pos[0]<=1 and 0<tetromino.pos[1]<=8:
                                    self.start='game_over'
                                tetromino.stuck = True
                                
                                pygame.mixer.Channel(1).play(pygame.mixer.Sound('stuck.wav'))
                    tetromino.affichage()
    
                            


            for tetromino in tetrominos:
                tetromino.affichage() #NE PAS TOUCHER A CETTE LIGNE !!!
                #if all the blocks in the tetromino are stuck, create a new one
                check = 0
                if tetromino.stuck == False:
                    check = 1
                else:
                    tetrominos.pop()
                    score+=15
                    ls = [tetromino_i(), tetromino_o(), tetromino_t(), tetromino_s(), tetromino_z(), tetromino_j(), tetromino_l()]
                    t = self.tetro_futur.pop(0)
                    tetrominos.append(ls[t])
            if check == 0:
                
                
                lignes_()
                changement_vitesse()
                

            ############################### FIN JEU #########################################
            

    def draw(self):
        global score,vitesse
        if self.start=='game_over':
            pyxel.cls(0)
            pyxel.text(80,100,f"GAME OVER", 7)
        if self.start == 'menu':
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
        elif self.start == 'game':
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
            pyxel.text(2,2,f"SCORE: \n{score}", 11,)
            pyxel.text(2,16, f'HIGHEST:\n{high_score}', 11)
            pyxel.text(2,40, f'VITESSE:\n{vitesse}', 11)
            ############################### FIN JEU #########################################
            #pyxel.rect(2, 40, 45, 140, 0)
            ls = [tetromino_i(), tetromino_o(), tetromino_t(), tetromino_s(), tetromino_z(), tetromino_j(), tetromino_l()]
            for i in range(len(self.tetro_futur)):
                pyxel.blt(180, 5*i +5,0,ls[self.tetro_futur[i]].mini[0],ls[self.tetro_futur[i]].mini[1],8,8)
            for i in self.mem:
                pyxel.blt(180, 5*i +5,0,i.mini[0],i.mini[1],8,8)

pygame.mixer.init()
pygame.mixer.Channel(0).set_volume(0.2)
pygame.mixer.Channel(1).set_volume(0.5)
pygame.mixer.Channel(0).play(pygame.mixer.Sound('main_theme.mp3'), -1)
App()
