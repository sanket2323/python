def is_palindrome(cs):
    if cs == '':
        return True

    return cs[-1] == cs[0] and is_palindrome(cs[1:-1])

print(is_palindrome('20'))