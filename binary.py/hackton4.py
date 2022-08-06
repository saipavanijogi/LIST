# there are n bikes and m cares on the road
# each bike has 2 tyres
# each car has 2 tyres
# find the totoa number of tyres on the road
cars=int(input("enter the number"))
bike=int(input("enter the number"))
i=0
while i<cars:
    if bike>i:
        total_cars=cars*4
        total_bike=bike*2
    i=i+1
print(total_cars)
print(total_bike)
    