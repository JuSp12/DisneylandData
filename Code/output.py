import json
import csv
import tui
import process
"""OBJECT-ORIENTED PROGRAMMING IMPLEMENTATION"""

"""class Output - This class initializes the data export method."""


class Output:
    def __init__(self, download):
        self.download = download

    """export(self) - This method exports the dictionary to a specific file format selected by the user."""

    def export(self):
        self.download = input('Which file format would you like to output? ')
        error_form = tui.format_error()
        if self.download == "json":
            json_object = json.dumps(process.data_dictionary, indent=4)
            with open("review.json", "w") as outfile:  # writing dictionary as json format
                outfile.write(json_object)
            print("Output written to review.json")
            tui.main_menu()

        elif self.download == "csv":
            with open("review.csv", "w") as outfile:
                write = csv.writer(outfile)
                f, e = process.dict_to_csv(process.data_dictionary)  # use of dict_to_csv function
                write.writerow(f)
                write.writerow(e)
            print("Output written to review.csv")
            tui.main_menu()

        elif self.download == "txt":
            with open("review.txt", 'w') as outfile:
                for key, value in process.data_dictionary.items():
                    outfile.write('%s: %s\n' % (key, value))
            print("Output written to review.txt")
            tui.main_menu()

        else:
            print(error_form)
            out.export()


out = Output("json")
