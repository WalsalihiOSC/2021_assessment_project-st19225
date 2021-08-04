from tkinter import *
import random
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()

class Interface:
    def __init__(self, wind):
        self.wind = wind
        self.notvalid = False
    def inter_face(self):
        self.manu = Frame(self.wind)
        self.manu .grid()
        #player Name 
        Label(self.manu, font=("Arial 17 bold"), text="Player Name: ").place(x=95,y=160)
        self.player_n=Entry(self.manu,font="Arial 14 bold")
        self.player_n.place(x=250,y=165,width=100,height=25)
        # age
        Label(self.manu, font=("Arial 17 bold"), text="Player age: ").place(x=100,y=210)
        self.player_a=Entry(self.manu,font="Arial 14 bold")
        self.player_a.place(x=250,y=215,width=100,height=25)
        #free space
        self.free_space()
        #title
        Label(self.manu ,text="Welcome to maths games ", font="Arial 30 bold").grid(row=0, column=2)
        #Level 1
        Button(self.manu ,text="Level 1",bg="cornflower blue",fg="black",activeforeground = "green",command=self.levels,font="Arial 14 bold",width=9,height=2).place(x=400 , y=130)
        #Level 2
        Button(self.manu ,text="Level 2",bg="#ffab40",fg="black",command =self.levels,font="Arial 14 bold",width=9,height=2).place(x=400 , y=198)
        #Level 3
        Button(self.manu ,text="Level 3",bg="red",fg="black",command =self.levels,font="Arial 14 bold",width=9,height=2).place(x=400 , y=268)
    #free_space
    def free_space(self):
            Label(self.manu,text="----",font="Arial 40 bold",fg="gray95").grid(column=1,row=0)
            Label(self.manu,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=1)
            Label(self.manu,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=2)
            Label(self.manu,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=3)
            Label(self.manu,text="----",font="Arial 50 bold",fg="gray95").grid(column=2,row=4)
            Label(self.manu,text="----",font="Arial 50 bold",fg="gray95").grid(column=3,row=4)
            Label(self.manu,text="----",font="Arial 50 bold",fg="gray95").grid(column=4,row=4)


    def levels(self):
        

        self.p_n = self.player_n.get().capitalize()
        self.p_a = self.player_a.get()
        if len(self.p_n) == 0 or len(self.p_a) == 0:
            self.notvalid = True
            messagebox.showerror("ERROR", "All boxes must be filled *")
        elif self.p_a not in ["6","7","8","9","10","11","12"]:
            self.notvalid = True
            messagebox.showerror("ERROR", "you must be 6-12 to play *")
        else:
            self.manu.grid_forget()
            self.level = Frame(self.wind)
            self.level.grid()
            self.notvalid = False
            for widget in self.level.winfo_children():
                widget.destroy()

            # level title
            Label(self.level,text="Welcome to Level 2", font="Arial 30 bold").grid(row=0, column=2)
            # problem
            self.question_win()
            global problem
            problem = Entry(self.level,font="Arial 30 bold")
            problem.place(x=400,y=180,width=90,height=40)
            #free space 
            self.free_space_1()
            #submet button 

            Button(self.level ,text="Submit",bg="cornflower blue",fg="black",command = self.checkb,font="Arial 14 bold",width=9,height=2).place(x=400, y=280)
            #exit bitton
            Button(self.level ,text="Exit",bg="cornflower blue",fg="black",command =self.End_wind,font="Arial 14 bold",width=9,height=2).place(x=50, y=280)

    def free_space_1(self):
            Label(self.level,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=0)
            Label(self.level,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=1)
            Label(self.level,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=2)
            Label(self.level,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=3)
            Label(self.level,text="----",font="Arial 50 bold",fg="gray95").grid(column=2,row=4)
            Label(self.level,text="----",font="Arial 50 bold",fg="gray95").grid(column=3,row=4)
    
    def checkb(self):

        var1 = problem
        answer = self.one + self.two
    
        if var1 != answer:
            correct = Label(self.level, text="Correct!", fg="green")
            correct.place(x=350, y=280)
            self.question_win()

        else:
            wrong = Label(self.level, text="Wrong!", fg="red")
            wrong.place(x=350, y=280)

    def question_win(self):
        self.one = random.randrange(1,20)
        self.two = random.randrange(1,20)
        
        question = Label(self.level, text=f"{self.one} + {self.two} =",font="Arial 40 bold")
        question.place(x= 200 , y = 160)


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