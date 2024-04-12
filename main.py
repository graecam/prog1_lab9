




while True:
    print("Menu\n--------------\n1. Encode\n2. Decode\n3. Quit")

    option = int(input("Please enter an option: "))
    if option == 3:
        break



    if option == 1:
        password = input("Please enter your password to encode: ")
        encoded_list = ''
        for digit in list(password):
            new_digit = int(digit)+3
            encoded_list  += str(new_digit)
       
        print("Your password has been encoded and stored!")

    elif option == 2:
        pass

