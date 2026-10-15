nested_list=[[1,2,3], [4,5,6], [7,8,9]]
total=0
for row in nested_list:
    for element in row:
        total = total + element
print("Nested List:",nested_list)
print("Sum of all elements:",total)        