case = input("Enter any letter: ")
if case.isupper():
    print("The letter is in uppercase.")
elif case.islower():
    print("The letter is in lowercase.")
else:
    print("The letter is neither uppercase nor lowercase.")