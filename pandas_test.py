import os
import pandas as pd


# These columns define what data about a meal is contained in a dataframe and
# how it's organized within the CSVs
COLUMNS = ["Meal_Name", "Meal_Type", "Diet", "Rating", "Servings",
           "Ingredients", "Instructions", "Notes"]


class Meal:
    def __init__(self, meal_name="N/A", meal_type=[], diet=[], rating=0,
                 servings=0, ingredients=[], instructions=[], notes=[]):
        """Initialize an object of class Meal.
        Arguments:
            meal_name: Meal name as a string. Default is 'N/A'
            meal_type: Valid meal types are breakfast, lunch, dinner, dessert
                        and snack. A single meal could be multiple meal types.
                        Default is an empty list.
            diet: What diet plans could this meal fall under. I.e. dairy free,
                        gluten free, low fat, low FODMAP... Default is an
                        empty list since a meal could be multiple diet plans.
            rating: What rating you give to the meal. Default is 0.
            servings: How many servings does this recipe make. Default is 0.
            ingredients: List of ingredients. Default is an empty list.
            instructions: List of instructions for making the recipe. Default
                        is an empty list."""
        self.meal_dict = {
            COLUMNS[0]: meal_name,
            COLUMNS[1]: meal_type,
            COLUMNS[2]: diet,
            COLUMNS[3]: rating,
            COLUMNS[4]: servings,
            COLUMNS[5]: ingredients,
            COLUMNS[6]: instructions,
            COLUMNS[7]: notes
        }


def import_csv(filename: str) -> pd.DataFrame:
    """Meal data is stored in CSV files. Check if the provided file exists. If
    it does, read the CSV and turn it to a DataFrame object.
    Arguments:
        filename - name of the CSV to read from.
    returns:
        pd.DataFrame object created by the CSV"""
    if os.path.exists(filename):
        return pd.read_csv(filename)
    else:
        return -1


def export_csv(dataframe: pd.DataFrame, filename: str):
    """Exports the provided DataFrame to the filepath as a CSV.
    Arguments:
        dataframe: pandas DataFrame object wished to be exported to a CSV.
        filename: Filepath to export the data to.
    Return:
        N/A"""
    dataframe.to_csv(filename, index=False)


def add_meal(dataframe: pd.DataFrame, meal: Meal) -> pd.DataFrame:
    """Added a Meal to the DataFrame.
    Arguments:
        dataframe: The pandas DataFrame the Meal should be added to.
        meal: The meal that should be added to the DataFrame"""
    new_row = meal.meal_dict
    return dataframe._append(new_row, ignore_index=True)


def contains_any(dataframe: pd.DataFrame, column_name: str,
                 item_list) -> pd.DataFrame:
    """Search through the DataFrame to find which of the meal entries contain
    any items from within the item_list under the column_name. I.e. search
    through for any meals that contain any of the provided ingredients.
    Arguments:
        dataframe: pandas DataFrame to query
        column_name: Which column of the DataFrame to query
        item_list: The list of items to search for under the column.
    Return:
        A new pandas DataFrame that contains the results of the query."""
    mask = dataframe[column_name].apply(
                                    lambda x: any(g in x for g in item_list))
    return dataframe[mask]


def contains_all(dataframe: pd.DataFrame, column_name: str,
                 item_list) -> pd.DataFrame:
    """Search through the DataFrame to find which of the meal entries contain
    all items from within the item_list under the column_name. I.e. search
    through for any meals that contain all of the provided ingredients.
    Arguments:
        dataframe: pandas DataFrame to query
        column_name: Which column of the DataFrame to query
        item_list: The list of items to search for under the column.
    Return:
        A new pandas DataFrame that contains the results of the query."""
    mask = dataframe[column_name].apply(
                                    lambda x: all(g in x for g in item_list))
    return dataframe[mask]


def edit_meal(dataframe: pd.DataFrame, column_name: str, location: int,
              new_val) -> pd.DataFrame:
    """Edit an existing meal within the DataFrame.
    Arguments:
        dataframe: pandas DataFrame to edit the meal within.
        column_name: Which column of the meal is being edited.
        location: The index the meal lives at within the DataFrame.
        new_val: The new value to write at the location.
    Return:
        New DataFrame that contains the edited Meal."""
    non_lists = ["Meal_Name", "Meal_Type", "Rating"]
    if (column_name in non_lists):
        dataframe[location] = new_val
        return dataframe


if __name__ == "__main__":
    # If file of data exists, read it. Otherwise, create empty dataframe to add items to
    # if (os.path.exists("data_storage.csv")):
    #     df = pd.read_csv("data_storage.csv")
    # else:
    #     df = pd.DataFrame(columns=COLUMNS)
    # COLUMNS = ["Meal_Name", "Meal_Type", "Diet", "Rating", "Servings",
    #        "Ingredients", "Instructions"]
    df = pd.DataFrame(columns=COLUMNS)
    curry = Meal("curry", "dinner", "N/A", 4, 6, ["chicken", "curry paste"], ["Do something", "do nothing"], ["No additional Notes"])
    granola = Meal("granola", "snack", "N/A", 3, 2, ["nuts", "honey", "the goods"], ["Do something", "do nothing"], ["No additional Notes"])
    pancake = Meal("pancake", "breakfast", "N/A", 2, 1, ["krusteaz"], ["Do something", "do nothing"], ["No additional Notes"])

    df = add_meal(df, curry)
    df = add_meal(df, granola)
    df = add_meal(df, pancake)
    #df = pd.read_csv("data_storage.csv")
    #print(df)
    # Querying: https://datagy.io/pandas-query/
    # Search for a meal name
    #queried = df.query('Meal_Name == "curry"', inplace=False)
    #print(queried)
    # Search for if an ingredient exists in any recipes
    #df_filtered = contains_all(df, "Ingredients", ["honey", "nuts"])
    #print(df_filtered)
    # Search if any ingredients in the list is in any recipes
    #df_filtered = contains_any(df, "Instructions", ["do nothing", "bleh"])
    #print(df_filtered)
    # Before closing, export list
    df.to_csv("data_storage.csv", index=False)