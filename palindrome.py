def is_palindrome(n):
    
    str_n = str(n)
    
    if str_n == str_n[::-1]:
        return True
    else:
        return False


number = int(input())


if is_palindrome(number):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
