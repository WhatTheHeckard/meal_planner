import json
import os.path

#filename = "recipes.json"


# CONSIDER MAKING THIS A DATACLASS
class Recipe:
    def __init__(self,
                 recipe_name : str="N/A",
                 recipe_type : list[str]=[],
                 diet : list[str]=[],
                 rating : int=0,
                 servings : int=0,
                 ingredients : list[str]=[],
                 instructions : str="N/A",
                 notes : str="N/A"):
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

    def to_dict(self) -> dict:
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
    
    def __str__(self) -> str:
        ret_str = f"Recipe Name: {self.recipe_name}\n"
        ret_str += f"Recipe Type: {', '.join(self.recipe_type)}\n"
        ret_str += f"Diet: {', '.join(self.diet)}\n"
        ret_str += f"Rating: {self.rating}\n"
        ret_str += f"Servings: {self.servings}\n"
        ret_str += f"Ingredients: {', '.join(self.ingredients)}\n"
        ret_str += f"Instructions: {self.instructions}\n"
        ret_str += f"Notes: {self.notes}\n"
        return ret_str


class RecipeBook:
    def __init__(self, filename):
        self.filename : str = filename
        self.recipe_list : list[Recipe] = self.load_recipe_list()

    def add_recipe(self, new_recipe: Recipe) -> 'RecipeBook':
        self.recipe_list.append(new_recipe)
        return self

    def remove_recipe(self, recipe_name="") -> 'RecipeBook':
        if (recipe_name == ""):
            # Should send some sort of error because there is no recipe
            # to remove.
            pass
        else:
            for recipe_itr in self.recipe_list:
                if (self.recipe_list[recipe_itr].recipe_name == recipe_name):
                    self.recipe_list.remove(recipe_itr)
                    break
        return self

    def overwrite_recipe(self, new_recipe: Recipe) -> 'RecipeBook':
        for item in self.recipe_list:
            if item.recipe_name == new_recipe.recipe_name:
                self.recipe_list[item] = new_recipe
                return self

    def print_list(self) -> 'RecipeBook':
        for recipe_itr in self.recipe_list:
            print(recipe_itr.to_dict())
        return self

    def dump_recipe_list(self) -> 'RecipeBook':
        """Print Recipe book to json file"""
        recipe_list = {}
        for recipe_itr in self.recipe_list:
            recipe_list.update(recipe_itr.to_dict())
        with open(self.filename, "w") as fd:
            json.dump(recipe_list, fd, indent=4)
            fd.close()
        return self

    def load_recipe_list(self) -> list[Recipe]:
        # If the file does not exist, return empty RecipeBook
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

    def search_meal_type(self, recipe_type) -> list[Recipe]:
        ret_list = []
        for item in self.recipe_list:
            if item.recipe_type == recipe_type:
                ret_list.append(item)
        return ret_list

    def search_ingredients(self, ingredient) -> list[Recipe]:
        ret_list = []
        for item in self.recipe_list:
            if ingredient in item.ingredients:
                ret_list.append(item)
        return ret_list
    
    def search_recipe_name(self, name) -> list[Recipe]:
        ret_list = []
        for item in self.recipe_list:
            if name.lower() in item.recipe_name.lower():
                ret_list.append(item)
        return ret_list


if __name__ == "__main__":
    read_list = RecipeBook("recipes.json")
    read_list.print_list()
