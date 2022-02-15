"""Restaurant rating lister."""
def read_rest_ratings(file):
    restaurant_file = open(file)

    rest_and_ratings = {}
    # rest_and_ratings[new_restaurant] = new_rating

    # Reads the ratings in from the file
    for line in restaurant_file:
        line = line.rstrip()
        line = line.split(":")
        restaurant_name, restaurant_rating = line

    # Stores them in a dictionary
        rest_and_ratings[restaurant_name] = restaurant_rating

    # Return the ratings in A-Z order by restaurant

    sorted_tuple = sorted(rest_and_ratings.items())

    for name, rating in sorted_tuple:
        print(f"{name} is rated at {rating}.")
    
    return rest_and_ratings
    restaurant_file.close()




def update_rest_ratings(file):
    new_restaurant = input("name new restaurant: ")

    while True:
        new_rating = input("new rating: ")
    
        try:
            int_new_rating = int(new_rating)
            if int_new_rating < 1 or int_new_rating > 5:
                print("Please enter valid num between 1-5")
                continue
            else:
                break
        except ValueError:
            print("Please enter valid num between 1-5")
            continue
        
    updated_dict = read_rest_ratings(file)
    updated_dict[new_restaurant] = new_rating

    sorted_updated_tuple= sorted(updated_dict.items())

    for name, rating in sorted_updated_tuple:
        print(f"{name} is rated at {rating}.")

        


def ask_user():
    while True:
        user_choice = input(" [1] See all restaurant ratings\n [2] Add and rate a new restaurant\n [q] to quit \n --------\n")
        

        if user_choice == "1":
            read_rest_ratings("scores.txt")
            continue
        elif user_choice == "2":
            update_rest_ratings("scores.txt")
            continue
        elif user_choice == "q":
            print("You will exit the program")
            break
        else:
            continue

ask_user()
