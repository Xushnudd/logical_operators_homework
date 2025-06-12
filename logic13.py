def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is even".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    b = a//10
    d = a%10
    c = b+d
    c = c%2
    return c==0
print(main(92))