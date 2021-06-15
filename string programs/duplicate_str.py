def duplicate(s):
    s1 = []
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] != s[j]:
                if s[i] not in s:
                # print(s[i],s[j])
                # s1 = s1 + s[i]
                    s1.remove(s[j])
                else:
                    s1.append(s[j])

    return s1

print(duplicate("geeksforgeeks"))
    

            