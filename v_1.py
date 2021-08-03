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
        Label(self.manu, font=("Arial 17 bold"), text="Player Name ").place(x=200,y=100)
        self.player_n=Entry(self.manu,font="Arial 14 bold")
        self.player_n.place(x=350,y=105,width=100,height=25)
        #free space
        self.free_space()
        #title
        Label(self.manu ,text="Welcome to maths games ", font="Arial 30 bold").grid(row=0, column=2)
        #Level 1
        Button(self.manu ,text="Level 1",bg="cornflower blue",fg="black",activeforeground = "green",command=self.levels,font="Arial 14 bold",width=9,height=2).place(x=300 , y=160)
        #Level 2
        Button(self.manu ,text="Level 2",bg="#ffab40",fg="black",command =self.levels,font="Arial 14 bold",width=9,height=2).place(x=300 , y=228)
        #Level 3
        Button(self.manu ,text="Level 3",bg="red",fg="black",command =self.levels,font="Arial 14 bold",width=9,height=2).place(x=300 , y=298)
    #free_space
    def free_space(self):
            Label(self.manu,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=0)
            Label(self.manu,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=1)
            Label(self.manu,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=2)
            Label(self.manu,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=3)
            Label(self.manu,text="----",font="Arial 50 bold",fg="gray95").grid(column=2,row=4)
            Label(self.manu,text="----",font="Arial 50 bold",fg="gray95").grid(column=3,row=5)
            Label(self.manu,text="----",font="Arial 100 bold",fg="gray95").grid(column=4,row=5)

    def levels(self):
        self.manu.grid_forget()
        self.level = Frame(self.wind)
        self.level.grid()

        self.p_n = (self.player_n.get().capitalize())
        if len(self.p_n) == 0:
            self.notvalid = True
            messagebox.showerror("ERROR", "All boxes must be filled *")
        else:
            self.notvalid = False
            for widget in self.level.winfo_children():
                widget.destroy()
            # random numbers
            self.one = random.randrange(1, 21)
            self.two = random.randrange(1, 21)
            # level title
            Label(self.level,text="Welcome to Level 2", font="Arial 30 bold").grid(row=0, column=3)
            # problem
            Label(self.level, font=("Arial 45 bold"), text=f"{self.one} + {self.two} = ").place(x= 200 , y = 160)
            global problem
            problem = Entry(self.level,font="Arial 30 bold")
            problem.place(x=460,y=180,width=90,height=40)
            #free space 
            self.free_space_1()
            #submet button 

            Button(self.level ,text="subimet",bg="cornflower blue",fg="black",command =self.salon,font="Arial 14 bold",width=9,height=2).place(x=550, y=380)
            #exit bitton
            Button(self.level ,text=f"{self.answer}",bg="cornflower blue",fg="black",command =self.End_wind,font="Arial 14 bold",width=9,height=2).place(x=50, y=380)

    def salon(self):
        problem_A = problem.get()
        print('value:', problem_A)

        if len(problem_A) == 0: 
            messagebox.showerror("ERROR", "All boxes must be filled *")
        elif problem_A == self.answer:
            messagebox.showerror("ERROR", "good job")
     
       

    def free_space_1(self):
            Label(self.level,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=0)
            Label(self.level,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=1)
            Label(self.level,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=2)
            Label(self.level,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=3)
            Label(self.level,text="----",font="Arial 50 bold",fg="gray95").grid(column=2,row=4)
            Label(self.level,text="----",font="Arial 50 bold",fg="gray95").grid(column=3,row=5)
            Label(self.level,text="----",font="Arial 100 bold",fg="gray95").grid(column=4,row=5)
    
    def End_wind(self):
        self.level.grid_forget()
        self.score = Frame(self.wind)
        self.score.grid()
        Label(self.score, text="You Score").grid(column=1 , row= 1)
        



root.title("OSC Course Selection")
root.geometry("705x450")
gui = Interface(root)
gui.inter_face()
root.mainloop()