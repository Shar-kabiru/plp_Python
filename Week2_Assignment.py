#Question 1: Create an empty list called my_list.
my_List = []
print(my_List)
#Question 2: Append the following elements to my_list: 10, 20, 30, 40.
my_List.append(10)
my_List.append(20)
my_List.append(30)
my_List.append(40)
print(my_List)

#Question 3: Insert the value 15 at the second position in the list.
my_List[1] = 15
print(my_List)

#Question 4: Extend my_list with another list: [50, 60, 70].
another_list = [50,60,70]
my_List.extend(another_list)
print(my_List)

#Question 5: Remove the last element from my_list.
del my_List[-1]
print(my_List)
#Question 6: Sort my_list in ascending order.
my_List.sort()
print(my_List)

#Question 7: Find and print the index of the value 30 in my_list.
index = my_List.index(30)

print("Index of 30:", index)