import tkinter as tk
import maze_maker as mm

def key_down(event):
  global key
  key = event.keysym
  #print(f"{key}キーが押されました")

def key_up(event):
 global key
 key = ""

def main_proc():
  global cx, cy, mx, my

  d = {  # キー：押されているキーkey/値:
    #"": [0, 0],
    "Up":[0, -1],
    "Down": [0, +1],
    "Left": [-1, 0],
    "Right": [+1, 0],
      }
  
  try:
    if maze_bg[ my+d[key][1]][mx+d[key][0]] == 0: # もし移動先が床ならば
      my, mx =  my+d[key][1], mx+d[key][0]
  except:
    pass


  cx, cy = mx*100+50, my*100+50
  #cx, cy = cx+d[key][0], cy+d[key][1]
  canvas.coords("photo", cx, cy)
  root.after(100, main_proc)

# ゴールするまで移動させる関数の定義
'''def goal_maze(pi):
  s = 0   # スタート地点
  state_history = [0]

  while (1): # ゴールするまでループ
    next_s = get_next_s(pi, s)
    state_history.append(next_s)

    if next_s == 8:
      break
    else:
      s = next_s'''

if __name__ == "__main__":
  root = tk.Tk()
  root.title("迷えるトラさん")
  
  canvas = tk.Canvas(root, width=1500, height=900, bg="black") #windowの大きさと色
  canvas.pack()

  maze_bg = mm.make_maze(15, 9) # 1:壁 0:床 を表す二次元リスト
  #print(maze_bg)
  mm.show_maze(canvas, maze_bg)# 

  photo = tk.PhotoImage(file="fig/トラさん.png")
  photo = photo.zoom(8)  #画像のサイズを変更
  photo = photo.subsample(32)  #もともとの画像の大きさ
  mx, my = 1, 1
  cx, cy = mx*100+50, my*100+50
  #cx, cy = 300, 400
  canvas.create_image(cx, cy, image=photo, tag="photo")

  key = ""

  root.bind("<KeyPress>", key_down) #ボタン押された時のもの
  root.bind("<KeyRelease>", key_up)

  main_proc()
  

  root.mainloop()