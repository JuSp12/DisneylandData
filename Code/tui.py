"""THE TUI MODULE IS IN CHARGE OF INTERACTION.
 THE FUNCTIONALITIES OF THIS MODULE ARE MAINLY TO DISPLAY MENUS AND CONTAINS BASIC FUNCTIONS.
 RECEIVES INFORMATION FROM THE USER AND PROVIDES AN APPROPRIATE OUTCOME TO CREATE A SMOOTH INTERFACE.
 PROCESS AND VISUAL MODULE FUNCTIONS HAVE BEEN IMPORTED."""
import process
import visual
import output

global park, location, year

"""welcome_text() - This function is used to display the welcome message to the user."""


def welcome_text(title):
    print()
    print("-" * len(title))
    print(title)
    print("-" * len(title))


""" print_data() - This function imports functions from the PROCESS module. Displays information about the 
completion of reading data and the amount of data from the file."""


def print_data(amount):
    print("\nThe Program has finished reading in the dataset.")
    print(f"The Total amount of Reviews is {amount - 1}.\n")


"""park_input() - This function gets the user park choice input."""


def park_input():
    global park
    park = input("Which park you would like to see? Hongkong / California / Paris \n").lower()
    return park


"""location_input() - This function gets the user location choice input."""


def location_input():
    global location
    location = input("Which reviewers location you wish to see the reviews for? ").capitalize()
    return location


"""year_input() - This function gets the user year choice input."""


def year_input():
    global year
    year = input("Which year you wish to see the reviews for? ")
    return year


"""location_output() - This function gives the user location choice output for a specific park."""


def location_output():
    output_location = f"The Total amount of Reviews for a {park} Disneyland and reviewer location {location} is: "
    return output_location


"""year_output() - This function gives the user year choice output for a specific park."""


def year_output():
    output_year = f"The average rating for the {park} Disneyland in {year} is: "
    return output_year


"""menu_error(), location_error(), park_error(), format_error() - 
This function displays information about the user incorrect/invalid input."""


def menu_error():
    error = "\nYou have entered an invalid menu choice. "
    return error


def location_error():
    error_loc = "\nThere is no reviews from this location or you have entered an invalid location. "
    return error_loc


def park_error():
    error_park = "\nYou have entered an invalid park name. "
    return error_park


def format_error():
    error_form = "\nYou have entered an invalid file format. "
    return error_form


"""main_menu() - This function displays the main menu."""


def main_menu():
    print("\nPlease enter the letter which corresponds with your desired menu choice: ")
    print("[A] View Data")
    print("[B] Visualize Data")
    print("[C] Output the Data")
    print("[X] Exit")
    menu_selection()


"""main_selection() - This function allows user to select a particular option from the main menu.
 The task is to collect the appropriate data and display the required information using internal functions.
 A loop allows the user to return to the beginning of the function during erroneous input.
 If statements allow the user to enter multiple decisions under conditions."""


def menu_selection():
    while True:
        user_menu_selection = input().lower()
        if user_menu_selection == 'a':
            print("Selection A: View Data. ")
            submenu_view_data()
        elif user_menu_selection == 'b':
            print("Selection B: Visualize Data. ")
            submenu_visualize_data()
        elif user_menu_selection == 'c':
            print("Selection C: Output the Data. ")
            output.out.export()
            main_menu()
        elif user_menu_selection == 'x':
            print("Selection X: Exit. Bye!")
            break
        else:
            print(menu_error())
            main_menu()
    exit()


"""submenu_view_data() - This function displays the first submenu"""


def submenu_view_data():
    print("\nPlease enter one of the following option: ")
    print("[A] View Reviews by Park. ")
    print("[B] Number of Reviews by Park and by Reviewer Location. ")
    print("[C] Average Score per Year by Park. ")
    print("[D] Average Score per Park by Reviewer Location. ")
    submenu_view_selection()


""" submenu_view_selection() - This function allows user to select a option and imports internal and 
external functions from the PROCESS module."""


def submenu_view_selection():
    user_submenu_a_selection = input().lower()
    if user_submenu_a_selection == 'a':
        print("Selection A: View Reviews by Park. \n")
        process.reviews_by_park()
    elif user_submenu_a_selection == 'b':
        print("Selection B: Number of Reviews by Park and by Reviewer Location. \n")
        process.reviews_by_park_and_reviewer_location()
    elif user_submenu_a_selection == 'c':
        print("Selection C: Average Score per Year by Park. \n")
        process.average_score_per_year_by_park()
    elif user_submenu_a_selection == 'd':
        print("Selection D: Average Score per Park by Reviewer Location. \n")
        process.average_score_per_park_by_reviewer_location()
    else:
        print(menu_error())
        submenu_view_data()


"""submenu_visualize_data() - This function displays the second submenu"""


def submenu_visualize_data():
    print("\nPlease enter one of the following option: ")
    print("[A] Most Review Park. ")
    print("[B] Average Scores. ")
    print("[C] Park Ranking by Nationality. ")
    print("[D] Most Popular Month by Park. ")
    submenu_visualize_selection()


"""submenu_visualize_selection() - This function allows user to select a option and imports internal and 
external functions from the VISUAL module."""


def submenu_visualize_selection():
    user_submenu_b_selection = input().lower()
    if user_submenu_b_selection == 'a':
        print("Selection A: Most Review Park. \n")
        visual.most_review_park_pie_chart()
        main_menu()
    elif user_submenu_b_selection == 'b':
        print("Selection B: Average Scores. \n")
        visual.average_scores_bar_chart()
        main_menu()
    elif user_submenu_b_selection == 'c':
        print("Selection C: Park Ranking by Nationality. \n")
        visual.ranking_by_nationality_bar_chart()
        main_menu()
    elif user_submenu_b_selection == 'd':
        print("Selection D: Most Popular Month by Park. \n")
        visual.most_popular_month_by_park_bar_chart()
        main_menu()
    else:
        print(menu_error())
        submenu_visualize_data()
