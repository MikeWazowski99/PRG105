"""
13.1 Name and Address

Write a GUI program that displays your name and address when a button is clicked (you can use the address of the school)
"""

import tkinter


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.name_value = tkinter.StringVar()
        self.street_value = tkinter.StringVar()
        self.csz_value = tkinter.StringVar()

        # 2 Frames
        self.info_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        self.name_label = tkinter.Label(self.info_frame, textvariable=self.name_value)
        self.street_label = tkinter.Label(self.info_frame, textvariable=self.street_value)
        self.csz_label = tkinter.Label(self.info_frame, textvariable=self.csz_value)

        # pack stuff
        self.name_label.pack()
        self.street_label.pack()
        self.csz_label.pack()
        # buttons
        self.show_info_button = tkinter.Button(self.button_frame, text='Show Info', command=self.show)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
        # pack buttons
        self.show_info_button.pack()
        self.quit_button.pack()
        # frame pack
        self.info_frame.pack()
        self.button_frame.pack()

        tkinter.mainloop()

    def show(self):
        self.name_value.set('Matt Wazowski')
        self.street_value.set('1535 Walnut Street')
        self.csz_value.set('Woodstock, IL, 60098')


my_gui = MyGUI()
