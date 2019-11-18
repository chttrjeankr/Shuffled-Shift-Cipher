from cipher import *


def main():
    """
    THE MAIN FUNCTION

    Menu driven program to guide the user through the process of encryption and decryption
    :return: nothing
    """
    print("Welcome to Encryption and Decryption Program")
    print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
    print("1. Encrypt")
    print("2. Decrypt")
    print("Press Anything Else to EXIT")
    print("*_*_*_*_*_*_*_*_*_*_*_*_*_*")

    choice = input("Enter choice: ")
    print()
    while True:
        if choice == "1":
            input_file_name = input(
                "Enter Input File Name containing message to be encoded: "
            )

            passcode = passcode_creator()  # creates the passcode used for encryption

            print("_____________________________________________________")
            print("Your passcode is: {}".format("".join(passcode)))

            cwd = os.getcwd()
            latest_passcode_file = os.path.join(
                cwd, "test_text_files", "latest_passcode.txt"
            )

            try:
                fo = open(latest_passcode_file, "w+")
                fo.write(
                    "".join(passcode)
                )  # stores the passcode to a separate latest_passcode_file for reuse

                print("Passcode successfully stored in {}".format(latest_passcode_file))
                print("_____________________________________________________")

                fo.close()
            except:
                print(
                    "FILE ERROR ::: (make sure test_text_files contain latest_passcode.txt)"
                )
                choice = 0
                continue

            print()

            encoded_output_file_name = input(
                "Enter File Name to store the encoded output: "
            )

            # checks if encoding() returns success code or not
            if encoding(input_file_name, passcode, encoded_output_file_name) == 0:
                print()
                print("Encoding... Successful")
                choice = 0  # if successful, takes steps to exit from program
                continue
            else:
                print(
                    "Try Again"
                )  # if error occurred, let the user try 1.Encryption option again
                continue

        elif choice == "2":
            encoded_input_file_name = input(
                "Enter Input File Name containing encoded message: "
            )

            cwd = os.getcwd()
            latest_passcode_file = os.path.join(
                cwd, "test_text_files", "latest_passcode.txt"
            )

            print("________________________________________________________")

            print("Want to load passcode from {} file?".format(latest_passcode_file))
            print()
            load = input("Press Y for YES or any other key for NO: ")

            print("________________________________________________________")

            if load == "y" or load == "Y":
                cwd = os.getcwd()
                latest_passcode_file = os.path.join(
                    cwd, "test_text_files", "latest_passcode.txt"
                )
                try:
                    fi = open(latest_passcode_file, "r+")
                    passcode = list(
                        fi.read()
                    )  # loads the latest passcode used as stored in file by encoding()
                    print("Password loaded successfully")
                    fi.close()
                except:
                    print(
                        "FILE ERROR ::: (make sure test_text_files contain latest_passcode.txt)"
                    )
                    choice = 0
                    continue
            else:
                passcode = list(
                    input("Enter passcode to decode: ")
                )  # lets the user enter the passcode

            print()

            decoded_output_file_name = input(
                "Enter File Name to store the decoded output: "
            )

            # checks if decoding() returns success code or not
            if (
                decoding(encoded_input_file_name, passcode, decoded_output_file_name)
                == 0
            ):
                print("Decoding Successful")
                choice = 0  # if successful, takes steps to exit from program
                continue
            else:
                print(
                    "Try Again"
                )  # if error occurred, let the user try 2.Decryption option again
                continue

        else:
            print()
            print("EXITING FROM PROGRAM")
            print("author: Ankur Chattopadhay, GCETTB CSE")
            exit(0)


if __name__ == "__main__":
    main()
