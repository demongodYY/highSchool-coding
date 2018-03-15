import tkinter
import random
import time
from tkinter import messagebox 

tk = tkinter.Tk()
tk.title("Game")
tk.wm_attributes("-topmost", 1)
canvas = tkinter.Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

class Ball():
    def __init__(self, canvas, paddle, color,):
        self.canvas = canvas
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id, 245, 100)
        starts=[-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.paddle = paddle
        self.hit_bottom = False
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        else:
            return False
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= 400:
            self.hit_bottom = True
        if pos[0] <= 0:
            self.x = 1
        if pos[2] >= 500:
            self.x = -1
        if self.hit_paddle(pos) == True:
            self. y = -3
class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 150, 10, fill=color)
        self.canvas.move(self.id, 200, 350)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        
    def turn_left(self, evt):
        self.x = -2
    def turn_right(self, evt):
        self.x = 2
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos  = self.canvas.coords(self.id)
        if pos[0] <=0 or self.canvas_width:
            self.x = 0

paddle =  Paddle(canvas, "blue")
ball = Ball(canvas, paddle, "red")

while True:
    if ball.hit_bottom == True:
        messagebox.showinfo('你输了！',' 游戏结束')
        break
    ball.draw()
    paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)