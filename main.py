#Melvyn Rodriguez
def encode(password):
    result = ""
    password = str(password)
    for digit in password:
        digit = (int(digit) + 3) % 10
        result = result + str(digit)
    return result

def decode(encoded_pass):

    decoded_pass = ""

    for char in encoded_pass:
        if int(char) > 2:
            decoded_pass += str(int(char)-3)

        if int(char) <= 2:
            decoded_pass += str(int(char)-3 + 10)

    return decoded_pass


def print_menu():
    print("\nMenu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def main():
    password = ""
    encoded_password = ""

    while True:
        print_menu()
        menu_choice = input("\nPlease enter an option: ")
        if menu_choice == "1":
            entered = input("Please enter your password to encode: ")
            password = password + str(entered)
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif menu_choice == "2":
            print(f"The encoded password is: {encode(password)}, and the original password is {decode(encoded_password)}.")
            password = ""
            encoded_password = ""
        else:
            print("Exiting Password Editor")
            break


if __name__ == '__main__':
    main()


#confirmed code is working 03.19.2024 at 2pm