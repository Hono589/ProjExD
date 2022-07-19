import pygame as pg
from pygame.locals import *  
from setting import *
from stage import *

#テキスト描画用の関数
def draw_text(text, size, x, y, color):
		font = pg.font.Font(None, size)
		text_surface = font.render(text, True, color)
		text_rect = text_surface.get_rect()
		text_rect.midtop = (x, y)
		SCREEN.blit(text_surface,text_rect)

#プレイヤークラス
class Player(pg.sprite.Sprite):
    def __init__(self,x,y, size,im):
        pg.sprite.Sprite.__init__(self)
        #self.image = pg.Surface((PLAYER_SIZE,PLAYER_SIZE))
        self.image = pg.image.load(im)
        self.image = pg.transform.rotozoom(self.image, 0, size)
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
        self.width = self.image.get_width()
        self.height = self.image.get_height() 
        self.goal = False
        
    def update(self,data):
        #プレイヤーの移動距離
        dx = 0
        dy = 0

		#プレイヤーのキー操作
        key = pg.key.get_pressed()
        if key[K_LEFT]:
            dx -= 5
        if key[K_RIGHT]:
            dx += 5
        if key[K_UP]:
            dy -= 5
        if key[K_DOWN]:
            dy += 5

        #壁との接触判定
        for tile in data:
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                dy = 0
        
        #移動速度を足す
        self.rect.x += dx
        self.rect.y += dy

        #ゴールした場合の処理
        if self.rect.left > WIDTH:
            self.kill()
            self.goal = True
            

#ステージクラス       
class Stage():
	def __init__(self, data):
		#空のリストを用意
		self.tile_list = []
		#のちに用意するstageの番号1を地面とし、リストに位置とサイズ情報を格納していく
		row_count = 0
		for row in data:
			col_count = 0
			for tile in row:
				if tile == 1:
					self.img = pg.image.load("ex06/meiro1/wall1.png")
					img_rect = self.img.get_rect()
					img_rect.x = col_count * CHIP_SIZE
					img_rect.y = row_count * CHIP_SIZE
					tile = (self.img, img_rect)
					self.tile_list.append(tile) 
				col_count += 1
			row_count += 1
        
	#上で得たリスト情報を元にスクリーンに描画する	
	def draw(self,screen):
		for tile in self.tile_list:
            #tile[0]には画像、tile[1]にはrectサイズの情報が入っている。
			SCREEN.blit(tile[0],tile[1])


#メインゲームクラス
class Game():
    def __init__(self):
        pg.init()      

        #各クラスのインスタンス化
        self.all_sprite = pg.sprite.Group()
        self.player = Player(50, 50, 0.3,"ex06/meiro1/wan.png")
        self.all_sprite.add(self.player)
        self.stage = Stage(stage_data)
       
    #メインループメソッド
    def main(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            #画面全体を白に
            SCREEN.fill(WHITE)
            #ステージを描画
            self.stage.draw(SCREEN)
            #プレイヤーを描画
            self.all_sprite.draw(SCREEN)
            #プレイヤーのupdateメソッド呼び出し
            self.all_sprite.update(self.stage.tile_list)
            
            #ゴール時の処理（テキスト描画）
            if self.player.goal:
                #draw_text('GOAL!', 100, WIDTH / 2, int(HEIGHT * 0.45), BLUE)
                goal_im = pg.image.load("ex06/meiro1/goal6.png").convert()
                rect_goal_im = goal_im.get_rect().move(180, 200)
                SCREEN.blit(goal_im, rect_goal_im)
                
            CLOCK.tick(FPS)
            pg.display.update()
        pg.quit()

game = Game()
game.main()