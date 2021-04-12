from configuration import listOfCountries
from configuration import listOfColors
from configuration import randomDataMax
from configuration import randomDataMin
import pandas as pd
import matplotlib.pyplot as plt
import random
import numpy as np
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from PIL import Image
#funkcja do generowania losowych wykresów kołowych

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def randomPieChart(title):
    #wybór indeksów
    selectedIndexes = []

    indexDataChoice = input("If you want to randomly select countries to be indexes - press 1 and enter, if you want manually enter indexes press 2 and enter: ")
    if str.isdigit(indexDataChoice):
        indexDataChoice = int(indexDataChoice)
        if indexDataChoice == 1:
            randomisedCountryNumberChoice = input("If you want to number of countries to be randomised enter 1, if you want the specify how many countries you want to have in the graph - enter 2: ")
            if str.isdigit(randomisedCountryNumberChoice):
                randomisedCountryNumberChoice = int(randomisedCountryNumberChoice)
                if randomisedCountryNumberChoice == 1:
                    print("przypisanie")
                    recordsNum = random.randint(1, len(listOfCountries))
                    selectedIndexes = listOfCountries
                    random.shuffle(selectedIndexes)
                    selectedIndexes = selectedIndexes[:recordsNum]
                elif randomisedCountryNumberChoice == 2:
                    isNumOfCountriesSet = False
                    while isNumOfCountriesSet == False:
                        recordsNumInput = input("Enter number of countries you want to chose: ")
                        if str.isdigit(recordsNumInput):
                            recordsNum = int(recordsNumInput)
                            selectedIndexes = listOfCountries
                            random.shuffle(selectedIndexes)
                            selectedIndexes = selectedIndexes[:recordsNum]
                            isNumOfCountriesSet = True
                        else:
                            print("Invalid input")
                else:
                    print("There is no such option you know")
            else:
                print("There is no such option you know")
        #opcja aby użytkownik wpisał se indexy ręcznie
        elif indexDataChoice == 2:
            indexDataInputChoice = ""
            print('When you are done entering data write "Done"')
            while indexDataInputChoice != "Done":
                indexDataInputChoice = input('Enter your custom index or enter "Done": ')
                if(indexDataInputChoice != "Done"):
                    selectedIndexes.append(indexDataInputChoice)
            recordsNum = len(selectedIndexes)
        else:
            print("There is no such option you know")
    else:
        print("There is no such option you know")

    print(title, "\n")
    
    data = []
    for y in range(0, recordsNum):
        print(selectedIndexes[y])  
        newDataRecord = random.random() + 1
        data.append(newDataRecord)      
    print(selectedIndexes)
    print(data)
    
    
    df = pd.DataFrame({title: data})
    plot = df.plot.pie(y=title, figsize=(11, 11), labels=selectedIndexes, fontsize=12, legend=False, autopct='%1.1f%%')
    fig = plot.get_figure()
    fig.savefig("myplot.png")

    im = Image.open(r"myplot.png") 
    im.show()

