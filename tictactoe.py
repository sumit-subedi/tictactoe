from tkinter import *;
import array as arr
import result

root = Tk()
root.geometry("500x300")
f = Frame(root)
f.place(relheight=1, relwidth=1)



class buttons:

    def __init__(self):
        global list
        list =  [0, 0, 0, 0, 0, 0, 0, 0, 0]
        global f
        global all
        f.destroy()
        f = Frame(root, bg="black")
        f.place(relheight=1, relwidth=1)

        b5 = Button(f, text="b5", bg="white", command=lambda: buttons.pressed(b5, 5))
        b5.place(relx=0.4, rely=0.4, relheight=0.2, relwidth=0.2)
        b6 = Button(f, text="b6", bg="white", command=lambda: buttons.pressed(b6, 6))
        b6.place(relx=0.6, rely=0.4, relheight=0.2, relwidth=0.2)
        b4 = Button(f, text="b4", bg="white", command=lambda: buttons.pressed(b4, 4))
        b4.place(relx=0.2, rely=0.4, relheight=0.2, relwidth=0.2)
        b2 = Button(f, text="b2", bg="white", command=lambda: buttons.pressed(b2, 2))
        b2.place(relx=0.4, rely=0.2, relheight=0.2, relwidth=0.2)
        b8 = Button(f, text="b8", bg="white", command=lambda: buttons.pressed(b8, 8))
        b8.place(relx=0.4, rely=0.6, relheight=0.2, relwidth=0.2)
        b1 = Button(f, text="b1", bg="white", command=lambda: buttons.pressed(b1, 1))
        b1.place(relx=0.2, rely=0.2, relheight=0.2, relwidth=0.2)
        b3 = Button(f, text="b3", bg="white", command=lambda: buttons.pressed(b3, 3))
        b3.place(relx=0.6, rely=0.2, relheight=0.2, relwidth=0.2)
        b9 = Button(f, text="b9", bg="white", command=lambda: buttons.pressed(b9, 9))
        b9.place(relx=0.6, rely=0.6, relheight=0.2, relwidth=0.2)
        b7 = Button(f, text="b7", bg="white", command=lambda: buttons.pressed(b7, 7))
        b7.place(relx=0.2, rely=0.6, relheight=0.2, relwidth=0.2)

        all = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

    def pressed(self, n):
        global list

        if (list[n - 1] == 0):
            self.config(text="X", font=("", 25))
            list[n - 1] = 1
        else: return

        j = result.checkresult(list)
        if (j == 1 ):
            l1 = Label(f, text="You won the game")
            endscreen(l1)
            return
        if (0 not in list):
            l1=Label(f,text="Game Draw")
            endscreen(l1)
        buttons.compressed(self)

    def compressed(self):
        global all
        global list
        k=result.nextpos(list)
        all[k].config(text="O",font=("",25))
        list[k]=2
        j = result.checkresult(list)
        if (j == 1):
            l1=Label(f,text="Computer won the game")

            endscreen(l1)
        return



def endscreen(l1):
    l1.place(relx=0,rely=0.8)
    l3=Button(f,text="Play Again",command=lambda:buttons())
    l3.place(relx=0.3,rely=0.9)
    l2=Button(f,text="quit",command=lambda:sys.exit())
    l2.place(relx=0.6,rely=0.9)

b1 = Button(f, text="1 Player", bg="red", command=lambda: buttons())
b1.place(relx=0.1, rely=0.4, relheight=0.2, relwidth=0.2)
b2 = Button(f, text="2 Player", bg="green")
#b2.place(relx=0.6, rely=0.4, relheight=0.2, relwidth=0.2)

root.mainloop()