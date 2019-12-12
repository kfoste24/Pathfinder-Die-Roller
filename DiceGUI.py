from tkinter import *
from random import randint

class Application(Frame):
    """
    An example of a Dice rolling app developed using the 
    Tkinter GUI.
    """
    def roll_die(num_faces):
        return randint(1,num_faces)

    def __init__(self, master):
        """
        Initializes the frame.
        :param master: root.Tk()
        """
        Frame.__init__(self, master)
        self.entry = Entry(master, width=16, font=("Arial",25))
        self.entry.grid(row=0, column=0, columnspan=8, sticky="w")
        self.entry.focus_set()
        self.entry.configure(state="disabled", disabledbackground="white", disabledforeground="black")
        self.create_widgets()
        self.bind_buttons(master)
        self.grid()
        
    def add_chr(self, char, btn=None):
        """
        Concatenates a character passed from a button press (or key type) 
        to a string.
        :param char: string to add passed from a button
        :param btn: button name to use if key is pressed (to flash)
        :return: None
        """
        self.entry.configure(state="normal")
        self.flash(btn) # Flash a button correspond to keystroke
        if self.entry.get() == "Invalid Input":
            self.entry.delete(0,END)
        self.entry.insert(END, char)
        self.entry.configure(state="disabled")

    def clear(self):
       
        self.entry.configure(state="normal")
        if self.entry.get() != "Invalid Input":
            # Clears full entry when "Invalid Input"
            text = self.entry.get()[:-1]
            self.entry.delete(0,END)
            self.entry.insert(0,text)
        else:
            self.entry.delete(0, END)
        self.entry.configure(state="disabled")

    def clear_all(self):
        
        self.entry.configure(state="normal")
        self.entry.delete(0, END)
        self.entry.configure(state="disabled")

    def calculate(self):
       
        self.entry.configure(state="normal")
        e = self.entry.get()
       

        try:
            ans = eval(e)
        except Exception as ex:
            self.entry.delete(0,END)
            self.entry.insert(0, "Invalid Input")
        else:
            self.entry.delete(0,END)
            if len(str(ans)) > 20: # Alleviates problem of large numbers
                self.entry.insert(0, '{:.10e}'.format(ans))
            else:
                self.entry.insert(0, ans)
        self.entry.configure(state="disabled")

    def flash(self,btn):
    
        if btn != None:
            btn.config(bg="darkblue")
            if btn == self.c_bttn:
                self.clear()
                self.master.after(100, lambda: btn.config(bg="SystemButtonFace"))
            elif btn == self.eq_bttn:
                self.master.after(100, lambda: btn.config(bg="red"))
                self.calculate()
            elif btn == self.ac_bttn:
                self.clear_all()
                self.master.after(100, lambda: btn.config(bg="SystemButtonFace"))
            else:
                self.master.after(100, lambda: btn.config(bg="SystemButtonFace"))
        else:
            pass

    def bind_buttons(self, master):
        master.bind("<Return>", lambda event, btn=self.eq_bttn: self.flash(btn))
        master.bind("<BackSpace>", lambda event, btn=self.c_bttn: self.flash(btn))
        master.bind("9", lambda event, char="Pathfinder Rocks!", btn=self.nine_bttn: self.add_chr(char, btn))
        master.bind("8", lambda event, char=randint(1,100), btn=self.eight_bttn: self.add_chr(char, btn))
        master.bind("7", lambda event, char=randint(1,2), btn=self.seven_bttn: self.add_chr(char, btn))
        master.bind("6", lambda event, char=randint(1,4), btn=self.six_bttn: self.add_chr(char, btn))
        master.bind("5", lambda event, char=randint(1,6), btn=self.five_bttn: self.add_chr(char, btn))
        master.bind("4", lambda event, char=randint(1,8), btn=self.four_bttn: self.add_chr(char, btn))
        master.bind("3", lambda event, char=randint(1,10), btn=self.three_bttn: self.add_chr(char, btn))
        master.bind("2", lambda event, char=randint(1,12), btn=self.two_bttn: self.add_chr(char, btn))
        master.bind("1", lambda event, char=roll_die(20), btn=self.one_bttn: self.add_chr(char, btn))
        master.bind("+", lambda event, char="+", btn=self.add_bttn: self.add_chr(char, btn))
        master.bind("c", lambda event, btn=self.ac_bttn: self.flash(btn), self.clear_all)
    
    def create_widgets(self):
        
        self.eq_bttn = Button(self, text="=", width=40, height=4, bg="red", command=lambda: self.calculate())
        self.eq_bttn.grid(row=4, column=0, columnspan=6)
        
        self.ac_bttn = Button(self, text='CE', width=9, height=4, bg="blue", command=lambda: self.clear_all())
        self.ac_bttn.grid(row=1, column=4)
        
        self.c_bttn = Button(self, text='←', width=9, height=4, bg="blue", command=lambda: self.clear())
        self.c_bttn.grid(row=2, column=4 )

        self.add_bttn = Button(self, text="+", width=9, height=4, bg="blue", command=lambda: self.add_chr('+'))
        self.add_bttn.grid(row=3, column=4)
            
        self.seven_bttn = Button(self, text="Coin Flip", width=9, height=4, bg="light blue", command=lambda: self.add_chr(randint(1,2)))
        self.seven_bttn.grid(row=1, column=0)

        self.eight_bttn = Button(self, text="D100", width=9, height=4, bg="light blue", command=lambda: self.add_chr(randint(1,100)))
        self.eight_bttn.grid(row=1, column=1)

        self.nine_bttn = Button(self, text="PF", width=9, height=4, bg="light blue", command=lambda: self.add_chr("Pathfinder Rocks!"))
        self.nine_bttn.grid(row=1, column=2)

        self.four_bttn = Button(self, text="D8", width=9, height=4, bg="light blue", command=lambda: self.add_chr(randint(1,8)))
        self.four_bttn.grid(row=2, column=0)

        self.five_bttn = Button(self, text="D6", width=9, height=4, bg="light blue", command=lambda: self.add_chr(randint(1,6)))
        self.five_bttn.grid(row=2, column=1)

        self.six_bttn = Button(self, text="D4", width=9, height=4, bg="light blue", command=lambda: self.add_chr(randint(1,4)))
        self.six_bttn.grid(row=2, column=2)

        self.one_bttn = Button(self, text="D20", width=9, height=4, bg="light blue", command=lambda: self.add_chr(randint(1,20)))
        self.one_bttn.grid(row=3, column=0)

        self.two_bttn = Button(self, text="D12", width=9, height=4, bg="light blue", command=lambda: self.add_chr(randint(1,12)))
        self.two_bttn.grid(row=3, column=1)

        self.three_bttn = Button(self, text="D10", width=9, height=4, bg="light blue", command=lambda: self.add_chr(randint(1,10)))
        self.three_bttn.grid(row=3, column=2)

       
root = Tk()
root.geometry()
root.title("Die Rolls")
app = Application(root)
root.mainloop()