#funkcja do generowania losowych wykresów słupkowych
def randomBarChart(title):
    selectedIndexes = []

    indexDataChoice = input("If you want to randomly select countries to be indexes - press 1 and enter, if you want manually enter indexes press 2 and enter: ")
    if str.isdigit(indexDataChoice):
        indexDataChoice = int(indexDataChoice)
        if indexDataChoice == 1:
            randomisedCountryNumberChoice = input("If you want to number of countries to be randomised enter 1, if you want the specify how many countries you want to have in the graph - enter 2: ")
            if str.isdigit(randomisedCountryNumberChoice):
                randomisedCountryNumberChoice = int(randomisedCountryNumberChoice)
                if randomisedCountryNumberChoice == 1:
                    print("przypisanie")
                    recordsNum = random.randint(1, len(listOfCountries))
                    selectedIndexes = listOfCountries
                    random.shuffle(selectedIndexes)
                    selectedIndexes = selectedIndexes[:recordsNum]
                elif randomisedCountryNumberChoice == 2:
                    isNumOfCountriesSet = False
                    while isNumOfCountriesSet == False:
                        recordsNumInput = input("Enter number of countries you want to chose: ")
                        if str.isdigit(recordsNumInput):
                            recordsNum = int(recordsNumInput)
                            selectedIndexes = listOfCountries
                            random.shuffle(selectedIndexes)
                            selectedIndexes = selectedIndexes[:recordsNum]
                            isNumOfCountriesSet = True
                        else:
                            print("Invalid input")
                else:
                    print("There is no such option you know")
            else:
                print("There is no such option you know")
        elif indexDataChoice == 2:
            indexDataInputChoice = ""
            print('When you are done entering data write "Done"')
            while indexDataInputChoice != "Done":
                indexDataInputChoice = input('Enter your custom index or enter "Done": ')
                if(indexDataInputChoice != "Done"):
                    selectedIndexes.append(indexDataInputChoice)
            recordsNum = len(selectedIndexes)
        else:
            print("There is no such option you know")
    else:
        print("There is no such option you know")

    print(title, "\n")
    print("Please now specife minimum and maximum value for data: ")

    inputMin = input("Specify the minimum value: ")
    while isfloat(inputMin) == False:
        inputMin = input("This is incorrect format of number. Specify the maximum value once again: ")
    minBarPlotValue = float(inputMin)

    inputMax = input("Specify the maximum value: ")
    while isfloat(inputMax) == False:
        inputMax = input("This is incorrect format of number. Specify the maximum value once again: ")
    maxBarPlotValue = float(inputMax)

    if(minBarPlotValue > maxBarPlotValue):
        temp = minBarPlotValue
        minBarPlotValue = maxBarPlotValue
        maxBarPlotValue = temp

    data = []
    for y in range(0, recordsNum):
        print(selectedIndexes[y])  
        newDataRecord = random.uniform(minBarPlotValue, maxBarPlotValue)
        data.append(newDataRecord)      
    print(selectedIndexes)
    print(data)
    
    #color selection
    colorsToUse = []
    for y in range(0, recordsNum):
        colorsToUse.append(listOfColors[y])
    random.shuffle(colorsToUse)

    sizeDiffrence = len(colorsToUse) - len(selectedIndexes)
    if(sizeDiffrence < 0):
        colorsToUse.append(colorsToUse[0:(sizeDiffrence + 1)])
    elif(sizeDiffrence > 0):
        colorsToUse = colorsToUse[0:(len(colorsToUse - sizeDiffrence + 1))]
    random.shuffle(colorsToUse)
    print(colorsToUse)


    df = pd.DataFrame({title: data}, index=selectedIndexes, color = colorsToUse)
    fig = df.plot.bar(rot=0)
    fig.figure.savefig("myplot.png")

    im = Image.open(r"myplot.png") 
    im.show()

def __main__():
    while True:
        print("""
        RandomChartGenerator
        Menu
        0 - Exit Program
        1 - Generate random pie chart
        #in production
        2 - Generate random bar chart (with one bar per index)
        #to be done
        3 - Generate random bar chart (with more than one bar per index)
        4 - generate random scatter plot
        2137 - Generate random COVID stats 
        2138 - Generate random voting poll
        """)
        menuChoice = input("Select positon from menu: ")
        if str.isdigit(menuChoice):
            menuChoice = int(menuChoice)
            if menuChoice == 0:
                break
            elif (menuChoice >= 1 and menuChoice <= 2 or menuChoice == 2137):
                title = input("Add some title to your chart: ")
                if menuChoice == 1:
                    randomPieChart(title)
                elif menuChoice == 2:
                    randomBarChart(title)
                if menuChoice == 2137:
                    print("I am sorry, I didn't add this option yet, please be patient")
                    #plan na ten: bierzemy datę, generujemy liczbę, w dni tygodnia do soboty włącznie zwiększa się statystyka, niedzielę i poniedziałek - zmniejsza
                    #jeszcze można dodać generowanie na podstawie liczby wpisanej przez użytkownika jako dzisiejsza
            else:
                print("There is no such option you know")
        else:
                print("There is no such option you know")

__main__()