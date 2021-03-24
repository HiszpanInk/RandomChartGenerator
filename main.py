import pandas as pd
import matplotlib.pyplot as plt
import random
from configuration import listOfCountries

def randomPieChart(title):
    recordsNum = random.randint(1, 5)
    selectedCountries = []
    print(title, "\n")
    selectedCountries = random.sample(listOfCountries, recordsNum)
    for y in range(0, recordsNum):
        print(selectedCountries[y])  

    """
    df = pd.DataFrame({'mass': [0.330, 4.87 , 5.97],
                   'radius': [2439.7, 6051.8, 6378.1]},
                  index=['Mercury', 'Venus', 'Earth'])
    plot = df.plot.pie(y='mass', figsize=(5, 5))
    """


def __main__():
    print("gówno")
    while True:
        print("""
        RandomChartGenerator
        Menu
        0 - Exit Program
        1 - Generate random pie chart
        2137 - Generate random COVID stats
        """)
        menuChoice = input("Select positon from menu: ")
        if str.isdigit(menuChoice):
            menuChoice = int(menuChoice)
            if menuChoice == 0:
                break
            elif (menuChoice >= 1 and menuChoice <= 1 or menuChoice == 2137):
                title = input("Add some title to your chart: ")
                if menuChoice == 1:
                    randomPieChart(title)
                if menuChoice == 2137:
                    print("I am sorry, I didn't add this option yet, please be patient")
            else:
                print("There is no such option you know")
        else:
                print("There is no such option you know")

__main__()