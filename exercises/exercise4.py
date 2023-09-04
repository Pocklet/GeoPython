def fahr_to_celsius(temp_fahrenheit):
    return (temp_fahrenheit - 32) * 5 / 9

# print(fahr_to_celsius(32))



def temp_classifier(temp_celsius):
    if temp_celsius < -2:
        return 0
    elif temp_celsius >= -2 and temp_celsius < 2:
        return 1
    
    elif temp_celsius >= 2 and temp_celsius < 15:
        return 2
    
    else:
        return 3
    

# print(temp_classifier(16))
# print(temp_classifier(2))
# print(temp_classifier(-1))



# List of half-hourly temperature values (in degrees Fahrenheit) for one week
temp_data =  [19, 21, 21, 21, 23, 23, 23, 21, 19, 21, 19, 21, 23, 27, 27, 28, 30, 30, 32, 32, 32, 32, 
              34, 34, 34, 36, 36, 36, 36, 36, 36, 34, 34, 34, 34, 34, 34, 32, 30, 30, 30, 28, 28, 27,
              27, 27, 23, 23, 21, 21, 21, 19, 19, 19, 18, 18, 21, 27, 28, 30, 32, 34, 36, 37, 37, 37, 
              39, 39, 39, 39, 39, 39, 41, 41, 41, 41, 41, 39, 39, 37, 37, 36, 36, 34, 34, 32, 30, 30,
              28, 27, 27, 25, 23, 23, 21, 21, 19, 19, 19, 18, 18, 18, 21, 25, 27, 28, 34, 34, 41, 37, 
              37, 39, 39, 39, 39, 41, 41, 39, 39, 39, 39, 39, 41, 39, 39, 39, 37, 36, 34, 32, 28, 28,
              27, 25, 25, 25, 23, 23, 23, 23, 21, 21, 21, 21, 19, 21, 19, 21, 21, 19, 21, 27, 28, 32,
              36, 36, 37, 39, 39, 39, 39, 39, 41, 41, 41, 41, 41, 41, 41, 41, 41, 39, 37, 36, 36, 34,
              32, 30, 28, 28, 27, 27, 25, 25, 23, 23, 23, 21, 21, 21, 19, 19, 19, 19, 19, 19, 21, 23,
              23, 23, 25, 27, 30, 36, 37, 37, 39, 39, 41, 41, 41, 39, 39, 41, 43, 43, 43, 43, 43, 43,
              43, 43, 43, 39, 37, 37, 37, 36, 36, 36, 36, 34, 32, 32, 32, 32, 30, 30, 28, 28, 28, 27,
              27, 27, 27, 25, 27, 27, 27, 28, 28, 28, 30, 32, 32, 32, 34, 34, 36, 36, 36, 37, 37, 37,
              37, 37, 37, 37, 37, 37, 36, 34, 30, 30, 27, 27, 25, 25, 23, 21, 21, 21, 21, 19, 19, 19,
              19, 19, 18, 18, 18, 18, 18, 19, 23, 27, 30, 32, 32, 32, 32, 32, 32, 34, 34, 34, 34, 34,
              36, 36, 36, 36, 36, 32, 32, 32, 32, 32, 32, 32, 32, 30, 30, 30, 30, 30, 30, 30, 30, 30,
              30, 30, 30, 30, 28, 28]

temp_classes = []


for i in range(len(temp_data)):
    temp_celsius = fahr_to_celsius(temp_data[i])
    temp_class = temp_classifier(temp_celsius)
    temp_classes.append(temp_class)

zeros = temp_classes.count(0)
ones = temp_classes.count(1)
twos = temp_classes.count(2)
threes = temp_classes.count(3)
print(len(temp_classes))