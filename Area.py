


def Area():
    area = 0
    a, b, h = map(int, input("Enter 3 separated numbers: ").split())
    area = ((a + b) * h) / 2
    return area


# Assign to a varable the function
result = Area()

# Then you can print out the results
print (result)

if result > 100:
    print("the result is big", result)


result2 = Area()
cost = result2 * 2
print("Cost to cover the area is:", cost)



result3 = Area()
a1 = Area()
a2 = Area()
a3 = Area()

total = a1 + a2 + a3
print("Total of all areas is:", total)










