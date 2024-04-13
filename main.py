




while True:
    print("Menu\n--------------\n1. Encode\n2. Decode\n3. Quit")

    option = int(input("Please enter an option: "))
    if option == 3:
        break



    if option == 1:
        password = input("Please enter your password to encode: ")
        encoded_list = []
        for digit in list(password):
            new_digit = int(digit)+3
            encoded_list.append(new_digit)
       
        print("Your password has been encoded and stored!")

    elif option == 2:
        decoded = []
        for digit in encoded_list:
            decoded_digit = int(digit) - 3
            decoded.append(decoded_digit)
            decoded_str = ''
            encoded_str = ''
            for item in decoded:
                decoded_str += str(item)
            for item in list(encoded_list):
                encoded_str += str(item)
        print("The encoded password is", encoded_str,", and the original password is", decoded_str,".")


