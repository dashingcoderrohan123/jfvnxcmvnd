#Define a function to find a cube and define another function which let execute the cube function if the number is divisible by 3
def cube(number):
    return number*number*number

def execution_cube(number):
    if number%3==0:
        return cube(number)
    
    else:
        return False
print(execution_cube(6))
print(execution_cube(7))