#count control loop
count = 0
while (count < 10):
    print("count is ", count)
    count = count + 1


print ("at the end count is ", count) 

count = 10
while count >=0:
    print ("countdown ", count)
    count -= 1
    
print("blast off")

#sentinel control loop

val = input("type something (q to quit):")
while val != "q":
    print ("Hi mom")
    val = input("q to quit")
print ("all done")