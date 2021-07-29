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
        Label(self.manu,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=0)
        Label(self.manu,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=1)
        Label(self.manu,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=3)
        Label(self.manu,text="----",font="Arial 50 bold",fg="gray95").grid(column=2,row=4)
        Label(self.manu,text="----",font="Arial 50 bold",fg="gray95").grid(column=3,row=5)
        Label(self.manu,text="----",font="Arial 50 bold",fg="gray95").grid(column=4,row=5)
        #title
        Label(self.manu ,text="Welcome to maths games ", font="Arial 30 bold").grid(row=0, column=2)
        #Levels 
        #Level 1
        Button(self.manu ,text="Level 1",bg="cornflower blue",fg="black",activeforeground = "green",command=self.levels,font="Arial 14 bold",width=9,height=2).place(x=300 , y=160)
        #Level 2
        Button(self.manu ,text="Level 2",bg="#ffab40",fg="black",command =self.levels,font="Arial 14 bold",width=9,height=2).place(x=300 , y=228)
        #Level 3
        Button(self.manu ,text="Level 3",bg="red",fg="black",command =self.levels,font="Arial 14 bold",width=9,height=2).place(x=300 , y=298)

    def levels(self):
        self.p_n = (self.player_n.get().capitalize())
        if len(self.p_n) == 0:
            self.notvalid = True
            messagebox.showerror("ERROR", "All boxes must be filled *")
        else:
            self.notvalid = False
            for widget in self.manu.winfo_children():
                widget.destroy()
            #random numbers
            number_one = random.randrange(1, 21)
            number_two = random.randrange(1, 21)
            aunser = number_one + number_two
            # level title
            Label(self.manu,text="Welcome to Level 2 division", font="Arial 30 bold").grid(row=0, column=2)
            # problem
            self.problem=Label(self.manu, font=("Arial 45 bold"), text=f"{number_one} + {number_two} = ")
            self.problem.place(x= 200 , y = 160)

            self.problem_a=Entry(self.manu,font="Arial 30 bold")
            self.problem_a.place(x=460,y=180,width=90,height=40)
            #free 
            Label(self.manu,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=0)
            Label(self.manu,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=1)
            Label(self.manu,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=2)
            Label(self.manu,text="----",font="Arial 50 bold",fg="gray95").grid(column=1,row=3)
            Label(self.manu,text="----",font="Arial 50 bold",fg="gray95").grid(column=2,row=4)
            Label(self.manu,text="----",font="Arial 50 bold",fg="gray95").grid(column=3,row=5)
            Label(self.manu,text="----",font="Arial 50 bold",fg="gray95").grid(column=4,row=5)
            #submet button 
            Button(self.manu ,text="subimet",bg="cornflower blue",fg="black",font="Arial 14 bold",width=9,height=2).place(x=550, y=380)
            #exit bitton
            Button(self.manu ,text="End Game",bg="cornflower blue",fg="black",command =self.end,font="Arial 14 bold",width=9,height=2).place(x=50, y=380)
    def end(self):

        self.manu.grid_forget()
        self.score = Frame(self.wind)
        self.score.grid()
        Label()


root.title("OSC Course Selection")
root.geometry("705x450")
gui = Interface(root)
gui.inter_face()
root.mainloop()