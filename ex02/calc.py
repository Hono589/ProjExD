from logging import root
import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
  btn = event.widget
  num = btn["text"]
  #tkm.showinfo("", f"{num}のボタンが押されました")
  entry.insert(tk.END, "hoge")

if __name__ == "__main__":
  root = tk.Tk()
  root.title("電卓")
  root.geometry("300x700")

  entry = tk.Entry(root, justify="right", width=10, font=("Times New Roman", 40))
  entry.grid(row=0, column=0, columnspan=3)

  r, c = 1, 0
  #numli = [9, 8, 7, 6, 5, 4, 3, 2, 1,0, "+"]
  for i num in enumerate([9, 8, 7, 6, 5, 4, 3, 2, 1,0, "+"]):
    btn = tk.Button(root,
                    text=f"{num}",
                    width=4,
                    height=2,
                    font=("Times New Roman", 30)
                    )
    
    btn.bind("<1>",button_click)
    btn.grid(row=r, column=c)
    c += 1
    if(i-1)%3 == 0:
        r += 1
        c = 0
    
    

  root.mainloop()