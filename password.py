password = input('Enter your password : ')
min_len = 8
min_digit = 2
min_alpha = 2
min_special = 2

dig_count = 0
alpha_count = 0
special_count = 0

if len(password) >= min_len:
    for char in password:
        if char.isdigit():
            dig_count = dig_count + 1
        elif char.isalpha():
            alpha_count = alpha_count + 1
        else:
            special_count = special_count + 1
    if dig_count >= min_digit and alpha_count >= min_alpha and special_count >= min_special:
        print("password is strong")
else:
 print("Password is not strong")
