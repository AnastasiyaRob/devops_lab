# Consider a list (list = []). You can perform the following commands:
# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of followed by lines of commands.
# Iterate through each command in order and perform the corresponding operation on your list.
# The first line contains an integer, , denoting the number of commands.
# Each line  of the  subsequent lines contains one of the commands described above
a = int(input())
myList = []
for i in range(a):
    b = input().split()
    if b[0] == "insert":
        myList.insert(int(b[1]), int(b[2]))
    if b[0] == "remove":
        myList.remove(int(b[1]))
    if b[0] == "print":
        print(myList)
    if b[0] == "append":
        myList.append(int(b[1]))
    if b[0] == "sort":
        myList.sort()
    if b[0] == "reverse":
        myList.reverse()
    if b[0] == "pop":
        myList.pop()
