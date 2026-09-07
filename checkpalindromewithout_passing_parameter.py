def palindrome_no_input():
    """Prompt user and print whether the entered number is a palindrome."""
    try:
        n = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input")
        return
    temp = n
    rev_num = 0
    while temp > 0:
        d = temp % 10
        temp //= 10
        rev_num = rev_num * 10 + d
    print(f"Reversed number: {rev_num}")
    if n == rev_num:
        print("Palindrome number")
    else:
        print("Not Palindrome number")


if __name__ == "__main__":
    palindrome_no_input()
