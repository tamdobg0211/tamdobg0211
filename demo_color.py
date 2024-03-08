from tkinter import *
from define import *
import os
root = Tk()                   #Tao doi tuong của 1 lớp

#Thiet lap chieu rong chieu cao
root.geometry("{}x{}+{}+{}".format(WINDOW_WIDTH,WINDOW_HEIGHT,WINDOW_POSITION_RIGHT,WINDOW_POSITION_DOWN))
#root.geometry( wide x height + right+down)


#Title
root.title("Change color")

root.mainloop()

