print("Hello, World!")

user_input = int(input("Choose your language: Press 1 for English, press 2 for Turkish"))
print(type(user_input))

if user_input == "1":
    print("Hello, World!")
elif user_input == "2":
    print("Merhaba, Dünya!")
else:
    print("Wrong input!")
