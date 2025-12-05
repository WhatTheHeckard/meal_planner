import tkinter as tk
from tkinter import ttk
from .recipe_tab import RecipeTab
from .meal_plan_tab import MealPlanTab

class RootWindow:
    def __init__(self):
        # Create the root window
        self.root = tk.Tk()
        self.root.title("Meal Planner")
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()
        self.root.geometry(f'{screenWidth}x{screenHeight}')
        # Create tabs of the window
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill="both")

        self.recipesTab = RecipeTab(self.notebook, screenWidth, screenHeight)
        self.notebook.add(self.recipesTab, text="Recipes")

        self.mealPlanTab = MealPlanTab(self.notebook, screenWidth, screenHeight)
        self.notebook.add(self.mealPlanTab, text="Meal Schedule")

        # Should have a shopping list class
        self.shoppingListTab = ttk.Frame(self.notebook)
        self.shoppingListTab.pack(fill='both', expand=True)
        self.notebook.add(self.shoppingListTab, text="Shopping List")


        self.root.mainloop()