import random
import string

key_list = string.printable


def decoding(encoded_message):
    decoded_message = ""
    for i in encoded_message:
        position = key_list.index(i)
        decoded_message += key_list[(position - caeser_key) % -len(key_list)]
    return decoded_message


def encoding(plaintext):
    encoded_message = ""
    for i in plaintext:
        position = key_list.index(i)
        encoded_message += key_list[(position + caeser_key) % len(key_list)]
    return encoded_message


if __name__ == "__main__":
    fo = open("enc_dec_unit_test_result.txt", "a")
    for i in range(1000):
        plaintext = string.printable
        caeser_key = random.randint(10, 500)
        ciphertext = encoding(plaintext)
        decodedtext = decoding(ciphertext)
        if decodedtext != plaintext:
            fo.write(decodedtext == plaintext + str(caeser_key) + "\n")
        fo.close()
    print("DONE")
