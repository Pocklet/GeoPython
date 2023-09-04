basename = "Station"
print(basename)

filenames = []
print(filenames)


for i in range(20):
    number = i + 1
    convertedNum = str(number)
    station = basename + "_" + convertedNum + ".txt"
    filenames.append(station)

print(filenames)



temperatures = [-5.4, 1.0, -1.3, -4.8, 3.9, 0.1, -4.4, 4.0, -2.2, -3.9, 4.4,
                -2.5, -4.6, 5.1, 2.1, -2.4, 1.9, -3.3, -4.8, 1.0, -0.8, -2.8,
                -0.1, -4.7, -5.6, 2.6, -2.7, -4.6, 3.4, -0.4, -0.9, 3.1, 2.4,
                1.6, 4.2, 3.5, 2.6, 3.1, 2.2, 1.8, 3.3, 1.6, 1.5, 4.7, 4.0,
                3.6, 4.9, 4.8, 5.3, 5.6, 4.1, 3.7, 7.6, 6.9, 5.1, 6.4, 3.8,
                4.0, 8.6, 4.1, 1.4, 8.9, 3.0, 1.6, 8.5, 4.7, 6.6, 8.1, 4.5,
                4.8, 11.3, 4.7, 5.2, 11.5, 6.2, 2.9, 4.3, 2.8, 2.8, 6.3, 2.6,
                -0.0, 7.3, 3.4, 4.7, 9.3, 6.4, 5.4, 7.6, 5.2]

cold = []
slippery = []
comfortable = []
warm = []


for i in range(len(temperatures)):
    
    if temperatures[i] < -2:
        cold.append(temperatures[i])
    
    elif temperatures[i] >= -2 and temperatures[i] < 2:
        slippery.append(temperatures[i])
    
    elif temperatures[i] >= 2 and temperatures[i] < 15:
        comfortable.append(temperatures[i])
    
    else:
        warm.append(temperatures[i])



cold_times = str(len(cold))
print("It was cold " + cold_times + " times.")

slippery_times = str(len(slippery))
print("It was slippery " + slippery_times + " times.")

comfortable_times = str(len(comfortable))
print("It was comfortable " + comfortable_times + " times.")



north_west = []
north_east = []
south_west = []
south_east = [] 

# Station names
stations = ['Hanko Russarö', 'Heinola Asemantaus', 'Helsinki Kaisaniemi', 
            'Helsinki Malmi airfield', 'Hyvinkää Hyvinkäänkylä', 'Joutsa Savenaho', 
            'Juuka Niemelä', 'Jyväskylä airport', 'Kaarina Yltöinen', 'Kauhava airfield', 
            'Kemi Kemi-Tornio airport', 'Kotka Rankki', 'Kouvola Anjala', 
            'Kouvola Utti airport', 'Kuopio Maaninka', 'Kuusamo airport', 
            'Lieksa Lampela', 'Mustasaari Valassaaret', 'Parainen Utö', 'Pori airport', 
            'Rovaniemi Apukka', 'Salo Kärkkä', 'Savonlinna Punkaharju Laukansaari', 
            'Seinäjoki Pelmaa', 'Siikajoki Ruukki', 'Siilinjärvi Kuopio airport', 
            'Tohmajärvi Kemie', 'Utsjoki Nuorgam', 'Vaala Pelso', 'Vaasa airport', 
            'Vesanto Sonkari', 'Vieremä Kaarakkala', 'Vihti Maasoja', 'Ylitornio Meltosjärvi']

# Latitude coordinates of Weather stations  
lats = [59.77, 61.2, 60.18, 60.25, 60.6, 61.88, 63.23, 62.4,
       60.39, 63.12, 65.78, 60.38, 60.7, 60.9, 63.14, 65.99,
       63.32, 63.44, 59.78, 61.47, 66.58, 60.37, 61.8, 62.94,
       64.68, 63.01, 62.24, 70.08, 64.501, 63.06, 62.92, 63.84,
       60.42, 66.53]

# Longitude coordinates of Weather stations 
lons = [22.95, 26.05, 24.94, 25.05, 24.8, 26.09, 29.23, 25.67, 
       22.55, 23.04, 24.58, 26.96, 26.81, 26.95, 27.31, 29.23, 
       30.05, 21.07, 21.37, 21.79, 26.01, 23.11, 29.32, 22.49, 
       25.09, 27.8, 30.35, 27.9, 26.42, 21.75, 26.42, 27.22, 
       24.4, 24.65]

# Cutoff values that correspond to the centroid of Finnish mainland
# North - South
north_south_cutoff = 64.5

# East-West
east_west_cutoff = 26.3


for n in range(len(stations)):
    if lats[n] >= north_south_cutoff:
        North = True
    else:
        North = False
    
    if lons[n] <= east_west_cutoff:
        West = True
    else:
        West = False
    
    if North == True and West == True:
        north_west.append(stations[n])

    if North == False and West == True:
        south_west.append(stations[n])

    if North == True and West == False:
        north_east.append(stations[n])

    if North == False and West == False:
        south_east.append(stations[n])


print(f"The names of the Northwest stations are:\n{north_west}")
print(f"The names of the Northeast stations are:\n{north_east}")
print(f"The names of the Southwest stations are:\n{south_west}")
print(f"The names of the Southeast stations are:\n{south_east}")

north_west_share = len(north_west) / len(stations) * 100
north_east_share = len(north_east) / len(stations) * 100
south_west_share = len(south_west) / len(stations) * 100
south_east_share = len(south_east) / len(stations) * 100

# Note we are using f-strings here
# .0f rounds the decimal values to whole numbers
print(f"Northwest contains {north_west_share:.0f}% of all stations.")
print(f"Northeast contains {north_east_share:.0f}% of all stations.")
print(f"Southwest contains {south_west_share:.0f}% of all stations.")
print(f"Southeast contains {south_east_share:.0f}% of all stations.")
