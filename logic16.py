def main(a):
    """
    Given integer a,  check the following statement "The integer is a five-digit number".
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
    all = b+d+e+f+g
    all = all%2
    return all==0
print(main(12346))