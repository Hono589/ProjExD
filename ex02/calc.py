from logging import root
import tkinter as tk
import tkinter.messagebox as tkm


def button_click(event):
  btn = event.widget
  num = btn["text"]
  #tkm.showinfo("", f"{num}のボタンが押されました")
  if num == "=":
    e = entry.get()
    ans = eval(e)
    entry.delete(0, tk.END)
    entry.insert(tk.END, ans)
    #print(ans)
  else:
    entry.insert(tk.END, num)

#ボタンイベント
'''def make_click(ch):
  def click(e):
    print(ch)
    if ch == "=":
      calc(1)
      return
    elif ch == "AC":
      disp.delete(0, tk.END)'''

if __name__ == "__main__":
  root = tk.Tk()
  root.title("電卓")
  root.geometry("300x700")

  entry = tk.Entry(root, justify="right", width=10, font=("Times New Roman", 40))
  entry.grid(row=0, column=0, columnspan=80)

  r, c = 1, 0
  #numli = [9, 8, 7, 6, 5, 4, 3, 2, 1,0, "+"]
  for i, num in enumerate([9, 8, 7, 6, 5, 4, 3, 2, 1,0, "+", "-", "*", "/", "=", "C"]):
    btn = tk.Button(root,
                    text=f"{num}",
                    width=4,
                    height=3,
                    bg='#00FA9A',    #bgはエメラルドグリーン
                    fg='#2E8B22',    #fgは緑
                    font=("Times New Roman", 20),
                    #num{14} =  
                    )
    #btn.resizable()
    
    #btn = tk.Button(root, bg='#f0e68c', fg='#ff0000')

    btn.bind("<1>",button_click)
    btn.grid(row=r, column=c, padx=5, pady=4)
    c += 1
    if(i+1)%3 == 0:
        r += 1
        c = 0
  
#b = tk.Button(root, text="C")
    
    

  root.mainloop()