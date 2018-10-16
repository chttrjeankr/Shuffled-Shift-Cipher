from cipher import *


def main():
    print("Welcome to Encryption and Decryption Program")
    print("1. Encrypt")
    print("2. Decrypt")
    print("Press Anything Else to EXIT")

    choice = input("Enter choice: ")

    if choice == "1":
        input_file_name = input("Enter Input File Name containing message to be encoded: ")
        passcode = passcode_creator()
        print("Your passcode is: {}".format(''.join(passcode)))
        encoded_output_file_name = input("Enter File Name to store the encoded output: ")
        encoding(input_file_name, passcode, encoded_output_file_name)

    elif choice == "2":
        encoded_input_file_name = input("Enter Input File Name containing encoded message: ")
        passcode = list(input("Enter passcode to decode: "))
        decoded_output_file_name = input("Enter File Name to store the decoded output: ")
        decoding(encoded_input_file_name, passcode, decoded_output_file_name)

    else:
        print("Exiting From Program")
        exit(0)

    return
