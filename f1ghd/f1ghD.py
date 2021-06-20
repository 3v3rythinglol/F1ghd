import pygame
import random
pygame.init()

wn = pygame.display.set_mode((1500, 700))

bg = pygame.image.load('re/background.png')
ch = pygame.image.load('re/char.png')
animation = [pygame.image.load('re/char.png'), pygame.image.load('re/char_ani1.png'), pygame.image.load('re/char_ani2.png'), pygame.image.load('re/char_ani3.png'), pygame.image.load('re/char_ani4.png'), pygame.image.load('re/char_ani5.png'), pygame.image.load('re/char_ani6.png'), pygame.image.load('re/char_ani5.png'), pygame.image.load('re/char_ani4.png'), pygame.image.load('re/char_ani3.png'), pygame.image.load('re/char_ani2.png'), pygame.image.load('re/char_ani1.png')]
count = 0
enlist = []
ensc = 0
enss = 100
chas = 75
chac = 0
chatc =  True
chani = True
run = True

class enemy():
    def __init__(self, ex, ehp):
        self.ex = ex
        self.ehp = ehp
    def move(self):
        if self.ex > 800:
            self.ex -= 2
        if self.ex < 600:
            self.ex += 2
        pygame.draw.rect(wn, (255, 0, 0), (self.ex, 300, 100, 150))
        

def me():
    global chani
    global chatc
    global count
    global chac
    global chas
    if chani == True:
        wn.blit(ch, (650, 250))
        count = 0
        if chatc == False:
            chac += 1
        if chac >= chas:
            chac = 0
            chatc = True
    elif chani == False and chatc == False:
        count += 1
        if count >= 12:
            count = 0
            chani = True
        wn.blit(animation[count], (650, 250))
       
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
                
    keys = pygame.key.get_pressed()
    
    wn.blit(bg, (0, 0))
    
    ensc += 1
    if ensc >= enss:
        ensc = 0
        if random.randrange(1, 3) == 1:
            enlist.append(enemy(0, 1))
        else:
            enlist.append(enemy(1400, 1))
            
    if keys[pygame.K_q] and chatc == True:
        chani = False
        chatc = False
            
    me()
    
    for i in enlist:
        i.move()
        if i.ex >= 600 and i.ex <= 800:
            enlist.pop(enlist.index(i))
    
    pygame.display.update()
pygame.QUIT