"""THE VISUAL MODULE IS IN CHARGE OF VISUALIZING THE DATA USING THE MATPLOTLIB LIBRARY.
 THE FUNCTIONALITIES OF THIS MODULE ARE MAINLY TO DISPLAY CHARTS
 AND INCLUDE FOUR FUNCTIONS CALLED IN THE SECOND SUBMENU.
 TUI AND PROCESS MODULE FUNCTIONS HAVE BEEN IMPORTED."""
import matplotlib.pyplot as plt
import process
import tui

"""THE SPECIFIC USE OF VARIABLES IN THESE FUNCTIONS COMBINED WITH LOGICALLY ARRANGED CODE VISUALIZED DETAILED CHARTS."""

"""most_review_park_pie_chart() - This function is responsible for displaying the pie chart
 The most review parks are according to the information contained in the CSV file read in the PROCESS module."""


def most_review_park_pie_chart():
    h = 0
    c = 0
    p = 0
    for column in process.data:
        if column[4] == 'Disneyland_HongKong':
            h += 1
        if column[4] == 'Disneyland_California':
            c += 1
        if column[4] == 'Disneyland_Paris':
            p += 1
    park_name = [f'HongKong\n{h}', f'California\n{c}', f'Paris\n{p}']
    plt.pie([h, c, p], labels=park_name, autopct='%1.1f%%')
    plt.title('Disneyland Reviews Summary', fontsize=16)
    plt.show()


"""average_scores_bar_chart() - This function is responsible for displaying the bar chart
The average scores for specific parks are according to the information contained in the CSV file."""


def average_scores_bar_chart():
    rating_len_hongkong = 0
    rating_sum_hongkong = 0
    rating_len_california = 0
    rating_sum_california = 0
    rating_len_paris = 0
    rating_sum_paris = 0
    average_scores_hongkong = 0
    average_scores_california = 0
    average_scores_paris = 0

    for review_rating_hongkong in process.data:
        if review_rating_hongkong[4] == 'Disneyland_HongKong':
            for review in review_rating_hongkong[1]:
                rating_sum_hongkong += int(review)
                rating_len_hongkong += 1
            average_scores_hongkong = rating_sum_hongkong / rating_len_hongkong

    for review_rating_california in process.data:
        if review_rating_california[4] == 'Disneyland_California':
            for review in review_rating_california[1]:
                rating_sum_california += int(review)
                rating_len_california += 1
            average_scores_california = rating_sum_california / rating_len_california

    for review_rating_paris in process.data:
        if review_rating_paris[4] == 'Disneyland_Paris':
            for review in review_rating_paris[1]:
                rating_sum_paris += int(review)
                rating_len_paris += 1
            average_scores_paris = rating_sum_paris / rating_len_paris

    park_name = ['HongKong', 'California', 'Paris']
    average_scores = [average_scores_hongkong, average_scores_california, average_scores_paris]
    plt.title('Disneyland Average Scores', fontsize=16)
    plt.bar(park_name, average_scores)
    plt.show()


"""ranking_by_nationality_bar_chart() - This function is responsible for displaying the bar chart
Ranking by nationality are according to the information contained in the CSV file."""


def ranking_by_nationality_bar_chart():
    rating_sum = {}
    location_sum = {}
    rating_average = {}
    park = tui.park_input()
    error_park = tui.park_error()
    for column in process.data:
        reviewer_location = column[3]
        rating = column[1]
        if park == 'hongkong' or park == 'hong kong':
            if column[4] == 'Disneyland_HongKong':
                if reviewer_location not in rating_sum:
                    rating_sum[reviewer_location] = int(rating)
                    location_sum[reviewer_location] = 1
                else:
                    rating_sum[reviewer_location] += int(rating)
                    location_sum[reviewer_location] += 1

        elif park == 'california':
            if column[4] == 'Disneyland_California':
                if reviewer_location not in rating_sum:
                    rating_sum[reviewer_location] = int(rating)
                    location_sum[reviewer_location] = 1
                else:
                    rating_sum[reviewer_location] += int(rating)
                    location_sum[reviewer_location] += 1

        elif park == 'paris':
            if column[4] == 'Disneyland_Paris':
                if reviewer_location not in rating_sum:
                    rating_sum[reviewer_location] = int(rating)
                    location_sum[reviewer_location] = 1
                else:
                    rating_sum[reviewer_location] += int(rating)
                    location_sum[reviewer_location] += 1

        else:
            print(error_park)
            ranking_by_nationality_bar_chart()
            tui.main_menu()

    for reviewer_location, total_rating in rating_sum.items():
        rating_average[reviewer_location] = total_rating / location_sum[reviewer_location]

    count_list = []

    for reviewer_location in rating_average:
        count_list.append([reviewer_location, rating_average[reviewer_location]])

    count_list = sorted(rating_average.items(), key=lambda x: x[1], reverse=True)

    keys = []
    values = []

    for i in range(0, 10):
        keys.append(count_list[i][0])
        values.append(count_list[i][1])

    plt.figure(figsize=(15, 5))
    bars = (plt.bar(keys, values))
    max_value = values.index(max(values))
    bars[max_value].set_color('red')
    min_value = values.index(min(values))
    bars[min_value].set_color('green')
    plt.title(f'{park.capitalize()} Disneyland Nationality Ranking', fontsize=16)
    plt.show()


"""most_popular_month_by_park_bar_chart() - This function is responsible for displaying the bar chart
 The most popular month by park are according to the information contained in the CSV file."""


def most_popular_month_by_park_bar_chart():
    rating_sum = {}
    month_sum = {}
    rating_average = {}
    park = tui.park_input()
    error_park = tui.park_error()
    for column in process.data:
        year_months = column[2]
        rating = column[1]
        months = year_months[5:]
        if park == 'hongkong' or park == 'hong kong':
            if column[4] == 'Disneyland_HongKong' and year_months != 'missing':
                if months not in rating_sum:
                    rating_sum[months] = int(rating)
                    month_sum[months] = 1
                else:
                    rating_sum[months] += int(rating)
                    month_sum[months] += 1

        elif park == 'california':
            if column[4] == 'Disneyland_California' and year_months != 'missing':
                if months not in rating_sum:
                    rating_sum[months] = int(rating)
                    month_sum[months] = 1
                else:
                    rating_sum[months] += int(rating)
                    month_sum[months] += 1

        elif park == 'paris':
            if column[4] == 'Disneyland_Paris' and year_months != 'missing':
                if months not in rating_sum:
                    rating_sum[months] = int(rating)
                    month_sum[months] = 1
                else:
                    rating_sum[months] += int(rating)
                    month_sum[months] += 1

        else:
            print(error_park)
            most_popular_month_by_park_bar_chart()
            tui.main_menu()

    for months, total_rating in rating_sum.items():
        rating_average[months] = total_rating / month_sum[months]

    months_name = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May',
                   '6': 'June', '7': 'July', '8': 'August', '9': 'September', '10': 'October',
                   '11': 'November', '12': 'December'}

    months_sort = {}
    for i in months_name:
        months_sort[months_name[i]] = rating_average[i]

    keys = list(months_sort.keys())
    values = list(months_sort.values())

    plt.figure(figsize=(15, 5))
    bars = (plt.bar(range(len(months_sort)), values, tick_label=keys))
    max_value = values.index(max(values))
    bars[max_value].set_color('red')
    min_value = values.index(min(values))
    bars[min_value].set_color('green')
    plt.title(f'{park.capitalize()} Disneyland Popularity by Month', fontsize=16)
    plt.show()
