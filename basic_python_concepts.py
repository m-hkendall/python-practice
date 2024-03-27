#Basin Python programming concepts: following Python for Geographic Data Analysis book: https://pythongis.org/index.html

#Python data types: int, float, str, bool, list

#List: store many related values together with a single variable; are mutable; store multiple data types in one list (not best practice)
station_names = [
    'Helsinki Harmaja',
    'Helsinki Kaisaniemi',
    'Helsinki Kaivopuisto',
    'Helsinki Kumpula'
]

print(station_names[0]) #Access list values using indices
print(len(station_names)) #Find the number of items in a list
print(station_names[-1]) #Access last item in a list

#del station_names[0] #Delete list value
station_names.append("Helsinki Malmi Airfield") #Add list value

print(station_names.count("Helsinki Kumpula")) #Count the number of times "Helsinki Kumpula" occurs in the list
print(station_names.index("Helsinki Kumpula")) #Find the index of "Helsinki Kumpula"

#station_names.reverse() #Reversing a list
#station_names.sort() #Sorting a list alphabetically - Python places capital letters below lowercase letters

#F-string formatting
station_name = 'Helsinki Kaivopuisto'
station_id = 132310
temp = 18.3892890 #float with many decimals
info_text = f"The temperature at {station_name} station (ID: {station_id}) is {temp:.2f} Celsius."
print(info_text)

#String manipulation
#Splitting strings
text = "Stations: Helsinki Kumpula, Helsinki Kaisaniemi, Helsinki Harmaja"
splitted = text.split(":") #This splits a string into difference components based on specific characters 
print(splitted)
print(splitted[0]) #We can now access different parts of the list
#Slicing text
stations_text = splitted[1]
stations_text = stations_text[1:] #Keep all the rest of the characters in our text without the preceeding space
print(stations_text)
#Remove words repeated multiple times
stations_without_helsinki = stations_text.replace("Helsinki ", "")
print(stations_without_helsinki)
stations_without_helsinki = stations_without_helsinki.upper()
print(stations_without_helsinki)

#for loops--------------------------------------------------------------
#for variable in collection:
#    do things with variable
#where, variable: can be any name you like

european_cities = [
    'Amsterdam',
    'Brussels',
    'Lisbon',
    'Reykjavik'
]
for city in european_cities:
    print(city)

#Loop that performs a calculation a specified number of times, use the range() function
for value in range(5): #range() gives a list of 5 numbers [0,1,2,3,4] that gets printed to the screen
    print(value)

numbers = [5,6,7,8]
for i in range(len(numbers)):
    print("Value of i: ", i)
    print("Value of numbers[i] before addition: ", numbers[i])
    numbers[i] = numbers[i] + i
    print("Value of numbers[i] after addition: ", numbers[i])
    print("")

european_countries = [
    'Netherlands',
    'Belgium',
    'Portugal',
    'Iceland'
]
for i in range(len(european_cities)):
    print(european_cities[i], "is the capital of", european_countries[i]) #The index i is used to access each item in the two lists of cities and countries and allows them to be put into city/country pairs.

temperatures = [0,12,17,28,30]
for temperature in temperatures:
    if temperature > 25:
        print(temperature, "is hot")
    else:
        print(temperature, 'is not hot')

#Functions--------------------------------------------------------------------
def celsius_to_fahr(temp):
    return 9/5 * temp + 32

freezing_point = celsius_to_fahr(0)
print('The freezing point of water in Fahrenheit is: ', freezing_point)
#You can also explicitly state which variable values is being used, i.e.,:
boiling_point = celsius_to_fahr(temp=100)
print('The boiling point of water in Fahrenheit is: ', boiling_point)

def kelvins_to_celsius(temp_kelvins):
    return temp_kelvins - 273.15

def kelvins_to_fahr(temp_kelvins):
    """"This is a docstring. It documents what a function does. This function converts temperatures in Kelvins to Fahrenheit"""
    temp_celsius = kelvins_to_celsius(temp_kelvins)
    temp_fahr = celsius_to_fahr(temp_celsius)
    return temp_fahr

absolute_zero_fahr = kelvins_to_fahr(temp_kelvins=0)
print("Absolute zero in Fahrenheit is: ", absolute_zero_fahr)

#Temperature calculator------------------------------------------------------------
def temp_calculator(temp_k, convert_to):
    """
    Function for converting temperature in Kelvins to Celsius or Fahrenheit.
    Parameters
    ----------
    temp_k: <numerical>
        Temperature in Kelvins
    convert_to: <str>
        Target temperature that can be either Celsius ('C') or Fahrenheit ('F'). Supported values: 'C' or 'F'.
    Returns
    -------
    <float>
        Converted temperature.
    """
    #Check if user wants the temperature in Celsius or Fahrenheit
    if convert_to == 'C':
        #Convert the value to Celsius using the kelvins_to_celsius function
        converted_temp = kelvins_to_celsius(temp_kelvins=temp_k)
    elif convert_to == 'F':
        #Convert the value to Fahrenheit using the kelvins_to_fahr function
        cels = kelvins_to_celsius(temp_kelvins=temp_k)
        converted_temp = celsius_to_fahr(temp=cels)
    return converted_temp

