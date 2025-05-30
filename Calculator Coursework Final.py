import tkinter as tk #Importing Tkinter to be able to create a user interface
from threading import Thread #Importing Thread from threading to run program with Threads
import math #Importing math to use more advanced math functions

#Super Class CalculatorApp
class CalculatorApp:
    #Initiate function with self parameter and root instance
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator") #Title of program

    #Define function to create entry box for input
    def widgets_Create(self):
        self.entry = tk.Entry(self.root, width=30, font=('Arial', 14))
        self.entry.grid(row=0, column=0, columnspan=5, sticky="ew", pady=5)

    #buttons list to hold the layout of the buttons in rows and columns withins sets
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('.', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('√', 1, 4), ('^', 2, 4), ('Del', 4, 4), ('C', 3, 4)
        ]
        
        #Creating buttons for each character in the buttons list
        for (text, row, column) in buttons:
            btn = tk.Button(self.root, text=text, width=5, height=2, font=('Arial', 14), command=lambda t=text: self.Button_press(t))
            btn.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
            #if statements to set background colors for all buttons
            if text.isdigit() or text == '.':
                btn.config(bg='#E0E0E0')
            elif text in {'+', '-', '*', '/'}:
                btn.config(bg='#FFD180')
            elif text == '=':
                btn.config(bg='#81C784')
            elif text == 'C':
                btn.config(bg='#FF8A80')
            elif text in {'√', '^'}:
                btn.config(bg='#B39DDB')
            elif text =='Del':
                btn.config(bg='#FF8A80')

        # Configure column and row weights
        self.root.columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.root.rowconfigure((0, 1, 2, 3, 4), weight=1)

    #Button_press function that runs the Button_press_thread function as a Thread
    def Button_press(self, char):
        btn_Press = Thread(target=self.Button_press_thread, args=(char,))
        btn_Press.start()
    
    #Button_press_thread function that inserts button presses
    def Button_press_thread(self, char):
        if char == 'C':
            self.entry.delete(0, tk.END)
        elif char == 'Del':
            self.entry.delete(len(self.entry.get())-1, tk.END)
        elif char == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif char == '√':
            try:
                result = math.sqrt(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif char == '^':
            self.entry.insert(tk.END, '**')
        else:
            self.entry.insert(tk.END, char)

#gui_init function which initiates GUI
def gui_init():
    root = tk.Tk()
    app = CalculatorApp(root)
    app.widgets_Create()  # Call create_widgets method here
    root.mainloop()

#If statement that checks if the program is being run within the same file
if __name__ == "__main__":
    #Thread that starts the code by calling gui_init using the gui_start thread
    gui_start = Thread(target=gui_init)
    gui_start.start()
