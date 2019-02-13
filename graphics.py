from tkinter import *
import matplotlib.pyplot as plt

cordsx = []
cordsy = []

def add():
    global x
    global y
    global cordsx
    global cordsy
    xx = float(x.get())
    yy = float(y.get())
    cordsx.append(xx)
    cordsy.append(yy)
    x.delete(0,END)
    y.delete(0,END)

def draw():
    global cordsx
    global cordsy
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(cordsx,cordsy)
    cordsx.clear()
    cordsy.clear()
    print(cordsx)
    print(cordsy)
    plt.show()


root = Tk()
root.title = "Graphics"
Label(text = "x:").pack()
x = Entry(justify = CENTER)
x.pack()
Label(text = "y:").pack()
y = Entry(justify = CENTER)
y.pack()
ad = Button(text = "Add", command = add).pack()
dr = Button(text = "Draw", command = draw).pack()
root.mainloop()
