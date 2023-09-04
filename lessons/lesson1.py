##import math
##
##print(1 + 1)
##print(5 * 7)
##
##print(math.sin(3))
##print(math.sqrt(4))
##print(math.pi)
##
##print("The square root of 4 is", math.sqrt(4))
##
##
##temp_celsius = 10.0
##print(temp_celsius)
##
##print("Temperature in Fahrenheit:", 9 / 5 * temp_celsius + 32)
##
##temp_celsius = 15.0
##print("Temperature in Celsius is now:", temp_celsius)
##temp_fahrenheit = 9 / 5 * temp_celsius + 32
##
##print("Temperature in Celsius:", temp_celsius, "and in Fahrenheit:", temp_fahrenheit)
##
##
##weatherForecast = "Hot"
##type(weatherForecast)
##
##place = input("Where are you from? ")
##print(place, "is a nice place!")



ice_cream_rating = 6
sleeping_rating = 10
maximum_rating = 10

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
my_name = first_name + " " + last_name
print("Hello", my_name)

happiness_rating = (ice_cream_rating + sleeping_rating) / 2

print("My name is", first_name, "and I rate eating ice cream", ice_cream_rating, "out of", maximum_rating)
print("I am", my_name, "and my sleeping enjoyment is", sleeping_rating, "/", maximum_rating)
print("My name is", my_name, "and based on the factors above my happiness rating is a", happiness_rating, "out of 10, or", (8 / 10)*100, "%")
