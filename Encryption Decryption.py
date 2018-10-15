import string
import math
import random
import itertools


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
    key_list = []
    steps = step_creator(passcode)
    key_list_options = list(string.printable)
    # key_list = key_list_options
    # key_list will be made by using itertools on key_list_options
    pass
    return key_list


def make_caeser_key(passcode):
    pass
    num = 0
    # return a number that will be the shift key
    return num


def encoding(input_file_name, passcode, encoded_output_file_name):
    """
    Does the encoding of the message after reading from input_file_name
    and writes the encoded_message to encoded_output_file_name

    :param input_file_name: the file name from where to fetch the message to encode
                            file must be present in the same directory as of the program
    :param passcode: the passcode generated from the 'passcode_creator()'
    :param encoded_output_file_name: the file name to store the encoded output
    """
    key_list = make_key_list(passcode)
    caeser_key = make_caeser_key(passcode)

    fi = open(input_file_name, "r+")
    input_message = fi.read()
    fi.close()

    encoded_message = ""

    for i in input_message:
        position = key_list.index(i)
        encoded_message += key_list[(position + caeser_key) % len(key_list)]

    fo = open(encoded_output_file_name, "w+")
    fo.write(encoded_message)
    print("Message encoded and stored in {}".format(encoded_output_file_name))
    fo.close()


def decoding(encoded_input_file_name, passcode, decoded_output_file_name):
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
