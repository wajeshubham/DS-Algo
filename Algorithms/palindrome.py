"""for number/integer"""


def is_palindrome(num):
    new_num = 0
    og_num = num
    while num > 0:
        new_num = new_num * 10 + num % 10
        num = num // 10

    if new_num == og_num:
        return True
    return False


"""for strings"""


def is_palindrome_str(string):
    new_str = ""
    for i in range(len(string) - 1, -1, -1):
        new_str += string[i]
    if new_str == string:
        return True
    return False


"""for sentences"""


def is_palindrome_sent(sent):
    lst = sent.split(" ")
    new_sent = ""
    for i in range(len(lst) - 1, -1, -1):
        if i == len(lst) - 1:
            new_sent += lst[i]
        else:
            new_sent += " " + lst[i]

    if new_sent == sent:
        return True
    return False
