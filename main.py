from pygame import *

init()
win = display.set_mode((1280, 720))
display.set_caption("Пинг Понг")
bg = transform.scale(
    image.load("bg.png"),
    (1280, 720)
)

class GameSprite(sprite.Sprite):

    def __init__(self, x, y, w, h, s, im, rockettype):
        self.image = transform.scale(
            image.load(im),
            (w, h)
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.s = s
        self.rockettype = rockettype
    
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):

    def __init__(self, x, y, w, h, s, im, rockettype):
        super().__init__(x, y, w, h, s, im, rockettype)
    
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

r1 = Player(160, 360, 25, 160, 5, "rocket.png", 1)
r2 = Player(1120, 360, 25, 160, 5, "rocket.png", 2)

clock = time.Clock()

game = True

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
        
    r1.move()
    r2.move()
    
    win.blit(bg, (0, 0))
    r1.reset()
    r2.reset()
    
    display.update()