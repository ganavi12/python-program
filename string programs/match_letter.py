def match(s1, s2):
    s3 = set()
    for i in s1:
        for j in s2:
            if i == j:
                s3.add(i)
    return s3
print(match("abcdef",'defghia'))
