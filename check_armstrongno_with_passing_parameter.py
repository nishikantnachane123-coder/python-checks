def is_armstrong(n: int) -> bool:
    """Return True if n is an Armstrong number (also called narcissistic)."""
    if n < 0:
        return False
    temp = n
    digits = 0
    while temp > 0:
        temp //= 10
        digits += 1
    if digits == 0:
        digits = 1  # handle n == 0
    temp = n
    total = 0
    while temp > 0:
        d = temp % 10
        total += d ** digits
        temp //= 10
    return total == n


if __name__ == "__main__":
    try:
        n = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input")
    else:
        print(f"{n} is an Armstrong number." if is_armstrong(n) else f"{n} is not an Armstrong number.")
