from tkinter import *
import functools
import random
root = Tk()
button = {}
root.title('BINGO')
#root.iconbitmap(r'E:\Projects\BINGO\main folder\image.ico')
class bingo:

    bingoIndex = 1

    def columnSame(self, c):
        Button(root, height=5, width=10, text='|\nV', state = DISABLED).grid(row=0, column=c)
        bingoStr = 'BINGO'
        Label(root, text = bingoStr[:bingo.bingoIndex]).grid(row = 6, column = 3)
        for columnSameIndex in range(1,6):
            Button(root, height = 5, width = 10, bg = 'green').grid(row = columnSameIndex, column=c)
        bingo.bingoIndex += 1

    def rowSame(self, r):
        Button(root, height=5, width=10, text='->', state = DISABLED).grid(row=r, column=0)
        bingoStr = 'BINGO'
        Label(root, text = bingoStr[:bingo.bingoIndex]).grid(row = 6, column = 3)
        for rowSameIndex in range(1,6):
            Button(root, height = 5, width = 10, bg = 'green').grid(row = r, column=rowSameIndex)
        bingo.bingoIndex += 1
    def upLeft_lowRight(self):
        button['00'] = Button(root, height=5, width=10, text='X', state = DISABLED).grid(row=0, column=0)
        bingoStr = 'BINGO'
        Label(root, text = bingoStr[:bingo.bingoIndex]).grid(row = 6, column = 3)
        for crossIndex in range(1,6):
            Button(root, height = 5, width = 10, bg = 'green').grid(row = crossIndex, column=crossIndex)
        bingo.bingoIndex += 1
    def lowLeft_upRight(self):
        button['60'] = Button(root, height=5, width=10, text='X', state = DISABLED).grid(row=6, column=0)
        bingoStr = 'BINGO'
        Label(root, text = bingoStr[:bingo.bingoIndex]).grid(row = 6, column = 3)
        for crossIndex in range(1,6):
            Button(root, height = 5, width = 10, bg = 'green').grid(row = crossIndex, column=6-crossIndex)
        bingo.bingoIndex += 1

class main:

    def clicked(self, r, c):
        Button(root, height = 5, width =10, bg = 'red').grid(row = r, column=c)

    def __init__(self):
        ## upper left to lower right
        button['00'] = Button(root, height=5, width=10, text='X', command = functools.partial(self.call_upLeft_lowRight)).grid(row=0, column=0)
        ## lower left to upper right
        button['60'] = Button(root, height=5, width=10, text='X', command = functools.partial(self.call_lowLeft_upRight)).grid(row=6, column=0)
        ## column arrows
        button['01'] = Button(root, height=5, width=10, text='|\nV', command = functools.partial(self.call_columnSame, 1)).grid(row=0, column=1)
        button['02'] = Button(root, height=5, width=10, text='|\nV', command = functools.partial(self.call_columnSame, 2)).grid(row=0, column=2)
        button['03'] = Button(root, height=5, width=10, text='|\nV', command = functools.partial(self.call_columnSame, 3)).grid(row=0, column=3)
        button['04'] = Button(root, height=5, width=10, text='|\nV', command = functools.partial(self.call_columnSame, 4)).grid(row=0, column=4)
        button['05'] = Button(root, height=5, width=10, text='|\nV', command = functools.partial(self.call_columnSame, 5)).grid(row=0, column=5)

        ## row arrows
        button['10'] = Button(root, height=5, width=10, text='->', command = functools.partial(self.call_rowSame, 1)).grid(row=1, column=0)
        button['20'] = Button(root, height=5, width=10, text='->', command = functools.partial(self.call_rowSame, 2)).grid(row=2, column=0)
        button['30'] = Button(root, height=5, width=10, text='->', command = functools.partial(self.call_rowSame, 3)).grid(row=3, column=0)
        button['40'] = Button(root, height=5, width=10, text='->', command = functools.partial(self.call_rowSame, 4)).grid(row=4, column=0)
        button['50'] = Button(root, height=5, width=10, text='->', command = functools.partial(self.call_rowSame, 5)).grid(row=5, column=0)

        l = list(range(1, 26))
        lst = random.sample(l, len(l))
        i = 0
        for rowNumber in range(1, 6):
            for colNumber in range(1, 6):
                button[str(rowNumber) + str(colNumber)] = Button(root, height=5, width=10, text=lst[i], fg='red',  bg='yellow',
                                                        command = functools.partial(self.clicked, rowNumber, colNumber)).grid(row=rowNumber, column=colNumber)
                i = i + 1
    def call_upLeft_lowRight(self):
        bingo.upLeft_lowRight(self)

    def call_lowLeft_upRight(self):
        bingo.lowLeft_upRight(self)

    def call_columnSame(self, c):
        bingo.columnSame(self, c)

    def call_rowSame(self, r):
        bingo.rowSame(self, r)


main()
root.mainloop()
