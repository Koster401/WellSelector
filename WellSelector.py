# WellSelector.py by Rasmus Larsen (RKLX)

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ctypes import windll
import os


class WellSelector:

    """ This class contains the code for the well selector GUI """

    def __init__(self, master, info_text):
        
        master.title("WellSelector96")
        self.label = ttk.Label(master,
                               text = info_text)
        self.label.grid(row = 0,
                        column = 0,
                        padx = 5,
                        pady = 5,
                        sticky = 'sw')

        self.frame = Frame(master,
                           highlightbackground = "grey",
                           highlightthickness = 1)
        self.frame.grid(row = 1,
                        column = 0,
                        padx = 5,
                        pady = 5)

        self.letters = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
        self.check_value = IntVar()

        for i in range(8):
            ttk.Label(self.frame, text = self.letters[i]).grid(row = i + 1,
                                                               column = 0,
                                                               padx = 5)

        for i in range(12):
            ttk.Label(self.frame, text = str(i + 1)).grid(row = 0,
                                                          column = i + 1,
                                                          sticky = "sw")
        self.check_button_counter = 0
        self.check_button_variable_list = []
        self.well_list = []
        global check_button_list
        global well_list
        
        for i in range(12):
            for j in range(8):
                self.well = f"{self.letters[j]}{i+1}"
                self.well_list.append(self.well)
                self.check_button_variable_list.append(IntVar())
                self.check_button = ttk.Checkbutton(self.frame,
                                                    variable = self.check_button_variable_list[self.check_button_counter])
                self.check_button.grid(row = j + 1,
                                       column = i + 1,
                                       ipadx = 2,
                                       ipady = 2)
                self.check_button_counter += 1

        check_button_list = self.check_button_variable_list
        well_list = self.well_list

        ttk.Button(master,
                   text = "Done",
                   command = lambda: [self.done(), master.destroy()]).grid(row = 2,
                                                                           column = 0,
                                                                           padx = 5,
                                                                           pady = 5)

    def done(self):
        
        """"This function retrieves the state of the check_button_list and writes it to an outputfile"""
        
        global check_button_list
        self.check_button_state_list = []
        self.dir_output = f"{os.path.dirname(os.path.realpath(__file__))}\Output.txt"
        print(self.dir_output)
        #self.check_button_state_dict = {}

        self.f = open(self.dir_output, "w")
        self.f.write("Well;State\n")
        
        for i in range(len(check_button_list)):
            self.check_button_value = check_button_list[i].get()
            #self.check_button_state_list.append(self.check_button_value)
            #self.check_button_state_dict[well_list[i]] = self.check_button_value
            print(f"{well_list[i]}: {self.check_button_value}")
            self.f.write(f"{well_list[i]}; {self.check_button_value}\n")
        self.f.close()
        
        
        
        
        

def main():
    
    windll.shcore.SetProcessDpiAwareness(1)
    root = Tk()
    app = WellSelector(root,"Vælg de utætte positioner på pladen.")
    root.mainloop()
    
if __name__ == "__main__": main()
