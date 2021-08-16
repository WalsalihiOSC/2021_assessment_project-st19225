from tkinter import *


class Player:
    def __init__(self,pn,pa):
        self.player_name = pn
        self.player_age = pa

    def age (self):
        return ["6","7","8","9","10","11","12"]
                
    def save(self):
        player_file = open("Player_info.text", "a")
        player_file.write(" player Name: {} \nplayerer age: {} \n \n"
        .format(self.player_name, self.player_age))
        player_file.write("##########################\n")
        player_file.close()
