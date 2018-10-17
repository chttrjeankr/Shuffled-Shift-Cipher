import random
import string

from helper_funcs import *


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
    password = [random.choice(choices) for i in range(random.randint(10, 20))]
    return password


def make_key_list(passcode):
    """
    Shuffles a key_list in an organized algorithm to avoid break in via brute force guessing of caeser shift key

    :param passcode: passcode in list format
    :return: a shuffled key list based on the particular passcode
    """

    return string.printable  # (works with zero shuffling)

    # key_list = []
    # key_list_options = list(string.printable)
    #
    # breakpoints = sorted(set(passcode))
    # temp_list = []
    #
    # for i in key_list_options:
    #     temp_list.extend(i)
    #     if i in breakpoints or i == key_list_options[-1]:
    #         key_list.extend(temp_list[::-1])
    #         temp_list = []
    #
    # return key_list


def make_caeser_key(passcode):
    """
    Gets the passcode, processes it and returns a caeser key to implement shift

    :param passcode: gets the passcode
    :return: a positive number which'll serve as a shift key to the caeser cipher algorithm
             returns the length of the passcode if the num to be returned is less than or equal to zero
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

    # reads and loads the plaintext file
    try:
        fi = open(input_file_name, "r+")
        plaintext = fi.read()
        fi.close()
    except FileNotFoundError:
        print("File Not Found")
        return 1

    encoded_message = ""

    # encoding shift like caeser cipher algorithm
    for i in plaintext:
        position = key_list.index(i)
        encoded_message += key_list[(position + caeser_key) % len(key_list)]

    # writes the encoded file to the output file
    fo = open(encoded_output_file_name, "w+")
    fo.write(encoded_message)
    print("Message encoded and stored in {}".format(encoded_output_file_name))
    fo.close()

    return 0


def decoding(encoded_input_file_name, passcode, decoded_output_file_name):
    """
    Does the decoding of the message after reading from encoded_input_file_name
    and writes the decoded_message to decoded_output_file_name

    :param encoded_input_file_name: the file name from where to fetch the encoded message
                                    file must be present in the same directory as of the program
    :param passcode: the passcode generated from the 'passcode_creator()'
    :param decoded_output_file_name: the file name to store the decoded output
    """
    key_list = make_key_list(passcode)
    caeser_key = make_caeser_key(passcode)

    try:
        fi = open(encoded_input_file_name, "r+")
        encoded_message = fi.read()
        fi.close()
    except FileNotFoundError:
        print("File Not Found")
        return 1

    decoded_message = ""

    for i in encoded_message:
        position = key_list.index(i)
        decoded_message += key_list[(position - caeser_key) % -len(key_list)]

    fo = open(decoded_output_file_name, "w+")
    fo.write(decoded_message)
    print("Message decoded and stored in {}".format(decoded_output_file_name))
    fo.close()

    return 0
