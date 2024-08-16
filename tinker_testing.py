import tkinter as tk

def donothing():
    filewin = tk.Toplevel(root)
    button = tk.Button(filewin, text="Do nothing button")
    button.pack()

root = tk.Tk()
#root.geometry("1000x1000") # set window size
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



# filemenu = tk.Menu(menubar, tearoff=0)
# filemenu.add_command(label="New", command=donothing)
# filemenu.add_command(label="Open", command=donothing)
# filemenu.add_command(label="Save", command=donothing)
# filemenu.add_command(label="Save as...", command=donothing)
# filemenu.add_command(label="Close", command=donothing)
# filemenu.add_separator()
# filemenu.add_command(label="Exit", command=root.quit)
# menubar.add_cascade(label="File", menu=filemenu)

# editmenu = tk.Menu(menubar, tearoff=0)
# editmenu.add_command(label="Undo", command=donothing)
# editmenu.add_separator()
# editmenu.add_command(label="Cut", command=donothing)
# editmenu.add_command(label="Copy", command=donothing)
# editmenu.add_command(label="Paste", command=donothing)
# editmenu.add_command(label="Delete", command=donothing)
# editmenu.add_command(label="Select All", command=donothing)
# menubar.add_cascade(label="Edit", menu=editmenu)

# helpmenu = tk.Menu(menubar, tearoff=0)
# helpmenu.add_command(label="Help Index", command=donothing)
# helpmenu.add_command(label="About...", command=donothing)
# menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()
