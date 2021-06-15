def palindrome(a):
    s = ''
    for i in a[::-1]:
        s = s + i
    if a == s:
        return "true" , s
    else:
        return "false", s
    # return s
print(palindrome("i am ganavi"))
    