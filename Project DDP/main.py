# main.py
from tkinter import *
from tkinter import messagebox
from project1 import PointOfSaleApp

def main():
    root = Tk()
    app = PointOfSaleApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
