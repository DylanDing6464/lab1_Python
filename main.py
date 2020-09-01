# Author: Dylan Ding dvd5567@psu.com
# Collaborator: William O'Rourke wjo5083@psu.edu
# Collaborator: Alexis Vajda acc5358@psu.edu
# Collaborator: Ashley Jones anj5278@psu.com

temperature = input('Enter temperature: ')
unit = input('Enter unit in F/f or C/c: ')

temperature = float(temperature)


if(unit == "c" or unit == "C"): 
	fahrenheitDegree = (9/5)*temperature+32	
	print (f"{temperature}° in Celsius is equivalent to {fahrenheitDegree}° Fahrenheit.")
	
elif(unit == "f" or unit == "F"):
	celsiusDegree = (temperature-32)*5/9 
	print (f"{temperature}° in Fahrenheit is equivalent to {celsiusDegree}° Celsius.")

else:
	print (f"Invalid unit({unit}).")

