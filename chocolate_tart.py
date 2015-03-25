#!/usr/bin/python3
from bcrypt import hashpw
from functools import reduce

def chocolate_tart(function):
    return reduce(lambda x, y: x + y, hashpw(str(function(I♥🎂)).encode(), b'$2a$18$4ROvoeW/IRnERuiotwaF9O'))


if __name__ == '__main__':
    print(chocolate_tart(lambda x: x**2 - 6875))
