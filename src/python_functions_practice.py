def return_10():
    ten = 5 + 5 
    return ten

def add(number_1, number_2):
    total = number_1 + number_2
    return total

def subtract(number_10, number_5):
    total = number_10 - number_5
    return total

def multiply(number_4, number_2):
    total = number_4 * number_2
    return total

def divide(number_10, number_2):
    total = number_10/number_2 
    return total
    
def length_of_string(string):
    # length = "A string of length 21"
    x = len(string)
    return x

def join_string (string_1, string_2):
    
    string_joined = string_1 + string_2
    return string_joined

def add_string_as_number(string_1, string_2):
    total = int(string_1) + int(string_2)
    return total
    
def number_to_full_month_name(month_number):
    months_of_year = {
    1:"January",
    2:"February",
    3 : "March",
    4 : "April",
    5 : "May",
    6 : "June",
    7 : "July",
    8 : "August", 
    9 : "September",
    10: "October",
    11: "November",
    12 :"Decemeber"
    }
    return months_of_year[month_number]

def number_to_short_month_name(month_number):
    return number_to_full_month_name(month_number)[0:3]
    # second option
    # short_month_name = number_to_short_month_name(month_number)
    # return = short_month_name[0:3]

#Given the length of a side of a cube calculate the volume
def test_volume_of_cube(side_length):
    return side_length * side_length * side_length

#Given a String, return the String reversed
def test_reverse_string(string):
    return string[::-1]

#Given a value in farenheit, convert this into celsius.
 
def test_fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (0.5556)
    return celsius
   
    




