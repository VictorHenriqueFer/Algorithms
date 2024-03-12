def is_palindrome_iterative(mud):
    if not mud:
        return False
    fx = len(mud)
    js = fx // 2
    for mo in range(0, js):
        if mud[mo] != mud[fx - 1 - mo]:
            return False
    return True
