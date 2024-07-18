"""THE DATA PROCESSING IS CARRIED OUT BY THE PROCESS MODULE.
 IT HAS FUNCTIONS THAT TAKE IN THE ENTIRE DATASET AND CARRY OUT THE REQUIRED OPERATIONS
 TO PRODUCE THE DESIRED RESULT IN THE EXPECTED FORMAT.
 TO ENSURE PROPER MODULE FUNCTIONALITY, THE PACKAGES JSON AND CSV ARE REQUIRED TO BE IMPORTED."""
import csv
import tui
from reviewfunctions import review_stats

"""get_disneyland_reviews_file() - This function reads a dataset. The CSV file is read using the built-in "with" 
function and then converted into a list. This function is called for each task."""


def get_disneyland_reviews_file():
    my_list = []
    with open('disneyland_reviews.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            my_list.append(row)
    return my_list


data = get_disneyland_reviews_file()

"""reviews_by_park() - This function displays specific park reviews. It processes information collected from the user 
in the TUI module, returns the required information and informs the user about any errors input."""


def reviews_by_park():
    park = tui.park_input()
    error_park = tui.park_error()
    if park == 'hongkong' or park == 'hong kong':
        for values in data:
            if values[4] == 'Disneyland_HongKong':
                print(values)
        tui.main_menu()
    elif park == 'california':
        for values in data:
            if values[4] == 'Disneyland_California':
                print(values)
        tui.main_menu()
    elif park == 'paris':
        for values in data:
            if values[4] == 'Disneyland_Paris':
                print(values)
        tui.main_menu()
    else:
        print(error_park)
        reviews_by_park()


"""reviews_by_park_and_reviewer_location() - This function processes data and displays user-selected information
 about the park's opinion based on the reviewer's location and informs the user about any errors input."""


def reviews_by_park_and_reviewer_location():
    park = tui.park_input()
    location = tui.location_input()
    answer_location = tui.location_output()
    error_park = tui.park_error()
    error_loc = tui.location_error()
    if park == 'hongkong' or park == 'hong kong':
        i = 0
        for values in data:
            if values[4] == 'Disneyland_HongKong' and values[3] == location:
                i += 1
        if i == 0:
            print(error_loc)
            reviews_by_park_and_reviewer_location()
        else:
            print(answer_location + str(i))
        tui.main_menu()
    elif park == 'california':
        i = 0
        for values in data:
            if values[4] == 'Disneyland_California' and values[3] == location:
                i += 1
        if i == 0:
            print(error_loc)
            reviews_by_park_and_reviewer_location()
        else:
            print(answer_location + str(i))
        tui.main_menu()
    elif park == 'paris':
        i = 0
        for values in data:
            if values[4] == 'Disneyland_Paris' and values[3] == location:
                i += 1
        if i == 0:
            print(error_loc)
            reviews_by_park_and_reviewer_location()
        else:
            print(answer_location + str(i))
        tui.main_menu()
    else:
        print(error_park)
        reviews_by_park_and_reviewer_location()


"""average_score_per_year_by_park() - This function processes data and displays user-selected information
 about the park's average rating score based on the selected year and informs the user about any errors input."""


def average_score_per_year_by_park():
    park = tui.park_input()
    year = tui.year_input()
    answer_year = tui.year_output()
    error_park = tui.park_error()
    error_loc = tui.location_error()
    if park == 'hongkong' or park == 'hong kong':
        rating_len = 0
        rating_sum = 0
        for values in data:
            four_char = values[2]
            rating = values[1]
            if values[4] == 'Disneyland_HongKong' and four_char[:4] == year:
                rating_len += 1
                for column in rating:
                    rating_sum += float(column)
        if rating_len == 0:
            print(error_loc)
            reviews_by_park_and_reviewer_location()
        else:
            print(answer_year + str(round(rating_sum / rating_len, 2)))
        tui.main_menu()
    elif park == 'california':
        rating_len = 0
        rating_sum = 0
        for values in data:
            four_char = values[2]
            rating = values[1]
            if values[4] == 'Disneyland_California' and four_char[:4] == year:
                rating_len += 1
                for column in rating:
                    rating_sum += float(column)
        if rating_len == 0:
            print(error_loc)
            reviews_by_park_and_reviewer_location()
        else:
            print(answer_year + str(round(rating_sum / rating_len, 2)))
        tui.main_menu()
    elif park == 'paris':
        rating_len = 0
        rating_sum = 0
        for values in data:
            four_char = values[2]
            rating = values[1]
            if values[4] == 'Disneyland_Paris' and four_char[:4] == year:
                rating_len += 1
                for column in rating:
                    rating_sum += float(column)
        if rating_len == 0:
            print(error_loc)
            reviews_by_park_and_reviewer_location()
        else:
            print(answer_year + str(round(rating_sum / rating_len, 2)))
        tui.main_menu()
    else:
        print(error_park)
        average_score_per_year_by_park()


"""average_score_per_park_by_reviewer_location() - This function processes data and displays user-selected
 information about the park's average score based on the selected reviewer location and informs the user 
 about any errors input."""


def average_score_per_park_by_reviewer_location():
    rating_sum_hongkong = {}
    location_sum_hongkong = {}
    average_scores_hongkong = {}
    rating_sum_california = {}
    location_sum_california = {}
    average_scores_california = {}
    rating_sum_paris = {}
    location_sum_paris = {}
    average_scores_paris = {}

    for column in data:
        if column[4] == 'Disneyland_HongKong':
            reviewer_location = column[3]
            rating = column[1]
            if reviewer_location not in rating_sum_hongkong:
                rating_sum_hongkong[reviewer_location] = int(rating)
                location_sum_hongkong[reviewer_location] = 1
            else:
                rating_sum_hongkong[reviewer_location] += int(rating)
                location_sum_hongkong[reviewer_location] += 1
                average_scores_hongkong[reviewer_location] = (round(rating_sum_hongkong[reviewer_location] /
                                                                    location_sum_hongkong[reviewer_location], 2))

        if column[4] == 'Disneyland_California':
            reviewer_location = column[3]
            rating = column[1]
            if reviewer_location not in rating_sum_california:
                rating_sum_california[reviewer_location] = int(rating)
                location_sum_california[reviewer_location] = 1
            else:
                rating_sum_california[reviewer_location] += int(rating)
                location_sum_california[reviewer_location] += 1
                average_scores_california[reviewer_location] = (round(rating_sum_california[reviewer_location] /
                                                                      location_sum_california[reviewer_location], 2))

        if column[4] == 'Disneyland_Paris':
            reviewer_location = column[3]
            rating = column[1]
            if reviewer_location not in rating_sum_paris:
                rating_sum_paris[reviewer_location] = int(rating)
                location_sum_paris[reviewer_location] = 1
            else:
                rating_sum_paris[reviewer_location] += int(rating)
                location_sum_paris[reviewer_location] += 1
                average_scores_paris[reviewer_location] = (round(rating_sum_paris[reviewer_location] /
                                                                 location_sum_paris[reviewer_location], 2))

    print('LOCATION                 Hongkong        California      Paris')
    print('--------------------------------------------------------------')

    merged_dict = {
        k: [average_scores_hongkong.get(k, 0), average_scores_california.get(k, 0), average_scores_paris.get(k, 0)]
        for k in set(average_scores_hongkong) | set(average_scores_california) | set(average_scores_paris)}

    sort_dict = dict(sorted(merged_dict.items(), key=lambda x: x[0].lower()))
    for k, v in sort_dict.items():
        print("{:<25} {:<15} {:<15} {:<10}".format(k, v[0], v[1], v[2]))
    tui.main_menu()


"""data {} - This dictionary is created from the processed data and the user converts it into various file formats."""
data_dictionary = {
    "Number of reviews Hongkong": review_stats.number_of_reviews('Disneyland_HongKong'),
    "Number of reviews California": review_stats.number_of_reviews('Disneyland_California'),
    "Number of reviews Paris": review_stats.number_of_reviews('Disneyland_Paris'),
    "Number of positive reviews Hongkong": review_stats.number_of_positive_reviews('Disneyland_HongKong'),
    "Number of positive reviews California": review_stats.number_of_positive_reviews('Disneyland_California'),
    "Number of positive reviews Paris": review_stats.number_of_positive_reviews('Disneyland_Paris'),
    "Average review score Hongkong": review_stats.average_score('Disneyland_HongKong'),
    "Average review score California": review_stats.average_score('Disneyland_California'),
    "Average review score Paris": review_stats.average_score('Disneyland_Paris'),
    "Number of countries that have reviewed Hongkong": review_stats.number_of_countries('Disneyland_HongKong'),
    "Number of countries that have reviewed California": review_stats.number_of_countries('Disneyland_California'),
    "Number of countries that have reviewed Paris": review_stats.number_of_countries('Disneyland_Paris'),
}

part_one, part_two = [], []

"""dict_to_csv(x) - This function uses a loop to split the database into separate lists."""


def dict_to_csv(x):
    for k in x:
        part_one.append(k)
        part_two.append(x[k])

    return part_one, part_two
