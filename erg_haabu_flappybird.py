import pygame

pygame.init()

ekraan = pygame.display.set_mode([1280, 720])
pygame.display.set_caption("Flappy Bird")
lind = pygame.image.load("lind.png")

linnu_x = 400
linnu_y = 360
loendaja = 0

mäng_töötab = False
hüpe = False
kukkumine = False

def küsi_valikut(pildi_aadress, valikud):
    pilt = pygame.image.load(pildi_aadress)
    laius = pilt.get_width()
    kõrgus = pilt.get_height()

    myfont = pygame.font.SysFont("monospace", 32, bold=True)
    myfont2 = pygame.font.SysFont("monospace", 24, bold=True, italic=False)

    labels = [myfont.render(e, 1, (255,255,255)) for e in valikud]
    labels_select = [myfont.render(e, 1, (255,0,0)) for e in valikud]
    
    ekraan2 = pygame.display.set_mode([1280, 720])
    
    while True:

        x, y = pygame.mouse.get_pos()
        
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if i.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(valikud)):
                    if y > kõrgus - 70 - 50 * i and y < kõrgus - 70 - 50 * i + 32:
                        return valikud[i]
                
        ekraan2.fill([0,0,0])
        ekraan2.blit(pilt, [0, 0])
    
        for i in range(len(labels)):
            if y > kõrgus - 70 - 50 * i and y < kõrgus - 70 - 50 * i + 32:
                ekraan2.blit(labels_select[i], (580, kõrgus - 70 - 50 * i))
            else:
                ekraan2.blit(labels[i], (580, kõrgus - 70 - 50 * i))
                
        pygame.display.flip()
        pygame.time.delay(16)

def näita_teadet(pildi_aadress, teade):
    küsi_valikut(pildi_aadress, teade, ["Edasi"])
    
valik1 = küsi_valikut("algus.png", ["Mängi"])

if valik1 == "Mängi":
    mäng_töötab = True

while mäng_töötab:
    ekraan = pygame.display.set_mode([1280, 720])
    for e in pygame.event.get():
         if e.type == pygame.QUIT:
              mäng_töötab = False
         elif e.type == pygame.MOUSEBUTTONDOWN:
             hüpe = True
                
    if hüpe:
        linnu_y -= 20
        loendaja += 1
        if loendaja >= 10:
            loendaja = 0
            hüpe = False
            kukkumine = True   
    if kukkumine:    #gravitatsioon
        linnu_y += 7
    if linnu_y >= 640: #et lind ei saaks alumisest ekraani servast allapoole kukkuda
        linnu_y = 640
    if linnu_y <= -5: #et lind ei saaks üle ülemise ääre minna
        linnu_y = -5
             
    ekraan.fill([255, 255, 255])
    ekraan.blit(lind, [linnu_x, linnu_y])
    pygame.display.flip()
    pygame.time.delay(17)
pygame.quit()

