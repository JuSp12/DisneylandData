import process

"""OBJECT-ORIENTED PROGRAMMING IMPLEMENTATION"""

"""class ReviewFunctions - This class processing data for all three parks and contains five methods:
 - Number of reviews,
 - Number of positive reviews,
 - Average review score,
 - Number of countries that have reviewed each park.
 The processed data is returned under option C in the main menu."""


class ReviewFunctions:

    @classmethod
    def number_of_reviews(cls, park):
        park_amount = 0
        for values in process.data:
            if values[4] == park:
                park_amount += 1
        return park_amount

    @classmethod
    def number_of_positive_reviews(cls, park):
        positive_amount = 0
        for values in process.data:
            if values[4] == park and int(values[1]) >= 4:
                positive_amount += 1
        return positive_amount

    @classmethod
    def average_score(cls, park):
        rating_len = 0
        rating_sum = 0
        for values in process.data:
            rating = values[1]
            if values[4] == park:
                rating_len += 1
                for column in rating:
                    rating_sum += float(column)
        return round(rating_sum / rating_len, 2) if rating_len > 0 else 0

    @classmethod
    def number_of_countries(cls, park):
        location_amount = {}
        location_sum = {}
        for column in process.data:
            if column[4] == park:
                location_list = column[3]
                if location_list not in location_amount:
                    location_sum[location_list] = 1
        return len(list(location_sum.keys()))


review_stats = ReviewFunctions()
