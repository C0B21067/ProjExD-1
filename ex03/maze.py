import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")#演習1

    canv = tk.Canvas(width = 1500,height = 900, bg = "black")#演習2
    canv.pack()

    tori = tk.PhotoImage(file = "fig/7.png")
    cx, cy = 300, 400
    canv.create_image(cx, cy, image = tori, tag = "tori")#演習3

    key = ""#演習4

    root.mainloop()