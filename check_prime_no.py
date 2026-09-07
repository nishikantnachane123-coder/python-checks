def is_prime(n: int) -> bool:
    """Return True if n is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


if __name__ == "__main__":
    try:
        n = int(input("Enter a number to check: "))
    except ValueError:
        print("Invalid input")
    else:
        print("Prime Number" if is_prime(n) else "Composite Number")
