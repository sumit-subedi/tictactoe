#### Conclusion
# first of all congrats on completing this project. :D
# it seems to work for the most part. Sometimes, the CPU wins but the game doesn't seem to catch that and lets me continue playing

#### Resource for better coding style
# also check out PEP 8. https://www.python.org/dev/peps/pep-0008/
# I made changes throughout the app to showcase the difference between our two styles. Imagine this being a component to a larger project and try to see how
#       the syle changes I made might help new people who are seeing the project for the first time understand the code better
# PEP 8 isn't required but is followed by most python programmers. Feel free to make changes though for personal projects that fit your style
#       but always remember the zen of python:
"""
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

"""
# don't take my word as gospel, as I am also learning. Try to take in all the points I made and decide for yourself if you find yourself agreeing with me or not
# Also, don't accept this pull request but instead use this as jumping off point to make your code better :D
import tkinter as tk # explicit is better than implicit here. and also things like Button and Label might be used elsewhere (very common names)
import array as arr
import result
import sys

root = tk.Tk()
root.geometry("500x300")
f = tk.Frame(root)
f.place(relheight=1, relwidth=1)


# 1. class names are generally started with uppercase
# 2. classes usually work as abstractions on real world things. The name buttons here is not really indicitive of what the class represents
## Board or TicTacToeBoard might be a better name, that you can use in this context
# 3. This does really gain anything by being a class. You even use it as a callable and keep it anonymous
##  (so you can use this as a function and nothing would really change). In general, a class will
##  will have state and functionality relating to said state. in this case you have no state and the functions are working with global variables
##  here's a challenge, try to remove global variables and make it instead member variables of the class. Then try to get it to work
class TicTacToeBoard:

    def __init__(self):
        global list # 4. In general globals are bad form. Not an issue in this context, but see if you can figure out a way to do this without using a global
        list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        global f
        global all
        f.destroy()
        f = tk.Frame(root, bg="black")
        f.place(relheight=1, relwidth=1)
        # 4. DRY: Don't repeat yourself, maybe you can use constants for the data since a lot of seems to be repeated
        ## Also maybe you can use a data structure and for loop to generate the board.
        ##  And then you can challenge yourself. Allow the player to decide if they want to play a 3x3 game or a of 5x5 or 7x7
        ##  of course the number of boxes you need in a row will change so some extra checking will be required in result.py
        b5 = tk.Button(f, text="b5", bg="white", command=lambda: TicTacToeBoard.pressed(b5, 5))
        b5.place(relx=0.4, rely=0.4, relheight=0.2, relwidth=0.2)
        b6 = tk.Button(f, text="b6", bg="white", command=lambda: TicTacToeBoard.pressed(b6, 6))
        b6.place(relx=0.6, rely=0.4, relheight=0.2, relwidth=0.2)
        b4 = tk.Button(f, text="b4", bg="white", command=lambda: TicTacToeBoard.pressed(b4, 4))
        b4.place(relx=0.2, rely=0.4, relheight=0.2, relwidth=0.2)
        b2 = tk.Button(f, text="b2", bg="white", command=lambda: TicTacToeBoard.pressed(b2, 2))
        b2.place(relx=0.4, rely=0.2, relheight=0.2, relwidth=0.2)
        b8 = tk.Button(f, text="b8", bg="white", command=lambda: TicTacToeBoard.pressed(b8, 8))
        b8.place(relx=0.4, rely=0.6, relheight=0.2, relwidth=0.2)
        b1 = tk.Button(f, text="b1", bg="white", command=lambda: TicTacToeBoard.pressed(b1, 1))
        b1.place(relx=0.2, rely=0.2, relheight=0.2, relwidth=0.2)
        b3 = tk.Button(f, text="b3", bg="white", command=lambda: TicTacToeBoard.pressed(b3, 3))
        b3.place(relx=0.6, rely=0.2, relheight=0.2, relwidth=0.2)
        b9 = tk.Button(f, text="b9", bg="white", command=lambda: TicTacToeBoard.pressed(b9, 9))
        b9.place(relx=0.6, rely=0.6, relheight=0.2, relwidth=0.2)
        b7 = tk.Button(f, text="b7", bg="white", command=lambda: TicTacToeBoard.pressed(b7, 7))
        b7.place(relx=0.2, rely=0.6, relheight=0.2, relwidth=0.2)

        all = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

    def pressed(self, n):
        global list

        if (list[n - 1] == 0):
            self.config(text="X", font=("", 25))
            list[n - 1] = 1
        else:
            return

        j = result.checkresult(list)
        if (j == 1):
            l1 = tk.Label(f, text="You won the game")
            endscreen(l1)
            return
        if (0 not in list):
            l1= tk.Label(f, text="Game Draw")
            endscreen(l1)
        TicTacToeBoard.compressed(self)

    def compressed(self):
        global all
        global list
        k = result.nextpos(list)
        all[k].config(text="O", font=("",25))
        list[k] = 2
        j = result.checkresult(list)
        if (j == 1):
            l1 = tk.Label(f, text="Computer won the game")

            endscreen(l1)
        return


def endscreen(l1):
    l1.place(relx=0, rely=0.8)
    l3 = tk.Button(f, text="Play Again", command=lambda: TicTacToeBoard())
    l3.place(relx=0.3, rely=0.9)
    l2 = tk.Button(f, text="quit", command=lambda: sys.exit())
    l2.place(relx=0.6, rely=0.9)


b1 = tk.Button(f, text="1 Player", bg="red", command=lambda: TicTacToeBoard())
b1.place(relx=0.1, rely=0.4, relheight=0.2, relwidth=0.2)
b2 = tk.Button(f, text="2 Player", bg="green")
#b2.place(relx=0.6, rely=0.4, relheight=0.2, relwidth=0.2)

root.mainloop()
