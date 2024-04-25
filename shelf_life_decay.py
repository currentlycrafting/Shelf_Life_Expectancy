

def food_life_expectancy(file_path):
    decay_rate_of_foods_in_days = {}
    with open(file_path, 'r') as shelf_life_file:
        shelf_life_food_category = None


        for food_item_line in shelf_life_file:
            food_item_line = food_item_line.strip()


            if food_item_line.endswith(':'):
                shelf_life_food_category = food_item_line[:-1]
                decay_rate_of_foods_in_days[shelf_life_food_category] = {}


            elif shelf_life_food_category and ':' in food_item_line:
                food_item_expectancy, shelf_life_in_days = food_item_line.split(':')
                decay_rate_of_foods_in_days[shelf_life_food_category][food_item_expectancy.strip()] = int(shelf_life_in_days.strip())

                
    return decay_rate_of_foods_in_days

def food_item_header(file_path, food_item_header):
    result_of_food_items = food_life_expectancy(file_path)
    if food_item_header in result_of_food_items:
        return result_of_food_items[food_item_header]
    else:
        return "Item Category is not found - Options include: (Fruits & Vegetables, Grains, Canned & Packaged Foods, Meat & Seafood, Dairy & Eggs Baking & Cooking)"

def decay_percentage(decay_rate_of_foods_in_days, shelf_days_elapsed, food_item_lookup):
    if food_item_lookup in decay_rate_of_foods_in_days:
        decay_rate = decay_rate_of_foods_in_days[food_item_lookup]
        if shelf_days_elapsed < 0:
            return "Invalid time. Time mustn't be less than Zero."
        else:
            shelf_life_decayed_percentage = (shelf_days_elapsed / decay_rate) * 100
            return shelf_life_decayed_percentage
    else:
        return "Food item not found in Category"


if __name__ == '__main__':
    file_path = 'shelf_life.txt'

    food_inputted_header = input("[Shelf-Life Expectancy] Enter the Food Category: ") 
    print()
    dictionary_of_food_items_storage_dates = food_item_header(file_path, food_inputted_header)
    print(dictionary_of_food_items_storage_dates)
    print()
    food_item_lookup = input("[Shelf-Life Expectancy] Enter desired Food item in category: ")
    shelf_days_elapsed = int(input("[Shelf-Life Expectancy] How many days as the food been on shelf: "))

    food_data_percentage = decay_percentage(dictionary_of_food_items_storage_dates, shelf_days_elapsed, food_item_lookup)

    #Turns the decay rate into percent form
    if isinstance(food_data_percentage, (int, float)):
        if food_data_percentage > 100:
            print("Item is expired")
        else:
            print()
            print(f'Rotten Decay Percentage: {food_data_percentage:.2f}%')
            print()
    else:
        print(food_data_percentage)
