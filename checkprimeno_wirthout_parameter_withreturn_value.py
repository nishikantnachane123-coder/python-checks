def check_prime_no_input() -> bool:
    """Prompt user for a number and return True if prime else False."""
    try:
        n = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input")
        return False
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
    print(check_prime_no_input())
