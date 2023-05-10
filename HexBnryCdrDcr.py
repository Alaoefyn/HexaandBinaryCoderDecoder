def hex_to_string(hex_input):
    return bytes.fromhex(hex_input).decode('utf-8')

def binary_to_string(binary_input):
    return ''.join(chr(int(binary_input[i:i+8], 2)) for i in range(0, len(binary_input), 8))

def string_to_hex(string_input):
    return ''.join(hex(ord(c))[2:] for c in string_input)

def string_to_binary(string_input):
    return ''.join(format(ord(c), '08b') for c in string_input)

def main():
    while True:
        user_input = input("Enter 'h' for Hexadecimal input, 'b' for Binary input and 's' for String input: ")
        if user_input.lower() == 'h':
            hex_input = input("Enter Hexadecimal Input: ")
            print("Decoded String: ", hex_to_string(hex_input))
        elif user_input.lower() == 'b':
            binary_input = input("Enter Binary Input: ")
            print("Decoded String: ", binary_to_string(binary_input))
        elif user_input.lower() == 's':
            string_input = input("Enter String Input: ")
            sub_input = input("Enter 'h' for Hexadecimal value, 'b' for Binary Output: ")
            if sub_input.lower() == 'h':
                print("Hexadecimal Output: ", string_to_hex(string_input))
            elif sub_input.lower() == 'b':
                print("Binary Output: ", string_to_binary(string_input))
        else:
            print("Invalid Input!")
        cont = input("Do you want to continue to code decode? (Y for YES,N for NO)(Y/N): ")
        if cont.lower() == 'n':
            break

if __name__ == '__main__':
    main()
