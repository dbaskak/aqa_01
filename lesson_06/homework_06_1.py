string = input("Enter string, please: ")
unique_chars = len(set(string))
if unique_chars > 10:
    print(True)
else:
    print(False)