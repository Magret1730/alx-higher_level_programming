#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    copy_str = str[:n] + str[n+1:]
    return copy_str
