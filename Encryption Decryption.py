import random
import string


def passcode_creator():
    """
    Creates a random password from the selection buffer of
    1. uppercase letters of the English alphabet
    2. lowercase letters of the English alphabet
    3. digits from 0 to 9

    :rtype: list
    :return: a password of a random length between 10 to 20
    """
    choices = string.ascii_letters + string.digits
    password = [random.choice(choices) for i in range(random.randint(10,20))]
    return password


def sum_of_digits(num):
    """
    Calculates the sum of all digits in 'num'

    :param num: a positive number
    :return: an integer which stores the sum of digits
    """
    sum_ = 0
    while num > 0:
        sum_ += num % 10
        num //= 10
    return sum_


def make_one_digit(digit):
    """
    Implements an algorithm to return a single digit integer
    Doesn't keep the value of input 'digit' intact

    :param digit: takes in a positive number
    :return: the number itself; if its single digit
                else, converts to single digit and returns
    """
    while digit > 10:
        digit = sum_of_digits(digit)
    return digit


def step_creator(passcode):
    """

    :param passcode: takes a string
    :return:
    """
    steps = 0
    for i in passcode:
        steps += ord(i)
    steps = make_one_digit(steps)
    return len(passcode) if steps == 1 else steps


def make_key_list(passcode):
    """
    Shuffles a key_list in an organized algorithm to avoid break in via brute force guessing of caeser shift key

    :param passcode: passcode in list format
    :return: a shuffled key list based on the particular passcode
    """
    key_list = []
    steps = step_creator(passcode)
    key_list_options = list(string.printable)
    # key_list = key_list_options
    # key_list will be made by using itertools on key_list_options
    pass
    return key_list


def neg_pos(iterlist):
    for i in range(len(iterlist)):
        iterlist[i] = iterlist[i] if i % 2 == 0 else -iterlist[i]
    return iterlist


def make_caeser_key(passcode):
    """

    :param passcode: gets the passcode
    :return: a number which'll serve as a shift key to the caeser cipher algorithm
    """
    num = sum(neg_pos(list(map(ord, passcode))))
    return num if num > 0 else len(passcode)


def encoding(input_file_name, passcode, encoded_output_file_name):
    """
    Does the encoding of the message after reading from input_file_name
    and writes the encoded_message to encoded_output_file_name

    :param input_file_name: the file name from where to fetch the message to encode
                            file must be present in the same directory as of the program
    :param passcode: the passcode generated from the 'passcode_creator()'
    :param encoded_output_file_name: the file name to store the encoded output
    """

    # creates a shuffled key_list to implement caeser cipher shift
    key_list = make_key_list(passcode)

    # creates the caeser_key (shift key) for encoding the plaintext
    caeser_key = make_caeser_key(passcode)

    #reads and loads the plaintext file
    fi = open(input_file_name, "r+")
    plaintext = fi.read()
    fi.close()

    encoded_message = ""

    # encoding shift like caeser cipher algorithm
    for i in plaintext:
        position = key_list.index(i)
        encoded_message += key_list[(position + caeser_key) % len(key_list)]

    #writes the encoded file to the output file
    fo = open(encoded_output_file_name, "w+")
    fo.write(encoded_message)
    print("Message encoded and stored in {}".format(encoded_output_file_name))
    fo.close()

    return


def decoding(encoded_input_file_name, passcode, decoded_output_file_name):
    """

    :param encoded_input_file_name:
    :param passcode:
    :param decoded_output_file_name:
    :return:
    """
    key_list = make_key_list(passcode)
    caeser_key = make_caeser_key(passcode)

    fi = open(encoded_input_file_name, "r+")
    encoded_message = fi.read()
    fi.close()

    decoded_message = ""

    for i in encoded_message:
        position = key_list.index(i)
        decoded_message += key_list[(position - caeser_key) % -len(key_list)]

    fo = open(decoded_output_file_name, "w+")
    fo.write(decoded_message)
    print("Message decoded and stored in {}".format(decoded_output_file_name))
    fo.close()

    return


def main():
    print("Welcome to Encryption and Decryption Program")
    print("1. Encrypt")
    print("2. Decrypt")
    print("Press Anything Else to EXIT")

    choice = input("Enter choice: ")

    if choice == 1:
        input_file_name = input("Enter Input File Name containing message to be encoded: ")
        passcode = passcode_creator()
        print("Your passcode is: {}".format(''.join(passcode)))
        encoded_output_file_name = input("Enter File Name to store the encoded output: ")
        encoding(input_file_name, passcode, encoded_output_file_name)

    elif choice == 2:
        encoded_input_file_name = input("Enter Input File Name containing encoded message: ")
        passcode = list(input("Enter passcode to decode: "))
        decoded_output_file_name = input("Enter File Name to store the decoded output: ")
        decoding(encoded_input_file_name, passcode, decoded_output_file_name)

    else:
        print("Exiting From Program")
        exit(0)


main()
