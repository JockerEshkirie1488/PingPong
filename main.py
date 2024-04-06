from pygame import *

init()
win = display.set_mode((1280, 720))
display.set_caption("Пинг Понг")
bg = transform.scale(
    image.load("bg.png"),
    (1280, 720)
)

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
            if keys_pressed[K_w] and self.rect.y > 40:
                self.rect.y -= self.s
            if keys_pressed[K_s] and self.rect.y < 680:
                self.rect.y += self.s
        elif self.rockettype == 2:
            if keys_pressed[K_UP] and self.rect.y > 40:
                self.rect.y -= self.s
            if keys_pressed[K_DOWN] and self.rect.y < 680:
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
        if self.rect.centerx <= 60 or self.rect.centerx >= 1220:
            self.speedx *= -1

r1 = Player(160, 300, 25, 160, 5, "rocket.png", 1)
r2 = Player(1120, 300, 25, 160, 5, "rocket.png", 2)
ball = Enemy(240, 300, 128, 128, 6, "ball.png", 6, 5)

clock = time.Clock()

game = True

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
        
    r1.move()
    r2.move()
    ball.move()

    if Rect.colliderect(ball.rect, r1.rect):
        ball.speedx *= -1
    if Rect.colliderect(ball.rect, r2.rect):
        ball.speedx *= -1
    
    win.blit(bg, (0, 0))
    ball.reset()
    r1.reset()
    r2.reset()
    
    display.update()