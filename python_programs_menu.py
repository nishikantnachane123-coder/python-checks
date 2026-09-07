def is_armstrong(n: int) -> bool:
    if n < 0:
        return False
    temp = n
    digits = 0
    while temp > 0:
        temp //= 10
        digits += 1
    if digits == 0:
        digits = 1
    temp = n
    total = 0
    while temp > 0:
        d = temp % 10
        total += d ** digits
        temp //= 10
    return total == n


def is_prime(n: int) -> bool:
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


def is_palindrome_number(n: int) -> bool:
    if n < 0:
        return False
    temp = n
    rev_num = 0
    while temp > 0:
        d = temp % 10
        temp //= 10
        rev_num = rev_num * 10 + d
    return n == rev_num


def main():
    menu = (
        "Choose an option:\n"
        "1) Check Armstrong number\n"
        "2) Check Prime\n"
        "3) Check Palindrome\n"
        "0) Exit\n"
    )
    while True:
        print(menu)
        choice = input("Enter choice: ").strip()
        if choice == "0":
            break
        if choice not in {"1", "2", "3"}:
            print("Invalid choice")
            continue
        try:
            n = int(input("Enter an integer: "))
        except ValueError:
            print("Invalid integer")
            continue
        if choice == "1":
            print(f"{n} is an Armstrong number." if is_armstrong(n) else f"{n} is not an Armstrong number.")
        elif choice == "2":
            print("Prime Number" if is_prime(n) else "Composite Number")
        elif choice == "3":
            print("Palindrome" if is_palindrome_number(n) else "Not palindrome")


if __name__ == "__main__":
    main()
