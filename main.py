def randomPieChart(title):
    print("wow")

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

