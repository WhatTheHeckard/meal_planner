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

    # Define buttons
    all_btn = tk.Button(root, text="All") # Root is the master module for the button to live on.
    all_btn.pack()
    breakfast_btn = tk.Button(root, text="Breakfast")
    breakfast_btn.pack()
    lunch_btn = tk.Button(root, text="Lunch")
    lunch_btn.pack()
    dinner_btn = tk.Button(root, text="Dinner")
    dinner_btn.pack()
    snacks_btn = tk.Button(root, text="Snacks")
    snacks_btn.pack()
    dessert_btn = tk.Button(root, text="Dessert")
    dessert_btn.pack()

    root.config(menu=menubar)
    root.mainloop()
