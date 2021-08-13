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
    # menu frame
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
        Button(self.menu ,text="Level 1",bg="cornflower blue",fg="black",activeforeground = "green",command=self.level_1,font="Arial 14 bold",width=9,height=2).place(x=400 , y=130)
        #Level 2
        Button(self.menu ,text="Level 2",bg="#ffab40",fg="black",command =self.level_2,font="Arial 14 bold",width=9,height=2).place(x=400 , y=198)
        #Level 3
        Button(self.menu ,text="Level 3",bg="red",fg="black",command =self.level_3,font="Arial 14 bold",width=9,height=2).place(x=400 , y=268)
    #free_space
    def free_space(self):
            Label(self.menu,text="----",font="Arial 40 bold",fg="gray95").grid(column=1,row=0)
            Label(self.menu,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=1)
            Label(self.menu,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=2)
            Label(self.menu,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=3)
            Label(self.menu,text="----",font="Arial 50 bold",fg="gray95").grid(column=2,row=4)
            Label(self.menu,text="----",font="Arial 50 bold",fg="gray95").grid(column=3,row=4)
            Label(self.menu,text="----",font="Arial 50 bold",fg="gray95").grid(column=4,row=4)
    #level 1
    def level_1(self):
        self.z = (1,2,3,4,5)
        self.w = (6,7,8,9,10)
        self.lev = 1
        self.levels()
    #level 2
    def level_2(self):
        self.z = (11,12,13,14,15)
        self.w = (16,17,18,19,20)
        self.lev = 2
        self.levels()
    #level 3
    def level_3(self):
        self.z = (21,22,23,24,25)
        self.w = (26,27,28,29,30)
        self.lev = 3
        self.levels()
    #level one frame 
    def levels(self):
        self.scoer_count = 0
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
            Label(self.level,text=f"Welcome to Level {self.lev}", font="Arial 30 bold").grid(row=0, column=3)
            # problem
            self.question()
            #free space 
            self.free_space_1()
            #submet button 
            self.butt = Button(self.level ,text="Submit",bg="cornflower blue",fg="black" ,font="Arial 14 bold",width=9,height=2,command = lambda: self.submet(self.problem))
            self.butt.place(x=510, y=300)
            #exit bitton
            Button(self.level ,text="New Game",bg="cornflower blue",fg="black",command =self.NEW_game,font="Arial 14 bold",width=9,height=2).place(x=20, y=300)
    #free space 
    def free_space_1(self):
            Label(self.level,text="------",font="Arial 50 bold",fg="gray95").grid(column=1,row=4)
            Label(self.level,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=1)
            Label(self.level,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=2)
            Label(self.level,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=3)
            Label(self.level,text="----",font="Arial 50 bold",fg="gray95").grid(column=3,row=4)
            Label(self.level,text="--------",font="Arial 50 bold",fg="gray95").grid(column=4,row=4)
    # Submit
    def submet(self,prob):
        ben = self.problem.get()
        # input == answer
        if prob.get() == str(self.answer()):
            correct = Label(self.level, text="Correct!", fg="green")
            correct.place(x=400, y=250)
            self.scoer_count += 1 
            self.count += 1
            self.question()
        # input == 0 
        elif len(ben) == 0:
            self.notvalid = True
            messagebox.showerror("ERROR", "All boxes must be filled *")
        else:
            wrong = Label(self.level, text="Wrong!", fg="red")
            wrong.place(x=350, y=280)
            self.count += 1
            self.question()
        # button == 10 times 
        if self.count ==11:
            self.butt.config(state=DISABLED)
            self.butt.unbind("<Button-1>")
            self.time = 11
            self.count=0
            def countdown():
                if self.time >= 0:
                    Label (self.level, text="======",font="Arial 50 bold",fg="gray95").place(x= 150 , y = 140)
                    Label(self.level, text=f"End of Game ",font="Arial 40 bold") .place(x= 165 , y = 145)
                    Label (self.level, text ="=======",font="Arial 20 bold",fg="gray95").grid(row=0 , column=1)
                    Button(self.level ,text="Exit",bg="cornflower blue",fg="black" ,font="Arial 14 bold",width=9,height=2,command = self.End_wind ).place(x=510, y=300)
                    self.time -= 1
                else:
                    global count
                    self.butt.config(state=NORMAL)
            countdown()
    # answer
    def answer(self):
        return self.answer_1
    # question 
    def question(self):     
        self.x = random.choice(self.z)
        self.y = random.choice(self.w)
        ops = (add, sub, mul)
        op = random.choice(ops)
        if op == add:
            Label (self.level, text="======",font="Arial 50 bold",fg="gray95").place(x= 150 , y = 140)
            question = Label(self.level, text=f"{self.x} + {self.y} =",font="Arial 40 bold")
            question.place(x= 165 , y = 145)
            #problem
            self.problem = Entry(self.level,font="Arial 30 bold")
            self.problem.place(x=400,y=160,width=90,height=40)
            #count
            Label (self.level, text=f"Q:({self.count}/10)",font="Arial 20 bold").grid(row=0 , column=1)
            self.answer_1 = self.x + self.y

        elif op == sub:
            Label (self.level, text="======",font="Arial 50 bold",fg="gray95").place(x= 150 , y = 140)
            question = Label(self.level, text=f"{self.y} - {self.x} =",font="Arial 40 bold")
            question.place(x= 165 , y = 145)
            #problem
            self.problem = Entry(self.level,font="Arial 30 bold")
            self.problem.place(x=400,y=160,width=90,height=40)
            #count
            Label (self.level, text=f"Q:({self.count}/10)",font="Arial 20 bold").grid(row=0 , column=1)
            self.answer_1 = self.y - self.x

        elif op == mul:
            Label (self.level, text="======",font="Arial 50 bold",fg="gray95").place(x= 150 , y = 140)
            question = Label(self.level, text=f"{self.y} x {self.x} =",font="Arial 40 bold")
            question.place(x= 165 , y = 145)
            #problem
            self.problem = Entry(self.level,font="Arial 30 bold")
            self.problem.place(x=400,y=160,width=90,height=40)
            #count
            Label (self.level, text=f"Q:({self.count}/10)",font="Arial 20 bold").grid(row=0 , column=1)
            self.answer_1 = self.y * self.x
    # New_button 
    def NEW_game(self):
        self.level.destroy()
        self.menu.grid() 
    # End wind frame 
    def End_wind(self):
        self.level.destroy()
        self.score = Frame(self.wind)
        self.score.grid()
        self.free_space_2()
        Label(self.score, text="You Score",font="Arial 30 bold").grid(column=3 , row= 0)
        Label(self.score, text=str(self.scoer_count),font="Arial 30 bold").grid(column=3 , row= 1)
        Button(self.score ,text="New Game",bg="cornflower blue",fg="black",command =self.NEW_game ,font="Arial 14 bold",width=9,height=2).place(x=20, y=300)
        Button(self.score ,text="New Player",bg="cornflower blue",fg="black",command =self.bat ,font="Arial 14 bold",width=9,height=2).place(x=20, y=200)
        Button(self.score ,text="Exit",bg="cornflower blue",fg="black" ,font="Arial 14 bold",width=9,height=2,command = self.quit ).place(x=510, y=300)


    def free_space_2(self):
                Label(self.score,text="---------",font="Arial 50 bold",fg="gray95").grid(column=1,row=4)
                Label(self.score,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=1)
                Label(self.score,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=2)
                Label(self.score,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=3)
                Label(self.score,text="----",font="Arial 50 bold",fg="gray95").grid(column=3,row=4)
                Label(self.score,text="----------",font="Arial 50 bold",fg="gray95").grid(column=4,row=4)
    def bat(self):
        self.score.destroy()
        self.level.destroy()
        self.menu.grid() 
    def quit(self):
        self.wind.destroy()
    def bat(self):
        self.score.destroy()
        self.inter_face()

root.title("OSC Course Selection")
root.geometry("650x380")
gui = Interface(root)
gui.inter_face()
root.mainloop()