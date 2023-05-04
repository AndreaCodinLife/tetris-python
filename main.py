# importing required library
import pygame
 
# activate the pygame library .
pygame.init()
X = 600
Y = 600
# create the display surface object
# of specific dimension..e(X, Y).
scrn = pygame.display.set_mode((X, Y))
pygame.mixer.init()
pygame.mixer.music.load('intro.wav')
#set the volume of the music
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()
pygame.time.delay(1000)
# set the pygame window name
pygame.display.set_caption('ACA Studios')
 
# create a surface object, image is drawn on it.
imp = pygame.image.load("ACA.png").convert()
#change the image size to fit the screen
imp = pygame.transform.scale(imp, (X, Y))
#make the image apear with an annimation like a fade in
for i in range(255):
    imp.set_alpha(i)
    scrn.blit(imp, (0, 0))
    pygame.display.flip()
    pygame.time.delay(1)

# Using blit to copy content from one surface to other
 
status = True
while (status):
 
  # iterate over the list of Event objects
  # that was returned by pygame.event.get() method.
    for i in pygame.event.get():
 
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if i.type == pygame.QUIT:
            status = False
        #Wait 5 seconds before closing the window
    pygame.time.delay(4000)
    status = False
 
# deactivates the pygame library
pygame.quit()