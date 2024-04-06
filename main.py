from pygame import *

init()
win = display.set_mode((1280, 720))
display.set_caption("Пинг Понг")
bg = transform.scale(
    image.load("bg.png"),
    (1280, 720)
)

class GameSprite(sprite.Sprite):
    def __init__(self, x, y, w, h, s, image):
        self.image = transform.scale(
            image.load(image),
            (1280, 720)
        )
        self.rect = self.image.get_rect()

clock = time.Clock()

game = True

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(60)
    win.blit(bg, (0, 0))
    display.update()