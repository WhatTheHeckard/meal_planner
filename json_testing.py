import json
import os.path
from typing import List

#filename = "recipes.json"


class Recipe:
    def __init__(self, recipe_name="N/A", recipe_type=[], diet=[], rating=0,
                 servings=0, ingredients=[], instructions="N/A", notes="N/A"):
        """Initialize an object of class Meal.
        Arguments:
            recipe_name: Meal name as a string. Default is 'N/A'
            recipe_type: Valid meal types are breakfast, lunch, dinner, dessert
                        and snack. A single meal could be multiple meal types.
                        Default is an empty list.
            diet: What diet plans could this meal fall under. I.e. dairy free,
                        gluten free, low fat, low FODMAP... Default is an
                        empty list since a meal could be multiple diet plans.
            rating: What rating you give to the meal. Default is 0.
            servings: How many servings does this recipe make. Default is 0.
            ingredients: List of ingredients. Default is an empty list.
            instructions: List of instructions for making the recipe. Default
                        is an empty list.
            notes: Any additional notes to add about the recipe."""

        self.recipe_name = recipe_name
        self.recipe_type = recipe_type
        self.diet = diet
        self.rating = rating
        self.servings = servings
        self.ingredients = ingredients
        self.instructions = instructions
        self.notes = notes

    def recipe_to_json(self):
        return {
            f"{self.recipe_name}": {
                "recipe_type": f"{self.recipe_type}",
                "diet": f"{self.diet}",
                "rating": f"{self.rating}",
                "servings": f"{self.servings}",
                "ingredients": f"{self.ingredients}",
                "instructions": f"{self.instructions}",
                "notes": f"{self.notes}"
            }
        }


class Recipe_Book:
    def __init__(self, filename):
        self.filename = filename
        self.recipe_list = self.load_recipe_list()

    def add_recipe(self, new_recipe: Recipe):
        self.recipe_list.append(new_recipe)

    def remove_recipe(self, recipe_name=""):
        if (recipe_name == ""):
            # Should send some sort of error because there is no recipe
            # to remove.
            pass
        else:
            for recipe_itr in self.recipe_list:
                if (self.recipe_list[recipe_itr].recipe_name == recipe_name):
                    self.recipe_list.remove(recipe_itr)
                    break

    def overwrite_recipe(self, new_recipe: Recipe):
        for item in self.recipe_list:
            if item.recipe_name == new_recipe.recipe_name:
                self.recipe_list[item] = new_recipe
                return

    def print_list(self):
        for recipe_itr in self.recipe_list:
            print(recipe_itr.recipe_to_json())

    def dump_recipe_list(self):
        """Print Recipe book to json file"""
        recipe_list = {}
        for recipe_itr in self.recipe_list:
            recipe_list.update(recipe_itr.recipe_to_json())
        with open(self.filename, "w") as fd:
            json.dump(recipe_list, fd, indent=4)
            fd.close()

    def load_recipe_list(self):
        # If the file does not exist, return empty Recipe_Book
        if (not os.path.isfile(self.filename)):
            return 0
        recipe_list = []
        with open(self.filename, "r") as fd:
            load_data = json.load(fd)
            fd.close()
        for key in load_data:
            recipe_name = str(key)
            read_recipe = Recipe(recipe_name, **load_data[key])
            recipe_list.append(read_recipe)
        return recipe_list

    def search_meal_type(meal_type, self) -> List[Recipe]:
        ret_list = []
        for item in self.recipe_list:
            if item.meal_type == meal_type:
                ret_list.append(item)
        return ret_list

    def search_ingredients(ingredient, self) -> List[Recipe]:
        ret_list = []
        for item in self.recipe_list:
            if ingredient in item.ingredients:
                ret_list.append(item)
        return ret_list


if __name__ == "__main__":
    read_list = Recipe_Book("recipes.json")
    read_list.print_list()
