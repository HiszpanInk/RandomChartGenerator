import pandas as pd
import matplotlib.pyplot as plt
import random
from configuration import listOfCountries

from configuration import ramdomDataMax

def randomPieChart(title):
    recordsNum = random.randint(1, 5)
    selectedCountries = []
    print(title, "\n")
    selectedCountries = listOfCountries
    random.shuffle(selectedCountries)
    selectedCountries = selectedCountries[:recordsNum]
    data = []
    for y in range(0, recordsNum):
        print(selectedCountries[y])  
        newDataRecord = random.random() + 1
        data.append(newDataRecord)      
    print(selectedCountries)
    print(data)
    
    
    df = pd.DataFrame({title: data},
                    index=selectedCountries)
    plot = df.plot.pie(y=title, figsize=(5, 5))
    fig = plot.get_figure()
    fig.savefig("myplot.png")
    

def __main__():
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
                    #plan na ten: bierzemy datę, generujemy liczbę, w dni tygodnia do soboty włącznie zwiększa się statystyka, niedzielę i poniedziałek - zmniejsza
                    #jeszcze można dodać generowanie na podstawie liczby wpisanej przez użytkownika jako dzisiejsza
            else:
                print("There is no such option you know")
        else:
                print("There is no such option you know")

__main__()