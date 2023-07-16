def getdigits(n, stack=None):
    if stack is None:
        stack = []
    divisor = 10**len(stack)
    next_digit = (n % (divisor * 10)) / divisor
    stack.insert(0, next_digit)
    n = n - next_digit * divisor
    if divisor > n:
        return stack
    return getdigits(n, stack)

print getdigits(1234567)
