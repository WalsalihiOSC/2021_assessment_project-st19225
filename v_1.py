from tkinter import *
import random
from PIL import ImageTk, Image
from tkinter import messagebox
from operator import add, sub, mul


root = Tk()

class Interface:
    def __init__(self, wind):
        self.wind = wind
        self.notvalid = False
    def inter_face(self):
        self.menu = Frame(self.wind)
        self.menu .grid()
        #player Name 
        Label(self.menu, font=("Arial 17 bold"), text="Player Name: ").place(x=95,y=160)
        self.player_n=Entry(self.menu,font="Arial 14 bold")
        self.player_n.place(x=250,y=165,width=100,height=25)
        # age
        Label(self.menu, font=("Arial 17 bold"), text="Player age: ").place(x=100,y=210)
        self.player_a=Entry(self.menu,font="Arial 14 bold")
        self.player_a.place(x=250,y=215,width=100,height=25)
        #free space
        self.free_space()
        #title
        Label(self.menu ,text="Welcome to maths games ", font="Arial 30 bold").grid(row=0, column=2)
        #Level 1
        Button(self.menu ,text="Level 1",bg="cornflower blue",fg="black",activeforeground = "green",command=self.levels,font="Arial 14 bold",width=9,height=2).place(x=400 , y=130)
        #Level 2
        Button(self.menu ,text="Level 2",bg="#ffab40",fg="black",command =self.levels,font="Arial 14 bold",width=9,height=2).place(x=400 , y=198)
        #Level 3
        Button(self.menu ,text="Level 3",bg="red",fg="black",command =self.levels,font="Arial 14 bold",width=9,height=2).place(x=400 , y=268)
    #free_space
    def free_space(self):
            Label(self.menu,text="----",font="Arial 40 bold",fg="gray95").grid(column=1,row=0)
            Label(self.menu,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=1)
            Label(self.menu,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=2)
            Label(self.menu,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=3)
            Label(self.menu,text="----",font="Arial 50 bold",fg="gray95").grid(column=2,row=4)
            Label(self.menu,text="----",font="Arial 50 bold",fg="gray95").grid(column=3,row=4)
            Label(self.menu,text="----",font="Arial 50 bold",fg="gray95").grid(column=4,row=4)

    def levels(self):
        self.count = 1
        self.p_n = self.player_n.get().capitalize()
        self.p_a = self.player_a.get()
        if len(self.p_n) == 0 or len(self.p_a) == 0:
            self.notvalid = True
            messagebox.showerror("ERROR", "All boxes must be filled *")
        elif self.p_a not in ["6","7","8","9","10","11","12"]:
            self.notvalid = True
            messagebox.showerror("ERROR", "you must be 6-12 to play *")
        else:
            self.menu.grid_forget()
            self.level = Frame(self.wind)
            self.level.grid()
            self.notvalid = False
            for widget in self.level.winfo_children():
                widget.destroy()

            # level title
            Label(self.level,text="Welcome to Level 2", font="Arial 30 bold").grid(row=0, column=3)
            # problem
            self.question()
            #free space 
            self.free_space_1()
            #submet button 
            self.butt = Button(self.level ,text="Submit",bg="cornflower blue",fg="black" ,font="Arial 14 bold",width=9,height=2,command = lambda: self.checkb(self.problem))
            self.butt.place(x=510, y=300)

            #exit bitton
            Button(self.level ,text="New Game",bg="cornflower blue",fg="black",command =self.edit,font="Arial 14 bold",width=9,height=2).place(x=20, y=300)
    #free space 
    def free_space_1(self):
            Label(self.level,text="------",font="Arial 50 bold",fg="gray95").grid(column=1,row=4)
            Label(self.level,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=1)
            Label(self.level,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=2)
            Label(self.level,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=3)
            Label(self.level,text="----",font="Arial 50 bold",fg="gray95").grid(column=3,row=4)
            Label(self.level,text="--------",font="Arial 50 bold",fg="gray95").grid(column=4,row=4)

    def checkb(self,prob):
        self.count += 1
        if self.count ==10:
            self.butt.config(state=DISABLED)
            self.butt.unbind("<Button-1>")
            self.time = 10
            self.count=0
            def countdown():
                if self.time >= 0:
                    self.butt.destroy()
                    Button(self.level ,text="Exit",bg="cornflower blue",fg="black" ,font="Arial 14 bold",width=9,height=2,command = self.End_wind ).place(x=510, y=300)                     
                    self.time -= 1
                else:
                    global count
                    self.butt.config(state=NORMAL)
            countdown()
        ben = self.problem.get()
        if prob.get() == str(self.answer()):
            correct = Label(self.level, text="Correct!", fg="green")
            correct.place(x=350, y=250)
            self.question()
        elif len(ben) == 0:
            self.notvalid = True
            messagebox.showerror("ERROR", "All boxes must be filled *")
        else:
            wrong = Label(self.level, text="Wrong!", fg="red")
            wrong.place(x=350, y=280)
            self.question()

    def answer(self):
        return self.one + self.two
        
    def question(self):     
        self.ops = (self.add, self.sub, self.mul)
        self.op = random.choice(self.ops)
        self.x = random.randint(1,10)
        self.y = random.randint(1,10)
        if self.op == self.add:
        #question        
            Label (self.level, text="======",font="Arial 50 bold",fg="gray95").place(x= 150 , y = 140)
            question = Label(self.level, text=f"{self.one} + {self.two} =",font="Arial 40 bold")
            question.place(x= 165 , y = 145)
            #problem
            self.problem = Entry(self.level,font="Arial 30 bold")
            self.problem.place(x=400,y=160,width=90,height=40)
            #count
            Label (self.level, text=f"Q:({self.count}/10)",font="Arial 20 bold").grid(row=0 , column=1)
        
    def edit(self):
        self.level.destroy()
        self.menu.grid() 

    def End_wind(self):
        self.level.grid_forget()
        self.score = Frame(self.wind)
        self.score.grid()
        Label(self.score, text="You Score").grid(column=1 , row= 1)
        



root.title("OSC Course Selection")
root.geometry("650x380")
gui = Interface(root)
gui.inter_face()
root.mainloop()