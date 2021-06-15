def string_match(s1, s2):
    n=''
    if len(s1) == len(s2):
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] not in s2:
                    n = s1[i]
                elif s2[j] not in s1:
                    n = s2[j]
                elif s1 == s2:
                    return " "
    else:
        return "false "
    print(n) 

string_match("coding", "ingcod")



# def string_match(s1, s2):
#     n = ""
#     for i in s1:
#         if i not in s2:
#             n = n + i
#         elif s2 not in i:
#             n = n + s2[i]

    
#     return n

# print(string_match("foobar","barfoot"))

