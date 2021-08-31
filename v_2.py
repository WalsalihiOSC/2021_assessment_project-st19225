

class Student:
    def __init__(self,pn,pa):
        self.player_name = pn
        self.player_age = pa


    def age (self):
        return ["6","7","8","9","10","11","12"]
        
    def level_one(self):
            z = ["1","2","3","4","5"]
            w = ["6","7","8","9","10"]
            return w , z ;

    def level_two(self):
            z = ["6","7","5","4","3"]
            w = ["8","9","10","11","12"]
            return w ,z ;

    def level_three(self):
            z = ["1","2","3","4","5","6","7","8","9"]
            w = ["13","14","15","16","10","11","12"]
            return w, z ;
            
                
    def save(self,ps):
        player_file = open("Player_info.text", "a")
        player_file.write("****************************\n")
        player_file.write("player Name: {} \nplayerer age: {} \n \n"
        .format(self.player_name, self.player_age))
        player_file.write(f"your Score({ps}/10)\n")
        player_file.write("****************************\n\n")
        player_file.close()