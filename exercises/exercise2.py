##station_names = ["lighthouse",
##                 "Harmaja",
##                 "Suomenlinna aaltopoiju",
##                 "Kumpula",
##                 "Kaisaniemi"]
##station_start_years = ["2003",
##                       "1989",
##                       "2016",
##                       "2005",
##                       "1844"]
##
##
##print(len(station_names))
##print(len(station_start_years))
##
##
##station_names.append("Malmi airfield")
##station_names.append("Vuosaari harbour")
##station_names.append("Kaivopuisto")
##
##station_start_years.append("1937")
##station_start_years.append("2012")
##station_start_years.append("1904")
##
##print(len(station_names))
##print(len(station_start_years))
##
##print(station_names[-1])
##print(station_start_years[-1])
##
##
##station_names.sort()
##station_start_years.sort()
##
##print(station_names[0])
##print(station_start_years[0])


##months = ["January", "Febuary", "March",
##          "April", "May", "June", "July",
##          "August", "September", "October",
##          "November", "December",]
average_temp = ["-3.5", "-4.5", "-1.0",
                "4.0", "10.0", "15.0",
                "18.0", "16.0", "11.5",
                "6.0", "2.0", "-1.5",]

def selectFromDict(months, name):

    index = 0
    indexValidList = []
    print("Select a " + name + ":")
    for monthName in months:
        index = index + 1
        indexValidList.extend([months[monthName]])
        print(str(index) + ")" + monthName)
    inputValid = False
    while not inputValid:
        inputRaw = input(name + ": ")
        inputNo = int(inputRaw) - 1
        if inputNo > -1 and inputNo < len(indexValidList):
            selected = indexValidList[inputNo]
            print("Selected " + name + ": " + selected)
            print("Average temperature in " + selected + " is: " + average_temp[inputNo])
            inputValid = True
            break
        else:
            print("Please select a valid " + name + " number")

    return selected

months = {}
months['January'] = 'Jan'
months['February'] = 'Feb'
months['March'] = 'Mar'
months['April'] = 'Apr'
months['May'] = 'May'
months['June'] = 'Jun'
months['July'] = 'Jul'
months['August'] = 'Aug'
months['September'] = 'Sep'
months['October'] = 'Oct'
months['November'] = 'Nov'
months['December'] = 'Dec'

# Let user select a month
month = selectFromDict(months, 'Month')

            

