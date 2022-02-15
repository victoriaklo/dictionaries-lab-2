"""Restaurant rating lister."""

# put your code here
def read_ratings(file):
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

    restaurant_file = open(file)

    rest_and_ratings = {}
    rest_and_ratings[new_restaurant] = new_rating

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
    
    restaurant_file.close()


read_ratings("scores.txt")
# Modify the script so that it validates the score users provide when they add a new restaurant and rating. 
# The rating must be an integer between 1 and 5 (inclusive). 
# If they enter something invalid, the script should prompt them again.