from cipher import *


def main():
    """
    THE MAIN FUNCTION

    Menu driven program to guide the user through the process of encryption and decryption
    :return: nothing
    """
    print("Welcome to Encryption and Decryption Program")
    print("1. Encrypt")
    print("2. Decrypt")
    print("Press Anything Else to EXIT")

    choice = input("Enter choice: ")
    while True:
        if choice == "1":
            input_file_name = input("Enter Input File Name containing message to be encoded: ")
            passcode = passcode_creator()
            print("Your passcode is: {}".format(''.join(passcode)))

            fo = open("latest_passcode.txt", "w+")
            fo.write(''.join(passcode))
            print("Passcode stored in {}".format("latest_passcode.txt"))
            fo.close()

            encoded_output_file_name = input("Enter File Name to store the encoded output: ")
            if (encoding(input_file_name, passcode, encoded_output_file_name) == 0):
                print("Encoding Successful")
                choice = 0
                continue
            else:
                print("Try Again")
                continue

        elif choice == "2":
            encoded_input_file_name = input("Enter Input File Name containing encoded message: ")
            load = input(
                "Want to load passcode from \"latest_passcode.txt\" file?\n Press Y for YES or any other key for NO")
            if load == 'y' or load == 'Y':
                fi = open("latest_passcode.txt", "r+")
                passcode = list(fi.read())
                fi.close()
            else:
                passcode = list(input("Enter passcode to decode: "))
            decoded_output_file_name = input("Enter File Name to store the decoded output: ")
            if (decoding(encoded_input_file_name, passcode, decoded_output_file_name) == 0):
                print("Decoding Successful")
                choice = 0
                continue
            else:
                print("Try Again")
                continue

        else:
            print("Exiting From Program")
            exit(0)


if __name__ == "__main__":
    main()
