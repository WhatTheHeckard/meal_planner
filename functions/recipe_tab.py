import tkinter as tk
from tkinter import ttk
from json_testing import RecipeBook, Recipe

class RecipeBox(ttk.Frame):
    def __init__(self, parent: ttk.Frame):
        super().__init__(parent)
        self.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        self.recipe_label = ttk.Label(self, text="", justify=tk.LEFT, anchor="nw")
        self.recipe_label.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

    def print_recipe(self, listbox: tk.Listbox, recipe_list: list[Recipe]):
        # Find which item is selected from the listbox
        selected_recipe = listbox.get(listbox.curselection())
        # Find the recipe in the recipe list
        for recipe in recipe_list:
            if recipe.recipe_name == selected_recipe:
                # Print out the recipe details
                self.recipe_label.config(text=str(recipe))
                break
        # Bind methods for editing and removing recipes
        edit_button = ttk.Button(self, text="Edit Recipe")
        edit_button.pack(side=tk.LEFT, padx=10, pady=10)
        del_button = ttk.Button(self, text="Remove Recipe")
        del_button.pack(side=tk.LEFT, padx=10, pady=10)

class RecipeTab(ttk.Frame):
    meal_types = ["Breakfast", "Lunch", "Dinner", "Snacks", "Dessert"]
    def __init__(self, parent: ttk.Frame | tk.Tk, screenWidth: int, screenHeight: int):
        super().__init__(parent, width=screenWidth, height=screenHeight)

        # Need to create a recipe list and provide to the Listbox
        recipe_list = RecipeBook("recipes.json").recipe_list
        recipe_names = [r.recipe_name for r in recipe_list]

        listbox = tk.Listbox(self, listvariable=tk.StringVar(value=recipe_names), selectmode=tk.SINGLE)
        listbox.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        listbox_yscroll = ttk.Scrollbar(self, orient=tk.VERTICAL, command=listbox.yview)
        listbox['yscrollcommand'] = listbox_yscroll.set
        listbox_yscroll.pack(pady=10, side=tk.RIGHT, fill=tk.Y)

        recipe_box = RecipeBox(self)

        listbox.bind('<<ListboxSelect>>', lambda _ : recipe_box.print_recipe(listbox, recipe_list))

        # EDIT AND REMOVE SHOULD PROBABLY GO ON THE RECIPE PAGE ITSELF

        # Define buttons
        meal_type_frame = ttk.Frame(self)
        ttk.Label(meal_type_frame, text="Meal Types: ").pack(side=tk.LEFT)

        selected_meal_type = [tk.BooleanVar(value=True) for _ in self.meal_types]
        for ind, meal_type in enumerate(self.meal_types):
            ttk.Checkbutton(meal_type_frame, text=meal_type, variable=selected_meal_type[ind]).pack(side=tk.LEFT)
        meal_type_frame.pack(side=tk.TOP, fill=tk.X)

        ingredients_frame = ttk.Frame(self)
        ttk.Label(ingredients_frame, text="Ingredients: ").pack(side=tk.LEFT)
        ingredients_entry = ttk.Entry(ingredients_frame)
        ingredients_entry.pack(side=tk.LEFT)
        ingredients_frame.pack(side=tk.TOP, fill=tk.X)

        diet_frame = ttk.Frame(self)
        ttk.Label(diet_frame, text="Diet: ").pack(side=tk.LEFT)
        diet_entry = ttk.Entry(diet_frame)
        diet_entry.pack(side=tk.LEFT)
        diet_frame.pack(side=tk.TOP, fill=tk.X)

        filter_button = ttk.Button(self, text="Apply Filters")
        filter_button.pack(side=tk.TOP, fill=tk.X) # ADD COMMAND TO UPDATE THE RECIPE LIST. command=self.update_recipe_list

        # NEED TO LINK COMMANDS TO THE BUTTONS


        # CHANGE OF PLANS
        # Initially, show a list of all recipes
        # Then have checkboxes to use as filters. All meal_type checkboxes will start selected to show all recipes
        # Then there will be checkboxes along with an entry for: diet, rating, servings, ingredients
        # Recipes name will always be searchable.
        # The button "Add Recipe" will open a new window which will allow for filling out the necessary fields to create a new recipe.