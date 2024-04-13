from pygame import *
from random import randint

init()
win = display.set_mode((1280, 720))
display.set_caption("Пинг Понг")
bg = transform.scale(
    image.load("bg.png"),
    (1280, 720)
)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
count1 = 0
count2 = 0
f = font.SysFont("Arial", 36)
ff = font.SysFont("Arial", 60)
game_over1 = ff.render("ИГРОК 1 ПРОИГРАЛ", False, RED)
game_over2 = ff.render("ИГРОК 2 ПРОИГРАЛ", False, RED)
count1_text = ff.render(f"ПРОПУЩЕНО: {count1}", False, BLUE)
count2_text = ff.render(f"ПРОПУЩЕНО: {count2}", False, RED)


class GameSprite(sprite.Sprite):

    def __init__(self, x, y, w, h, s, im):
        self.image = transform.scale(
            image.load(im),
            (w, h)
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.s = s

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):

    def __init__(self, x, y, w, h, s, im, rockettype):
        super().__init__(x, y, w, h, s, im)
        self.rockettype = rockettype
    
    def move(self):
        keys_pressed = key.get_pressed()
        if self.rockettype == 1:
            if keys_pressed[K_w] and self.rect.y > 4:
                self.rect.y -= self.s
            if keys_pressed[K_s] and self.rect.y < 560:
                self.rect.y += self.s
        elif self.rockettype == 2:
            if keys_pressed[K_UP] and self.rect.y > 4:
                self.rect.y -= self.s
            if keys_pressed[K_DOWN] and self.rect.y < 560:
                self.rect.y += self.s

class Enemy(GameSprite):

    def __init__(self, x, y, w, h, s, im, speedx, speedy):
        super().__init__(x, y, w, h, s, im)
        self.speedx = speedx
        self.speedy = speedy
    
    def move(self):

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.centery <= 60 or self.rect.centery >= 660:
            self.speedy *= -1

r1 = Player(160, 300, 25, 160, 5, "rocket1.png", 1)
r2 = Player(1120, 300, 25, 160, 5, "rocket2.png", 2)
ball = Enemy(460, 300, 96, 96, 6, "ball.png", 7, 6)
cube1 = GameSprite(randint(240, 1040), randint(100, 620), 100, 100, 0, "cube.png")
cube2 = GameSprite(randint(240, 1040), randint(100, 620), 100, 100, 0, "cube.png")

clock = time.Clock()

game = True
loser = None

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
      
    r1.move()
    r2.move()
    ball.move()

    if Rect.colliderect(ball.rect, r1.rect):
        ball.speedx *= -1
        if randint(1, 2) == 1:
            ball.speedy *= 1
    if Rect.colliderect(ball.rect, r2.rect):
        ball.speedx *= -1
        if randint(1, 2) == 1:
            ball.speedy *= 1
    if Rect.colliderect(ball.rect, cube1.rect):
        ball.speedx *= -1
        if randint(1, 2) == 1:
            ball.speedy *= 1
        cube1.rect.x = randint(240, 1040)
        cube1.rect.y = randint(100, 620)
    if Rect.colliderect(ball.rect, cube2.rect):
        ball.speedx *= -1
        if randint(1, 2) == 1:
            ball.speedy *= 1
        cube2.rect.x = randint(240, 1040)
        cube2.rect.y = randint(100, 620)
    
    if ball.rect.x < 5:
        count1 += 1
        ball.rect.x = 460
        ball.rect.y = 300
        ball.speedx *= -1
    if ball.rect.x > 1155:
        count2 += 1
        ball.rect.x = 460
        ball.rect.y = 300
        ball.speedx *= -1
    
    if count1 == 5:
        loser = 1
    if count2 == 5:
        loser = 2

    count1_text = f.render(f"ПРОПУЩЕНО: {count1}", False, BLUE)
    count2_text = f.render(f"ПРОПУЩЕНО: {count2}", False, RED)
    
    win.blit(bg, (0, 0))    
    ball.reset()
    r1.reset()
    r2.reset()
    cube1.reset()
    cube2.reset()
    win.blit(count1_text, (20, 30))
    win.blit(count2_text, (960, 30))

    display.update()

    count1_text = f.render(f"ПРОПУЩЕНО: {count1}", False, BLUE)
    count2_text = f.render(f"ПРОПУЩЕНО: {count2}", False, RED)

    while loser:

        for e in event.get():
            if e.type == QUIT:
                game = False              
                loser = None

        keys_pressed = key.get_pressed()
        if keys_pressed[K_r]:
            loser = None
            count1 = 0
            count2 = 0
            count1_text = f.render(f"ПРОПУЩЕНО: {count1}", False, BLUE)
            count2_text = f.render(f"ПРОПУЩЕНО: {count2}", False, RED)
            r1 = Player(160, 300, 25, 160, 5, "rocket1.png", 1)
            r2 = Player(1120, 300, 25, 160, 5, "rocket2.png", 2)
            ball = Enemy(460, 300, 96, 96, 6, "ball.png", 7, 6)
            cube1 = GameSprite(randint(240, 1040), randint(100, 620), 100, 100, 0, "cube.png")

        if loser == 1:
            win.blit(game_over1, (400, 320))
        elif loser == 2:
            win.blit(game_over2, (400, 320))
    
        display.update()