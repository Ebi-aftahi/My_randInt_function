import random
def randInt(min = 0  , max = 100):
    if(max < 0):
        print("Error: maximum must be a positive number")
        return -1
    elif(min < 0):
        min = 0
    elif(min > max):
        print("Error: maximum smaller than minimum")
        return -1
       
    num = random.random() * (max- min) + min
    return round(num)

print(randInt()) 		    # should print a random integer between 0 to 100
print(randInt(max=50)) 	            # should print a random integer between 0 to 50
print(randInt(min=50)) 	            # should print a random integer between 50 to 100
print(randInt(min=50, max=500))     # should print a random integer between 50 and 500
print(randInt(min=-1))
print(randInt(max=-5))
print(randInt(min = 50, max=5 ))
