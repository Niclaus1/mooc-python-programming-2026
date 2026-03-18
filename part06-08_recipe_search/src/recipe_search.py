# Write your solution here
def search_by_name(filename: str, word: str):
    food_recipe = get_data(filename)
    
    food_list = []
    for food in food_recipe:
        if word in food[0].lower():
            food_list.append(food[0])
    return food_list

def search_by_time(filename : str, time: int):
    food_recipe = get_data(filename)

    food_list = []
    for food in food_recipe:
        if time >= int(food[1]):
            food_list.append(f'{food[0]}, preparation time {food[1]} min')
    return food_list

def search_by_ingredient(filename : str, ingredient : str):
    food_recipe = get_data(filename)
    
    food_list = []
    for food in food_recipe:
        if ingredient in food:
            food_list.append(f'{food[0]}, preparation time {food[1]} min')
            
    return food_list

def get_data(filename: str):
    recipes = []
    with open (filename) as new_file:
        current_recipe = []
        for line in new_file:
            line = line.strip()
            
            if line == "":
                recipes.append(current_recipe)
                current_recipe = []
            else:
                current_recipe.append(line)
        recipes.append(current_recipe)
    return recipes

if __name__ == "__main__":
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)