def is_palindrome_number(n: int) -> bool:
    """Return True if n is a palindrome (numeric)."""
    if n < 0:
        return False
    temp = n
    rev_num = 0
    while temp > 0:
        d = temp % 10
        temp //= 10
        rev_num = rev_num * 10 + d
    return n == rev_num


if __name__ == "__main__":
    try:
        n = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input")
    else:
        print("Palindrome" if is_palindrome_number(n) else "Not palindrome")
