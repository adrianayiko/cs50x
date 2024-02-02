# declaring , intializing and assigning variables
y = 1 
b = 2 
c=3 
print(f"The variables we have are {y}, {b},and {c} for reference")

#trying out the if conditions 

number = int(input("Enter a number: "))

if(number > 0):
    print(f"The number {number} is a positive number.")
elif(number == 0):
    print(f"{number} is neither positive nor negative.")
else:
    print(f"The number {number} is a negative number.")
    
#Data structures 

#lists 
names = ["mark", "sam" , "paulo"]
names.append["Ben"]
print(names)
print(names[-1])

#Tuples 
coordinates = (0.2,0.4)
print(coordinates)

more_fruits = ("pawpaw" , "pineapple")
fruits =  ("banana" , "orange")
print(fruits)
fruits.add("apple")
fruits.update(more_fruits)
print(fruits)