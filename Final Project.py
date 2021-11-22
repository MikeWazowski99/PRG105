"""
My final python project for PRG-105

Make a program that will tell the user interesting things about the certain areas around the world and inform the user
of the area such as the weather around there, the cost to live there for a certain amount of months, a fun fact of the
country,

List of things need to add: * a fun fact, * how much it cost to live there, * interesting things about the country,
                            * weather in the country, * currency converter, * image of the country / specific area
"""

import tkinter
from tkinter import *
# from PIL import ImageTk, Image
# from PIL import Image




class MyGUI:
    def __init__(self):
        # These self mains are there to add a popup for countries / states except for self main.window
        self.main_window = tkinter.Tk()
        self.main_US_value = tkinter.StringVar()
        self.main_France = tkinter.StringVar()
        self.main_Japan_value = tkinter.StringVar()
        self.main_Italy = tkinter.StringVar()
        self.main_Canada = tkinter.StringVar()
        self.main_Hawaii_value = tkinter.StringVar()

        # 2 Frames
        self.info_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        self.main_US = tkinter.Label(self.info_frame, textvariable=self.main_US_value)
        self.main_Japan = tkinter.Label(self.info_frame, textvariable=self.main_Japan_value)
        self.main_Hawaii = tkinter.Label(self.info_frame, textvariable=self.main_Hawaii_value)

        # pack stuff
        self.main_US.pack()
        self.main_Japan.pack()
        self.main_Hawaii.pack()

        # buttons
        self.show_info_button = tkinter.Button(self.button_frame, text='Show Info', command=self.show)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)

        # pack buttons
        self.show_info_button.pack(side='left')
        self.quit_button.pack(side='right')

        # frame pack
        self.info_frame.pack()
        self.button_frame.pack()

        tkinter.mainloop()

    def show(self):
        self.main_US_value.set('US')
        self.main_Japan_value.set('Japan')
        self.main_Hawaii_value.set('Hawaii')


my_gui = MyGUI()


def main():
    root = Tk()
    root.title("World Explorer")
    root.iconbitmap("/Users/mtapia19/Desktop/PRG105/favicon-3.ico")
    root.mainloop()

main()
