import pandas as pd

pizza_data = pd.read_csv('IN3067-INM713_coursework_data_pizza_8358_1_reduced.csv')

print(pizza_data.value_counts(['menu item', 'item description']))

pizza_data.value_counts('menu item').head(79)

# my_pizzaMenu = set(pizza_data['menu item'])

#my_pizzaMenu = set(pizza_data['menu item'])


#print(pizza.columns)

#print(my_pizzaMenu)

#print(pizza['menu item'].items)