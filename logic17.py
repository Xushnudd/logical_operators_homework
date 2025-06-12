def main(a):
    """
    Given a five-digit integer a,  check the following statement "All digits of the number are in ascending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    b = a//10000
    d = (a//1000)%10
    e = (a//100)%100%10
    f = (a//10)%1000%10
    g = a%10000%10
    return b<d<e<f<g
print(main(12345))