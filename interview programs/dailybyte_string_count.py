# def string_count(s):
#     c = []
#     if len(s) > 0:
#         for i in range(len(s)): 
#             if s[i] in s:
#                 c.append(s[i])
#                 if s[i] in c:
#                     c.append(s[i])
#                 else:
#                     c.remove(s[i])
#                 return len(c)
#             else:
#                 return 0
        
# print(string_count("abcd"))


# def string_count(s):
#     c = []
#     if len(s) > 0:
#         for i in range(len(s)):
#             for j in range(i+1,len(s)):
#                 if s[i] == s[j]:
#                     c.append(s[i])
#                 return len(c)
            
        
# print(string_count("abcda"))

s = "abcda"
def string_count(s):
    if len(s) > 0:
        c = 0
        for i in range(len(s)):
            found = s.count(s[i]) 
            if found > 0:
                c = c + 1 
            else: 
                return 0
            return c
print(string_count(s))

            
        