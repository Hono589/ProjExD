import random

def main():
  sei = shutudai()
  kai(sei)

def shutudai():
  qu = [
      {"q":"サザエの旦那の名前は？", "a":["マスオ", "ますお"]},
      {"q":"カツオの妹の名前は？","a":["ワカメ", "わかめ"]},
      {"q":"タラオはカツオから見てどんな関係？", "a": ["甥", "おい", "甥っ子", "おいっこ"]}
      ]
  print("問題：")
  ra = random.randint(0, 2)
  print(qu[ra]["q"])
  return qu[ra]["a"]


  def kaitou(sei):
    a = input("答えてください")
    if a in sei:
      print("正解だよ！！！")
    else:
      print("不正解！！！")

  if __name__=="__main__":
    main()