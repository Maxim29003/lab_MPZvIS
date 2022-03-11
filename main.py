from threading import Thread
from time import sleep
from tkinter import *
from tkinter.ttk import Progressbar
import os

stopThread = False
startThread = False


def process(pb, max_value, time):
    pb.configure(maximum=max_value)
    for i in range(max_value + 1):
        pb.configure(value=i)
        sleep(time)
        pb.update()
        while stopThread:
            pass


def start():
    global startThread
    global stopThread

    if stopThread:
        stopThread = False
    if not startThread:
        th1 = Thread(target=process, args=(pb1, 120, 0.03))
        th1.start()
        th2 = Thread(target=process, args=(pb2, 100, 0.05))
        th2.start()

    startThread = True


def stop():
    global stopThread
    stopThread = True


w1 = Tk()
w1.title(" Потоки ")
w1.geometry("250x150")
w1.resizable(False, False)

# кнопка Старт
btn1 = Button(w1, text="Старт", command=start)
btn1.place(x=190, y=20, width=55, height=22)

# кнопка Стоп
btn2 = Button(w1, text="Стоп", command=stop)
btn2.place(x=190, y=47, width=55, height=22)

# кнопка Закрыть
btn3 = Button(w1, text="Закрыть", command=w1.destroy)
btn3.place(x=190, y=74, width=55, height=22)

# Метки
lbl1 = Label(w1, text="Поток №1")
lbl1.place(x=15, y=5)
lbl2 = Label(w1, text="Поток №2")
lbl2.place(x=15, y=54)

# Прогрессбар
pb1 = Progressbar(w1, orient=HORIZONTAL, mode="determinate")
pb1.place(x=15, y=30, width=150, height=22)
pb2 = Progressbar(w1, orient=HORIZONTAL, mode="determinate")
pb2.place(x=15, y=74, width=150, height=22)

w1.mainloop()
os.abort()