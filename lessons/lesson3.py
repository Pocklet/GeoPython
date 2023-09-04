european_cities = ["Amsterdam", "Brussels", "Lisbon", "Reykjavik",]

for city in european_cities:
    print(city)



us_cities = ["Detroit", "Chicago", "Denver", "Boston", 
             "Portland", "San Francisco", "Houston", "Orlando",]

for city in us_cities:
    print(city)


# for loops in Python have the general form below.

# for variable in collection:
#     do things with variable

for value in range(5):
    print(value)

for i in range(2, 9, 3):
    print(i)


numbers = [5, 6, 7, 8]

for i in range(len(numbers)):
    print(f"Value of i: {i}")
    print(f"Value of numbers[i] before addition: {numbers[i]}")
    numbers[i] = numbers[i] + i
    print(f"Value of numbers[i] after  addition: {numbers[i]}")
    print("")

print(numbers)


cities = ["Helsinki", "Stockholm", "Oslo", "Reykjavik", "Copenhagen"]
countries = ["Finland", "Sweden", "Norway", "Iceland", "Denmark"]

for i in range(len(cities)):
    print(f"{cities[i]} is the capital of {countries[i]}")


odd_numbers = [1, 3, 5, 7, 9]
even_numbers = [10, 4, 6, 8, 2]
for i in range(len(odd_numbers)):
    print(odd_numbers[i] + even_numbers[i])


temperature = 17

if temperature > 25:
    print(f"{temperature} is hot!")
else:
    print(f"{temperature} is not hot!")


print(temperature > 25)


temperatures = [0, 28, 12, 17, 30]

for temperature in temperatures:
    if temperature > 25:
        print(f"{temperature} is hot")
    else:
        print(f"{temperature} is not hot")
