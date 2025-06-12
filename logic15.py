def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    b = a//100
    d = (a//10)%10
    c = a%10
    e = b+d+c
    return e%2 == 0
print(main(224))