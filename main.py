# ----------------Visitors Guide Neptune Zoo-------------------*/

"""
You are to write a program that guides visitors to a zoo. The visitor must be able to input
date and time interval before the visit, and the program must print out which animals are expected
be awake, and when these animals are fed (if the feeding falls during the visit).
for example, it can look like this:What date do you want to visit Neptune Zoo? 21 June
The zoo is open between 06:00 and 23:00.
What time do you want to come? 13-16
During your visit you can see:
Bear
Sea lions *** are fed at 2pm ***
Seal *** is fed at 2pm ***
Wolf
Moose

Information about the animals' wake times must be stored on file, for example in the following format:
name / Hibernation /waking time / feeding time
Bear / winter / 9-20 / 12
Sloth / summer / 12-14 /
13 Night owl / - / 21-05 /
21 Sea lion/ - / 6-18 /
14 Sell ​​/ - / 6-18 /
14 Wolf / - / 6-20 /
12 moose / - / 7-19 / 10

"""

import datetime  # Used For date and Time formats
import pandas as pd  # Used to make a Dataframe from Excel File
from colorama import Fore  # Used for the colors in the text
from datetime import datetime as dt

class Guide:
    def __init__(self):
        self.date = None
        self.time = None
        self.dataframe = None
        self.In_time = 6
        self.Out_time = 23
        self.month = None
        self.summer_start = 3
        self.summer_end = 9

        # Input function for Date and Time inputs

    def input(self):
        print(Fore.GREEN + "=> What date do you want to visit Neptune Zoo?")
        date_entry = input(Fore.BLUE + '=> Enter a date in MM-DD format:')
        self.month, day = map(int, date_entry.split('-'))
        self.date = datetime.date(2022, self.month, day)

        print(Fore.GREEN + "=> What time do you want to come?")
        self.time = int(input(Fore.BLUE + '=> Enter Hours in hh format:'))

        self.Read()
        self.Available_animals()

    # Read function to read text file which has the data
    def Read(self):
        data = 'Zoo.txt'
        self.dataframe = pd.read_csv(data, sep=',')

    # Function for the available animals and there feeding times
    def Available_animals(self):
        if self.In_time <= self.time <= self.Out_time:
            print(Fore.GREEN + "\n\n", "=" * 20, "Wow! The Zoo will be Open", "=" * 20)
            print(Fore.BLUE + "\nDuring your visit you can see\n")
            for i in range(len(self.dataframe)):
                if self.time >= int(self.dataframe["waking time"][i]):
                    if int(self.dataframe["feeding time"][i]) == self.time:
                        if self.summer_start <= self.month <= self.summer_end:
                            if str(self.dataframe["Hibernation"][i]) == "winter":
                                d = dt.strptime(str(self.dataframe["feeding time"][i]), "%H")

                                print(Fore.BLUE + "=>", self.dataframe["Name"][i], Fore.RED + "*** fed at",
                                      d.strftime("%I:%M %p"), "***")
                            elif str(self.dataframe["Hibernation"][i]) == "-":
                                d = dt.strptime(str(self.dataframe["feeding time"][i]), "%H")

                                print(Fore.BLUE + "=>", self.dataframe["Name"][i], Fore.RED + "*** fed at",
                                      d.strftime("%I:%M %p"), "***")
                        else:
                            if str(self.dataframe["Hibernation"][i]) == "summer":
                                d = dt.strptime(str(self.dataframe["feeding time"][i]), "%H")

                                print(Fore.BLUE + "=>", self.dataframe["Name"][i], Fore.RED + "*** fed at",
                                      d.strftime("%I:%M %p"), "***")
                            elif str(self.dataframe["Hibernation"][i]) == "-":
                                d = dt.strptime(str(self.dataframe["feeding time"][i]), "%H")

                                print(Fore.BLUE + "=>", self.dataframe["Name"][i], Fore.RED + "*** fed at",
                                      d.strftime("%I:%M %p"), "***")

                    else:
                        if self.summer_start <= self.month <= self.summer_end:
                            if str(self.dataframe["Hibernation"][i]) == "winter":
                                print(Fore.BLUE + "=>", self.dataframe["Name"][i])
                            elif str(self.dataframe["Hibernation"][i]) == "-":
                                print(Fore.BLUE + "=>", self.dataframe["Name"][i])
                        else:
                            if str(self.dataframe["Hibernation"][i]) == "summer":
                                print(Fore.BLUE + "=>", self.dataframe["Name"][i])
                            elif str(self.dataframe["Hibernation"][i]) == "-":
                                print(Fore.BLUE + "=>", self.dataframe["Name"][i])
        else:
            print("\nSorry we are Closed!")
            print("The zoo is open between 06:00 and 23:00.")


# main
if __name__ == "__main__":
    print(Fore.BLUE + "=" * 20, "Visitors Guide Neptune Zoo", 20 * "=", "\n")
    Object = Guide()
    Object.input()
