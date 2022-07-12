import pygame as pg
import sys
import random

class Screen:
    def __init__(self, title, wh, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)     #Surface
        self.rct = self.sfc.get_rect()         # Rect
        self.bgi_sfc = pg.image.load(image)    # Surface
        self.bgi_rct = self.bgi_sfc.get_rect() # Rect

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) #背景画像用


class Bird:
    def __init__(self, image, size, xy):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy

    def blit(self, scr):
        scr.sfc.blit(self.sfc, self.rct)
        #screen_sfc.blit(kkimg_sfc, kkimg_rct)

    def update(self, scr: Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]: 
            self.rct.centery -= 1
        if key_states[pg.K_DOWN]: 
            self.rct.centery += 1
        if key_states[pg.K_LEFT]: 
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT]: 
            self.rct.centerx += 1
        # 練習7
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]: 
                self.rct.centery += 1
            if key_states[pg.K_DOWN]: 
                self.rct.centery -= 1
            if key_states[pg.K_LEFT]: 
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT]: 
                self.rct.centerx -= 1
        self.blit(scr)

    def attack(self):
        return Shot(self)


class Bomb:
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 128, 0)]
    def __init__(self, color, size, vxy, scr:Screen):
        #color = random.shuffle(Bomb.colors)
        #vx = random.shuffle([-1, +1])
        #vy = random.shuffle([-1, +1])
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy # 練習6

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        # 練習6
        self.rct.move_ip(self.vx, self.vy)
        # 練習7
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        # 練習5
        self.blit(scr)

#UFOを動かせるようにする
class UFO:
    speed = 10
    images = []
    def __init__(self, image, size, xy):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy
        #これで動かせるようにしたかった
        #self.vx, self.vy = XY
        # self.image = self.images[0]
        # self.facing = random.choice((-1, 1)) * UFO.speed
        # self.frame = 0
        # if self.facing < 0:
        #     self.rect.right = scr.rct.right

    def blit(self, scr):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        # 練習6
        #self.rct.move_ip(self.vx, self.vy)
        #self.rct.move_ip(+1, 0)
        self.blit(scr)

#ビームがこうかとんから出るようにする
class Shot:
    def __init__(self, chr:Bird):
        self.sfc = pg.image.load("fig/beam.png")    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, 1.0)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.midleft = chr.rct.center

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(+1, 0)
        if check_bound(self.rct, scr.rct):
            del self
        self.blit(scr)
   

def main():
    clock = pg.time.Clock()
    scr = Screen("逃げろ！こうかとん", (1600, 900), "fig/hosi.jpg")
    kkt = Bird("fig/6.png", 2.0, (900, 400))
    bkd = Bomb((255, 0, 0), 10, (+1, +1), scr)
    ufo = UFO("fig/UFO3.png", 0.5, (900, 400))
    beam = None

    while True:
        #screen_sfc.blit(bgimg_sfc, bgimg_rct)
        scr.blit()
        # 練習2
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                beam = kkt.attack()

        kkt.update(scr)
        bkd.update(scr)
        ufo.update(scr)
        if beam:
            beam.update(scr)

        if kkt.rct.colliderect(bkd.rct):
            return

        pg.display.update()
        clock.tick(1000)


# 練習7
def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()