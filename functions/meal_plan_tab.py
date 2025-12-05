import tkinter as tk
from tkinter import ttk


class MealPlanTab(ttk.Frame):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    def __init__(self, parent, screenWidth, screenHeight):
        super().__init__(parent, width = screenWidth, height=screenHeight)

        # |            | Sunday     | Monday     | ... | Saturaday  |
        # | Breakfast: | Text Field | Text Field | ... | Text Field |
        # | Lunch:     | Text Field | Text Field | ... | Text Field |
        # | Dinner:    | Text Field | Text Field | ... | Text Field |
        # | Snacks:    | Text Field | Text Field | ... | Text Field |
        # | Dessert:   | Text Field | Text Field | ... | Text Field |

        # Basically, create a grit of 8x6.
        # In column 1, Add lable, in column 2, add Entry
        self.breakfastLabel = ttk.Label(self, text="Breakfast").grid(column='0', row='1')
        self.lunchLabel = ttk.Label(self, text="Lunch").grid(column='0', row='2')
        self.dinnerLabel = ttk.Label(self, text="Dinner").grid(column='0', row='3')
        self.snacksLabel = ttk.Label(self, text="Snacks").grid(column='0', row='4')
        self.dessertLabel = ttk.Label(self, text="Dessert").grid(column='0', row='5')
        for i in range(7):
            self._add_day_plan(i)

    def _add_day_plan(self, dayNum):
        column = str(dayNum + 1)
        self.label = ttk.Label(self, text=self.days[dayNum]).grid(column=column, row='0')
    
        self.breakfastEntry = ttk.Entry(self).grid(column=column, row='1')
        self.lunchEntry = ttk.Entry(self).grid(column=column, row='2')
        self.dinnerEntry = ttk.Entry(self).grid(column=column, row='3')
        self.snacksEntry = ttk.Entry(self).grid(column=column, row='4')
        self.dessertEntry = ttk.Entry(self).grid(column=column, row='5')