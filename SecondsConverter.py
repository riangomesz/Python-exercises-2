# Program that receives a number of days, hours and minutes
# and converts the entered values ​​to seconds

days = int(input("Days: "))
hours = int(input("Hours: "))
minutes = int(input("Minutess: "))
total = days * 24 * 3600 + hours * 3600 + minutes * 60

print("Converted to seconds is equal to %10d seconds." %total)
