import random
import string

class Shuffled_Shift_Cipher(object):
    """docstring for Shuffled_Shift_Cipher."""

    def __init__(self, passkey=None):
        if passkey == None:
            self.__passcode = self.__passcode_creator()
        else:
            self.__passcode = passkey
        self.__key_list = self.__make_key_list()
        self.__shift_key = self.__make_shift_key()

    def __str__(self):
        return "Passcode is: " + ''.join(self.__passcode)

    def __sum_of_digits(self, num):
        """
        Calculates the sum of all digits in 'num'

        :param num: a positive natural number
        :return: an integer which stores the sum of digits
        """
        sum_ = sum(map(int, str(num)))
        return sum_

    def __make_one_digit(self, digit):
        """
        Implements an algorithm to return a single digit integer
        Doesn't keep the value of input 'digit' intact

        :param digit: takes in a positive number
        :return: the number itself; if its single digit
                    else, converts to single digit and returns
        """
        while digit > 10:
            digit = self.__sum_of_digits(digit)
        return digit

    def __neg_pos(self, iterlist):
        """
        Mutates the list by changing the sign of each other element

        :param iterlist: takes a list iterable
        :return: the mutated list
        """
        for i in range(1,len(iterlist),2):
            iterlist[i] *= -1
        return iterlist

    def __passcode_creator(self):
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

    def __make_key_list(self):
        # key_list_options contain nearly all printable except few elements from string.whitespace
        key_list_options = string.ascii_letters + string.digits + string.punctuation + " \t\n"

        keys_l = []

        # creates points known as breakpoints to break the key_list_options at those points and pivot each substring
        breakpoints = sorted(set(self.__passcode))
        temp_list = []

        # algorithm for creating a new shuffled list, keys_l, out of key_list_options
        for i in key_list_options:
            temp_list.extend(i)

            # checking breakpoints at which to pivot temporary sublist and add it into keys_l
            if i in breakpoints or i == key_list_options[-1]:
                keys_l.extend(temp_list[::-1])
                temp_list = []

        # returning a shuffled keys_l to prevent brute force guessing of shift key
        return keys_l

    def __make_shift_key(self):
        num = sum(self.__neg_pos(list(map(ord, self.__passcode))))
        return num if num > 0 else len(self.__passcode)

    def decrypt(self, encoded_message):
        decoded_message = ""

        # decoding shift like caeser cipher algorithm implementing negative shift or reverse shift or left shift
        for i in encoded_message:
            position = self.__key_list.index(i)
            decoded_message += self.__key_list[(position - self.__shift_key) % -len(self.__key_list)]

        return decoded_message

    def encrypt(self, plaintext):
        encoded_message = ""

        # encoding shift like caeser cipher algorithm implementing positive shift or forward shift or right shift
        for i in plaintext:
            position = self.__key_list.index(i)
            encoded_message += self.__key_list[(position + self.__shift_key) % len(self.__key_list)]

        return encoded_message

if __name__ == "__main__":
    # cip1 = Shuffled_Shift_Cipher('d4usr9TWxw9wMD')
    cip1 = Shuffled_Shift_Cipher()
    cipher = cip1.encrypt("Hello, this is like a modified caeser cipher")
    print(cipher)
    print(cip1)
    print(cip1.decrypt(cipher))
