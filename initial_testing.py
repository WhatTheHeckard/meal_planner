import tkinter as tk
import pandas_test as pt

def new_window():
    pass

def donothing():
    filewin = tk.Toplevel(root)
    button = tk.Button(filewin, text="Do nothing button")
    button.pack()


if __name__ == "__main__":
    # start by getting Pandas dataframe from the created CSV
    filename = "./data_storage.csv"
    df = pt.import_csv(filename)

    root = tk.Tk()
    root.geometry("1000x1000") # set window size
    root.title("Welcome to my app!")
    menubar = tk.Menu(root)



    root.config(menu=menubar)
    root.mainloop()
