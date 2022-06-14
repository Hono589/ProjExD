import random
import time

k = 5 # 最大繰り返し数
moji = 10# 対象文字数
son = 2 # 欠損文字数

def main():
  st = time.time()
  for i in range(moji):
    seikai = shutudai()
    f = kaitou(seikai)
    if f == 1:
      break
  #st = time.time()
  time.sleep(1)
  end = time.time()
  ti = end - st
  print(f"所要時間{ti}秒かかりました")

def shutudai():
  al = [chr(c+65) for c in range(26)]
  num = random.randint(al, moji)

  print(f"対象文字：{num}")

  li = random.randint(num, moji)
  print(f"欠損文字：{li}")

  hyouji = [c for c in al if c not in li]
  print(f"表示文字：{hyouji}")


def kaitou(seikai):
  n = int(input("欠損文字はいくつあるでしょうか？"))
  if n != moji:
    print("不正解です。")
    return 0

  else:
    print("正解です。それでは欠損文字を1文字ずつ入力してください")
    for i in range(moji):
      c = input(f"{i+1}つ目の文字を入力してください")
      if c not in seikai:
        print("不正解です。またチャレンジしてください")
      seikai.remove(c)
    print("正解です。")
    return 1

if __name__ == "__main__":
  main()