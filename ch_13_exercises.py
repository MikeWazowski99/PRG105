"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""
import tkinter
import tkinter.messagebox

# TODO 13.2 Using the tkinter Module
print("=" * 10, "Section 13.2 using tkinter", "=" * 10)
# Write the code from program 13-2 to display an empty window, no need
# to re-import tkinter. Use the class name MyGUI2

# TODO 13.3 Adding a label widget
print("=" * 10, "Section 13.3 adding a label widget", "=" * 10)


# Add a label to MyGUI2 (above) that prints your first and last name; pack the label
# Create an instance of MyGUI2


class MyGUI2:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(self.main_window, text='Michael Tapia')
        self.label.pack()
        tkinter.mainloop()


my_gui = MyGUI2()

# TODO 13.4 Organizing Widgets with Frames
print("=" * 10, "Section 13.4 using frames", "=" * 10)


# Create a MyGUI3 class that creates a window with two frames
# In the top Frame add labels with your name and major
# In the bottom frame add labels with the classes you are taking this semester
# Create an instance of MyGUI3


class MyGUI3:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)

        # top frame labels
        self.label_name = tkinter.Label(self.frame1, text="Michael Tapia")
        self.label_major = tkinter.Label(self.frame1, text="Mobile Design And Development")

        self.label_name.pack(side='top')
        self.label_major.pack(side='top')

        # bottom frame labels

        self.label_programming_logics = tkinter.Label(self.frame2, text='Programming Logics')
        self.label_web_dev = tkinter.Label(self.frame2, text='Web Development')
        self.label_micro_eco = tkinter.Label(self.frame2, text='Micro Economics')
        self.label_game_design = tkinter.Label(self.frame2, text='Game Design')

        self.label_programming_logics.pack(side='left')
        self.label_web_dev.pack(side='left')
        self.label_micro_eco.pack(side='left')
        self.label_game_design.pack(side='left')

        # pack frames

        self.frame1.pack()
        self.frame2.pack()

        tkinter.mainloop()


my_gui3 = MyGUI3()

# TODO 13.5 Button Widgets and info Dialog Boxes
print("=" * 10, "Section 13.5 button widgets and info dialogs", "=" * 10)
# Create a GUI that will tell a joke
# Use a button to show the punch line, which should appear in a dialog box
# Create an instance of the GUI


class MyGUI4:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.joke = tkinter.Label(self.main_window, text='Why are crabs so bad at sharing?')
        self.my_button = tkinter.Button(self.main_window, text="Punchline", command=self.reveal)

        self.my_button.pack()
        self.joke.pack()

        tkinter.mainloop()

    def reveal(self):
        tkinter.messagebox.showinfo('Punchline', 'Because they’re all shellfish.')


my_gui4 = MyGUI4()

# TODO 13.6 getting input / 13.7 Using Labels as output fields
print("=" * 10, "Section 13.6-13.7 input and output using Entry and Label", "=" * 10)
# Using the program in 13.10 kilo converter as a sample,
# create a program to convert inches to centimeters


class InchConverterGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.prompt_label = tkinter.Label(self.top_frame, text="Enter a distance in inches:  ")
        self.inch_entry = tkinter.Entry(self.top_frame, width=10)

        self.prompt_label.pack(side='left')
        self.inch_entry.pack(side='left')

        #middle frame

        self.describe_label = tkinter.Label(self.main_window, text='Converted to centimeters:')
        self.value = tkinter.StringVar()
        self.centi_label = tkinter.Label(self.main_window, textvariable=self.value)

        self.describe_label.pack(side='left')
        self.centi_label.pack(side='left')
        self.calc_button = tkinter.Button(self.main_window, text=''
                                                                 'Convert', command=self.convert)
        self.quit_button = tkinter.Button(self.main_window, text='Quit', command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):
        inch = float(self.inch_entry.get())
        centi = inch * 2.54

        self.value.set(centi)


my_gui5 = InchConverterGUI()
