def remove_rotten(bag_of_fruits):
    if type(bag_of_fruits) != type(list()):
        return []
    bag_of_fruits = str(bag_of_fruits)
    bag_of_fruits = bag_of_fruits.replace('rotten', '')
    bag_of_fruits = bag_of_fruits.lower()
    bag_of_fruits = eval(bag_of_fruits)
    return bag_of_fruits
bag_of_fruits = ['rottenApple', 'rottenBanana', 'rottenApple', 'rottenPineapple', 'rottenKiwi']
print(remove_rotten(bag_of_fruits))




