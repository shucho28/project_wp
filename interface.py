from tkinter import *

win = Tk()
win.overrideredirect(True)
win_width = win.winfo_screenwidth()
win_height = win.winfo_screenheight()
win.geometry(str(win_width)+'x'+str(win_height))

game_width = win_width/6
game_height = win_height/6
game_frame = Frame(win,width=game_width,height=game_height,bg='blue')
game_frame.grid(row=0,column=0)

win.mainloop()
