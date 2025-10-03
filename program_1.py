def milesConverter(kilometers):
    miles = kilometers * 0.621371
    return miles
kilometers = float(input("Enter distance in kilometers: "))
print("Distance in miles is", milesConverter(kilometers))