#!/usr/bin/env python3

from sys import argv
import re
import string
import secrets

def gen_secret(bad_chars=None, length=12):
    """
        Generate a secure random string
        of length specified.

        length = int

        bad_chars = List of characters to remove.
    """
    
    length = int(length)

    chars = string.ascii_letters + string.digits + string.punctuation

    chars = chars.replace('\\', '')

    if bad_chars:
        
        for bad_char in bad_chars:

            chars = chars.replace(bad_char, '')

    the_secret = [secrets.choice(chars) for i in range(length)]

    return ''.join(the_secret)

if __name__ == '__main__':

    try:

        length = argv[1]

    except IndexError:

        length = None
    
    try:

        bad_chars = argv[2]

    except IndexError:

        bad_chars = None

    # TODO: better argument parsing.
    if length and not bad_chars:

        print(gen_secret(length=length))

    elif length and bad_chars:

        print(gen_secret(length=length, bad_chars=bad_chars))

    else:

        print(gen_secret())
