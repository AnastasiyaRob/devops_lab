# Check whether the input string is palindrome
a = input("Input string")
if a == a[::-1]:
    print("yes")
else:
    print("no")
