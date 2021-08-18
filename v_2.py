from tkinter import *


class Player:
    def __init__(self,pn,pa,lv):
        self.player_name = pn
        self.player_age = pa
        self.level = lv


    def age (self):
        return ["6","7","8","9","10","11","12"]
                
    def save(self,ps):
        player_file = open("Player_info.text", "a")
        player_file.write("****************************\n")
        player_file.write("player Name: {} \nplayerer age: {} \n \n"
        .format(self.player_name, self.player_age))
        player_file.write(f"level {self.level}\n")
        player_file.write(f"your Score({ps}/10)\n")
        player_file.write("****************************\n\n")
        player_file.close()
45