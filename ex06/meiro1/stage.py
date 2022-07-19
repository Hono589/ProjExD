from setting import *
import random

#ステージの設定
stage_data = []
SIZE_W = int(WIDTH / CHIP_SIZE)#CHIP_SIZE
SIZE_H = int(HEIGHT / CHIP_SIZE)

#始めにステージ全てを[0]にする
for y in range(SIZE_H):
    stage_data.append([0]*SIZE_W)
#周りの壁のみを[1]にする
for x in range(SIZE_W):
    stage_data[0][x] = 1
    stage_data[SIZE_H-1][x] = 1
for y in range(SIZE_H):
    stage_data[y][0] = 1
    stage_data[y][SIZE_W-1] = 1
    
#壁から２列毎に柱を立てる
for y in range(2, SIZE_W - 2, 2):
    for x in range(2, SIZE_H - 2, 2):
        stage_data[y][x] = 1

#柱から上下左右にランダムに柱を立てる。入れない通路ができないように
xp = [0, 1, 0, -1]
yp = [-1, 0, 1, 0]
for y in range(2, SIZE_H - 2, 2):
    for x in range(2, SIZE_W - 2, 2):
        d = random.randint(0, 3)
        if x > 2:
            d = random.randint(0, 2)
        stage_data[y + yp[d]][x + xp[d]] = 1

#ゴールを作る。ゴールの１マス左が壁ならゴールにたどりつけなくなるので壁か通路かの判定を行う。
goal = random.randint(1,SIZE_H-2)
if stage_data[goal][SIZE_W-2] == 0:
    stage_data[goal][SIZE_W-1] = 0
if stage_data[goal][SIZE_W-2] == 1:
    stage_data[goal][SIZE_W-2] = 0
    stage_data[goal][SIZE_W-1] = 0

#ステージの並びを確認（これはなくても良い。確認用のコード）
for stage in stage_data:
    print(stage)