#importing functions from a different file 
from function import square,cube
for i in range(11):
    print(f"The square of {i} is {square(i)}")
    print(f"The cube of {i} is {cube(i)}")