temp_kelvin = 30
temperature_celsius = temp_calculator(temp_k=temp_kelvin, convert_to='C')
print("The temperature", temp_kelvin, "Kelvin is", temperature_celsius, "degrees Celsius.")

#Exercise 2.2 - Creating and changing lists----------------------------------------------------
station_name = [
    'lighthouse',
    'Harmaja',
    'Suomenlinna aaltopoiju',
    'Kumpula',
    'Kaisaniemi'
]
y_operation = [
    2003,
    1989,
    2016,
    2005,
    1844
]
station_name.append('Malmi airfield')
station_name.append('Vuosaari harbour')
station_name.append('Kaivopuisto')
print(station_name)
y_operation.append(1937)
y_operation.append(2012)
y_operation.append(1904)
print(y_operation)
station_name.sort()
print(station_name)
y_operation.sort()
print(y_operation)

#Exercise 2.3 - Lists and index values---------------------------------------------------
months = [
    'Jan',
    'Feb',
    'Mar',
    'Apr',
    'May',
    'Jun',
    'Jul',
    'Aug',
    'Sep',
    'Oct',
    'Nov',
    'Dec'
]
temp_cels = [-3.5,-4.5,-1.0,4.0,10.0,15.0,18.0,16.0,11.5,6.0,2.0,-1.5]
for i in range(len(months)):
    print('The average temperature in Helsinki in', months[i], 'is', temp_cels[i])

#Exercise 2.4 - Batch processing files with a for loop----------------------------------
basename = 'Station'
station_files = []
for i in range(21):
    station = basename + "_" + str(i) + ".txt"
    station_files.append(station)

#Exercise 2.5 - Classifying temperatures---------------------------------------------------
cold = []
slippery = []
comfortable = []
warm = []
temperatures = [-5.4, 1.0, -1.3, -4.8, 3.9, 0.1, -4.4, 4.0, -2.2, -3.9, 4.4,
                -2.5, -4.6, 5.1, 2.1, -2.4, 1.9, -3.3, -4.8, 1.0, -0.8, -2.8,
                -0.1, -4.7, -5.6, 2.6, -2.7, -4.6, 3.4, -0.4, -0.9, 3.1, 2.4,
                1.6, 4.2, 3.5, 2.6, 3.1, 2.2, 1.8, 3.3, 1.6, 1.5, 4.7, 4.0,
                3.6, 4.9, 4.8, 5.3, 5.6, 4.1, 3.7, 7.6, 6.9, 5.1, 6.4, 3.8,
                4.0, 8.6, 4.1, 1.4, 8.9, 3.0, 1.6, 8.5, 4.7, 6.6, 8.1, 4.5,
                4.8, 11.3, 4.7, 5.2, 11.5, 6.2, 2.9, 4.3, 2.8, 2.8, 6.3, 2.6,
                -0.0, 7.3, 3.4, 4.7, 9.3, 6.4, 5.4, 7.6, 5.2]
for temp in temperatures:
    if temp < -2:
        cold.append(temp)
    elif temp >= -2 and temp <= 2:
        slippery.append(temp)
    elif temp >= 2 and temp <= 15:
        comfortable.append(temp)
    elif temp >= 15:
        warm.append(temp)
print(cold)
print(slippery)
print(comfortable)
print(warm)
#How many times was it cold in Helsinki?
print('Helsinki was cold ', len(cold), 'times.')
#How many times was it comfortable?
print('Helsinki was comfortable ', len(comfortable), 'times.')
#Was it every warm?
print('Helsinki was warm ', len(warm), 'days.')

#Exercise 2.6 A temperature conversion function--------------------------------------------
temps_to_convert = [32,68,91,-17]
def temp_conversion(fahrenheit_temp):
    celsius_temp = (fahrenheit_temp-32)*(5/9)
    return celsius_temp
for temp in temps_to_convert:
    celsius_temperature = temp_conversion(fahrenheit_temp=temp)
    print(celsius_temperature)

#Exercise 2.7 A temperature classifier function-----------------------------------------
temps_to_classify = [17,2,1.9,-2]
def temp_classifier(temp):
    if temp < -2:
        temp_classification = 0
    elif temp >= -2 and temp <= 2:
        temp_classification = 1
    elif temp >= 2 and temp <= 15:
        temp_classification = 2
    elif temp >= 15:
        temp_classification = 3
    return temp_classification
for temps in temps_to_classify:
    classification = temp_classifier(temp=temps)
    print(classification)