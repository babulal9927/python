def is_palindrome(x):
    
    num_str = str(x)

    
    return num_str == num_str[::-1]


x = -121
print(is_palindrome(x))  
