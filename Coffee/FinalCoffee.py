"""
My final python project for PRG-105
Make a program that will tell the user interesting things about the certain areas around the world and inform the user
of the area such as the weather around there, the cost to live there for a certain amount of months, a fun fact of the
country,
List of things need to add: * a fun fact, * how much it cost to live there, * interesting things about the country,
                            * weather in the country, * currency converter, * image of the country / specific area
"""
import tkinter
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


# class MyGUI:
#     def __init__(self):
#         # These self mains are there to add a popup for countries / states except for self main.window
#         self.main_window = tkinter.Tk()
#         self.main_US_value = tkinter.StringVar()
#         self.main_France = tkinter.StringVar()
#         self.main_Japan_value = tkinter.StringVar()
#         self.main_Italy = tkinter.StringVar()
#         self.main_Canada = tkinter.StringVar()
#         self.main_Hawaii_value = tkinter.StringVar()
#
#         # 2 Frames
#         self.info_frame = tkinter.Frame(self.main_window)
#         self.button_frame = tkinter.Frame(self.main_window)
#
#         self.main_US = tkinter.Label(self.info_frame, textvariable=self.main_US_value)
#         self.main_Japan = tkinter.Label(self.info_frame, textvariable=self.main_Japan_value)
#         self.main_Hawaii = tkinter.Label(self.info_frame, textvariable=self.main_Hawaii_value)
#
#         # pack stuff
#         self.main_US.pack()
#         self.main_Japan.pack()
#         self.main_Hawaii.pack()
#
#         # buttons
#         self.show_info_button = tkinter.Button(self.button_frame, text='Show Info', command=self.show)
#         self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
#
#         # pack buttons
#         self.show_info_button.pack(side='left')
#         self.quit_button.pack(side='right')
#
#         # frame pack
#         self.info_frame.pack()
#         self.button_frame.pack()
#
#         tkinter.mainloop()
#
#     def show(self):
#         self.main_US_value.set('US')
#         self.main_Japan_value.set('Japan')
#         self.main_Hawaii_value.set('Hawaii')
#
#
# my_gui = MyGUI()
#


# Another pic

# Menu for Japan


def on_click(event=None):
    print("Image clicked")
    # Engine
    root = tk.Tk()
    # Title
    root.title("World Explorer")
    #
    img_file1 = Image.open('Japan.jpg')
    img_file1 = img_file1.resize((400, 400))
    photo = ImageTk.PhotoImage(img_file1)
    f = tk.Button(image=photo, command=cog())
    f.pack()
    b = tk.Button(root, text="Close", command=root.destroy, height='1')
    b.pack(side='bottom')
    root.mainloop()


def cog():
    print("Image Clicked")


def main(state='disabled'):
    # Icon for program
    root = tk.Tk()
    root.title("World Explorer")

    # Clickable images for Japan
    img_file1 = Image.open('Japan.jpg')
    img_file1 = img_file1.resize((200, 200))
    photo = ImageTk.PhotoImage(img_file1)

    # Clickable image for Mexico
    img_file2 = Image.open('CacunPlaya.jpg')
    img_file2 = img_file2.resize((200, 200))
    photo1 = ImageTk.PhotoImage(img_file2)

    # Clickable image for USA
    img_file3 = Image.open('NewYork.jpg')
    img_file3 = img_file3.resize((200, 200))
    photo2 = ImageTk.PhotoImage(img_file3)

    # button with image bind to the same function Japan
    a = tk.Button(root, image=photo1, command=on_click)
    a.pack(side='left')

    # button for Mexico
    c = tk.Button(root, image=photo, command=on_click)
    c.pack(side='right')

    # button for USA
    d = tk.Button(root, image=photo2, comand=on_click)
    d.pack(side='top')

    # button with text closing window
    b = tk.Button(root, text="Close", command=root.destroy, height='1')
    b.pack(side='bottom')

    # "start the engine"
    root.mainloop()


main()
