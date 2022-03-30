from tkinter import *
from random import shuffle
import math
words = []

with open('words.txt','r') as f:
    words = f.readlines()


class App:
    def __init__(self):
        self.corrects = 0
        self.wrongs = 0
        self.points = 0
        self.root = Tk()
        self.root.geometry('600x300')
        self.ent = Entry(self.root,width=600,font=('david',14))
        self.box = Listbox(self.root,bg='grey',width=600,font=('david',14))
        self.box.place(rely=0,relx=0)
        self.ent.place(relx=0,rely=0.9)
        self.seconds = 0
        self.time = Label(self.root,text=f'seconds: {self.seconds}')
        self.time.place(relx = 0.1,rely = 0.8)
        self.score = Label(self.root,text=f'WPM = {0}')
        self.score.place(relx=0.4,rely = 0.8)

    def addWords(self):
        # shuffle(words)
        for word in words:
            self.box.insert(0,word)
    
    def timer(self):
        self.time.config(text=f'seconds = {self.seconds}')
        self.seconds += 1 
        self.root.after(1000,self.timer)

    def wpm(self):
        self.score.config(text=
        f'WPM = {round(self.corrects / self.seconds * 60,2)}')
        self.root.after(100,self.wpm)




    def verifyWord(self):

        if ' ' in self.ent.get():

            written = self.ent.get().strip()
            if written == self.box.get(0).strip():
                self.points += 10
                self.root.config(bg='green')
                self.corrects += 1
            
            else:
                self.root.config(bg='red')
                self.wrongs += 1


            self.ent.delete(0,END)
            self.box.delete(0)
        

        self.root.after(50,self.verifyWord)
        

    
    def run(self):
        self.addWords()
        self.verifyWord()
        self.timer()
        self.wpm()
        self.root.mainloop()


aoo = App()
aoo.run()
