"""Restaurant rating lister."""

scores_file = open("scores.txt")

# put your code here
def read_ratings(file):
    new_restaurant = input("name new restaurant: ")
    new_rating = input("new rating: ")

    
    restaurant_file = open(file)

    rest_and_ratings = {}
    # Reads the ratings in from the file
    for line in restaurant_file:
        line = line.rstrip()
        line = line.split(":")
        restaurant_name, restaurant_rating = line
    # Stores them in a dictionary
        rest_and_ratings[restaurant_name] = restaurant_rating
        rest_and_ratings[new_restaurant] = new_rating
    # Return the ratings in A-Z order by restaurant

    sorted_dict = sorted(rest_and_ratings.items())

    for name, rating in sorted_dict:
        print(f"{name} is rated at {rating}.")
    
    restaurant_file.close()


read_ratings("scores.txt")


 
# Modify your script so that after it reads the scores file from disk, 
# it prompts the user for a new restaurant and rating.

# The program should:

# Prompt the user for a restaurant name

# Prompt the user for a restaurant score

# Store the new restaurant/rating in the dictionary

# Print all of the ratings in alphabetical order (including the new one, of course)