import random

nums_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
letters_list_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
                      "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                      "S", "T", "U", "V", "W", "X", "Y", "Z"]
letters_list_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
                      "j", "k", "l", "m", "n", "o", "p", "q", "r",
                      "s", "t", "u", "v", "w", "x", "y", "z"]
special_char_list = ["!", "@", "#", "$", "%", "&", "*", "/", "+", "=", "-", "~", "?"]
selected_chars = []



def password_params():
    password_length = input("How many characters would you like your password to be? ")
    password_length = int(password_length)

    password_nums = input("Would you like numbers in your password? y/n ")
    if password_nums == "y":
        selected_chars.extend(nums_list)

    password_upper = input("Would you like uppercase letters in your password? y/n ")
    if password_upper == "y":
        selected_chars.extend(letters_list_upper)

    password_lower = input("Would you like lowercase letters in your password? y/n ")
    if password_lower == "y":
        selected_chars.extend(letters_list_lower)

    password_special = input("Would you like special characters in your password? y/n ")
    if password_special == "y":
        selected_chars.extend(special_char_list)

    return password_length


final_length = password_params()



def generate_password(num):
    user_password = ""
    count = 0
    while count < num:
        count += 1
        random_num = random.randint(0, len(selected_chars))
        user_password += selected_chars[random_num]

    print(f"Your password is: {user_password}")


generate_password(final_length)











