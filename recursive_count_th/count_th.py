'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    char_length = 2  # the lenght of 'th'
    if len(word) < char_length:
        return 0
    if word[0: char_length] == "th":
        return 1 + count_th(word[char_length - 1:])
    else:
        return count_th(word[char_length - 1:])
