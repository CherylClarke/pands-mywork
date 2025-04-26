# messing with functions

# to demonstrate the defining and using of functions

x, y, z = (1, 2,3)
print (x, y,z)
print (f"{x}-{y} {z}")


def cube(number):
    print(number)
    return (number ** 3)


#ans = cube(23)
#print(f"we got {ans}")
num = 45


print(f"and {num} is {cube(num)}")
