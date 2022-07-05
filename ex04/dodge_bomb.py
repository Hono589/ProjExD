import pygame as pg
import sys
import random

def main():
  clock = pg.time.Clock()
  pg.display.set_caption("逃げろ！こうかとん")
  screen_sfc = pg.display.set_mode((1600, 900)) #Surface
  screen_rct = screen_sfc.get_rect()            #画面用Rect
  bgimg_sfc = pg.image.load("fig/pg_bg.jpg")    #背景画像用Surface
  bgimg_rct = bgimg_sfc.get_rect()              #Rect
  screen_sfc.blit(bgimg_sfc, bgimg_rct)

  #練習3 こうかとん
  kkimg_sfc = pg.image.load("fig/2.png")   #効果トン画像用Surface
  kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0)  #効果トン画像の拡大Surface
  kkimg_rct = kkimg_sfc.get_rect()         #こうかとん画像用Rect
  kkimg_rct.center = 900, 400              #こうかとんの中心を900、400に指定

  #練習5 爆弾
  bmimg_sfc = pg.Surface((20, 20)) #爆弾用Surface
  bmimg_sfc.set_colorkey((0, 0, 0))   
  pg.draw.circle(bmimg_sfc, (255, 0, 0), (10, 10), 10)  #爆弾用Surfaceに円を描く。色・中心・半径を指定
  bmimg_rct = bmimg_sfc.get_rect() #爆弾用Rect
  bmimg_rct.centerx = random.randint(0, screen_rct.width)  #爆弾のx座標をランダムに決定
  bmimg_rct.centery = random.randint(0, screen_rct.height)  #爆弾のy座標をランダムに決定

  vx, vy = +1, +1



  #pg.display.update()
  #clock.tick(0.5)

  while True:
    screen_sfc.blit(bgimg_sfc, bgimg_rct)
    

    #練習2
    for event in pg.event.get():
      if event.type == pg.QUIT:
        return

    #練習4
    key_states = pg.key.get_pressed()#辞書
    if key_states[pg.K_UP] == True: kkimg_rct.centery -= 1  #y座標を－1
    if key_states[pg.K_DOWN] == True: kkimg_rct.centery += 1 #y +1
    if key_states[pg.K_LEFT] == True: kkimg_rct.centerx -= 1 #y -1
    if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx += 1 #y +1
    if check_bound(kkimg_rct, screen_rct) != (1, 1):
      if key_states[pg.K_UP] == True: kkimg_rct.centery += 1  #y座標を－1
      if key_states[pg.K_DOWN] == True: kkimg_rct.centery -= 1 #y +1
      if key_states[pg.K_LEFT] == True: kkimg_rct.centerx += 1 #y -1
      if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx -= 1
    screen_sfc.blit(kkimg_sfc, kkimg_rct)

    #練習6
    bmimg_rct.move_ip(vx, vy)

    #練習5
    screen_sfc.blit(bmimg_sfc, bmimg_rct)

    #練習7 #爆弾の移動
    x, y = check_bound(bmimg_rct, screen_rct)
    vx *= x
    vy *= y

    #練習8 爆弾の当たり判定
    if kkimg_rct.colliderect(bmimg_rct) == True: #toriがbombと重なったらTrue
            return #終了(mainから抜ける)
    

    pg.display.update()
    clock.tick(1000)

def check_bound(rct, scr_rct):
   #画面内なら：+1 / 画面外なら：-1を返す
    x, y = +1, +1
    if rct.left < scr_rct.left or scr_rct.right < rct.right: x = -1   #画面外に行ったらx=-1
    if rct.top < scr_rct.top or scr_rct.bottom < rct.bottom: y = -1   #画面外に行ったらy=-1
    return x, y

if __name__ == "__main__":
  pg.init()
  main()
  pg.quit()
  sys.exit()