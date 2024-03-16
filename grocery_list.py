'''
Ryan Cheng
10/1/23
Sources: None
Reflection: I felt pretty comfortable with this assignment. I'm a huge fan of try and except or catch,
            however one likes to put it, so it was great being able to use it to handle the error of
            trying to remove something from a list when it doesn't exist. Also becoming a bigger and
            bigger fan of formatted strings by the day. So much easier than " and + all the time.
On my honor, I have neither given nor received unauthorized aid: Ryan Cheng
'''

# initialization
grocery_list = []

# meant to reduce repetitive code
def get_item(prompt):
    while True:
        item = input(prompt).lower().strip()
        if item == "":
            print("You did not enter anything. Please try again.")
        elif not item.isalpha:
            print("You entered a non-letter. Please try again.")
        else:
            return item

# meant to reduce repetitive code
def show_list(title):
    print(title)
    for item in grocery_list:
        print(f" - {item}")

# execution
print("Welcome! This program will help you create a grocery list.")

while True:
    action = input("Choose an action: (1) add an item, (2) remove an item, (3) see your list, or (4) quit ").lower().strip()
    if action == "1":
        # add to grocery list
        grocery_list.append(get_item("Add an item: "))
    elif action == "2":
        item = get_item("Remove an item: ")
        # try to remove from grocery list
        try:
            grocery_list.remove(item)
        except ValueError:
            # if item doesn't exist, catch the error here and handle it gracefully
            print(f"The item {item} doesn't exist in the grocery list. Please try removing something else.")
    elif action == "3":
        show_list("Here's your grocery list so far:")
    elif action == "4":
        break
    else:
        print("You entered something other than actions (1), (2), (3), or (4). Please try again.")

print("Thanks for using this program.")
show_list("Here's your final grocery list:")