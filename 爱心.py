import math
import random
import time
import tkinter as tk

hearts, all_wins = [], []
tips = ["我想你了"]
colors = ["pink"]

 #Edit [ Explain | Test | Document | Fix
def heart_points(n, screen_w, screen_h):
   # """"生成心形曲线上的n个屏幕坐标点"""
    points= []
    for i in range(n):
        t = i/n*2*math.pi
        x = 16*math.sin(t)**3
        y = (13*math.cos(t)-5*math.cos(2*t)-2*math.cos(3*t)-math.cos(4*t))
        sx = int(screen_w/2+x*20-50)
        sy = int(screen_h/2-y*20-80)
        sx = max(0, min(sx, screen_w-150))
        sy = max(0,min(sy, screen_h-60))
        points.append((sx, sy))
    return points
 #Edit|Explain|Test|Document|Fix
def create_popup(x, y, tip = None):
    #"""在指定位置创建一个弹窗"""
    win = tk.Toplevel()
    win.geometry(f"150x60+{int(x)}+{int(y)}")
    win.title("提示")
    win.attributes('-topmost', 1)
    text = tip if tip is not  None else random.choice(tips)
    bg = random.choice(colors)
    tk.Label(win, text=text, bg=bg, font = ("微软雅黑",14),width = 20, height = 3).pack()
    win.bind('<space>', lambda e: win.destroy())
    return win

#Edit|Explain|Test|IDocument|Fix
def main():
    root = tk.Tk()
    root.withdraw()
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    # ---阶段一：爱心统放---
    points = heart_points(100,sw,sh)
    for i,(x, y) in enumerate(points):
     tip = "我爱你" if i == len(points)-1 else None
     win = create_popup(x, y, tip)
     hearts.append(win)
     root.update()
     time.sleep(0.001)
     time.sleep(0.1)
    for w in hearts:
        if isinstance(w, tk.Toplevel) and w.winfo_exists():
            w.destroy()
    # ---阶段二：满屏暴击--
    count = sw // 150*sh//40+50
    for i in range(count):
         x = random.randint(0, sw - 150)
         y = random.randint(0, sh - 60)
         win = create_popup(x, y)
         all_wins.append(win)
         root.update()
         time.sleep(0.001)
    time.sleep(1)
    # --阶段三：优雅关闭--
    interval = 1.0 / len(all_wins) if all_wins else 0
    for win in all_wins:
        if isinstance(win, tk.Toplevel) and win.winfo_exists():
            win.destroy()
        root.update()
        time.sleep(interval)
    root.update()

if __name__== '__main__':
    main()