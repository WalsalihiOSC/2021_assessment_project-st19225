from tkinter import *

class window2:
    def __init__(self, master1):
        self.panel2 = Frame(master1)
        self.panel2.grid()
        self.button2 = Button(self.panel2, text = "Quit", command = self.panel2.quit)
        self.button2.grid()
        vcmd = (master1.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.text1 = Entry(self.panel2, validate = 'key', validatecommand = vcmd)
        self.text1.grid()
        self.text1.focus()

    def validate(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        if text in '0123456789.-+':
            try:
                if value_if_allowed:
                    float(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False

root1 = Tk()
root1.geometry("200x50")

window2(root1)
root1.mainloop()