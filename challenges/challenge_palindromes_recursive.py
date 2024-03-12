def is_palindrome_recursive(dd, b_or=0, or_t=None):
    if dd == "":
        return False
    if or_t is None:
        or_t = len(dd) - 1
    if b_or >= or_t:
        return True
    if dd[b_or] != dd[or_t]:
        return False
    return is_palindrome_recursive(dd, b_or + 1, or_t - 1)
