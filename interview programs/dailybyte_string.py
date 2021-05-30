def string_check(s1,s2):
    if len(s1) == len(s2):
        for i in s1:
            for j in s2:
                if i in s2 or j in s1:
                    return True
                else:
                    return False
    else:
        return False

print(string_check("program","function"))