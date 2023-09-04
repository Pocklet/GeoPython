station_names = [
    "Helsinki Harmaja",
    "Helsinki Kaisaniemi",
    "Helsinki Kaivopuisto",
    "Helsinki Kumpula",]
##
##print(station_names)
##type(station_names)
##
##print(station_names[0])
##len(station_names)
##
##print(station_names[-1]) #shows last item in list



##station_types = [
##    "Weather stations",
##    "Weather stations",
##    "Weather stations",
##    "Weather stations",]
##
##print(station_types)
##
##station_types[2] = "Mareographs"
##print(station_types)


station_name = "Helsinki Kaivopuisto"
station_id = 132310
station_lat = 60.15
station_lon = 24.96
station_type = "Mareographs"

station_hel_kaivo = [station_name, station_id, station_lat, station_lon, station_type]
print(station_hel_kaivo)

del station_names[0]
print(station_names)

station_names.append("Helsinki lighthouse")
station_names.append("Helsinki Malmi airfield")
print(station_names)

station_name_length = len(station_names)
print(station_name_length)

# The count method counts the number of occurences of a value
station_names.count("Helsinki Kumpula")

# The index method gives the index value of an item in a list
station_names.index("Helsinki Kumpula")


station_names.reverse()
print(station_names)

station_names.sort()
print(station_names)



station_id_str = str(station_id)

station_name_and_id = station_name + ": " + str(station_id)
print(station_name_and_id)


