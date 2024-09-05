while True:
    word = input("Enter any word containing letter 'h' (both lower and upper case): ")
    if 'h' in word.lower():
        print("Tnaks!")
        break
    else:
        print("Please try again!")