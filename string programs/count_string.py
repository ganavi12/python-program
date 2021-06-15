# from collections import Counter


# def count_str(s):
#     spt_str = s.split()
#     print(s)
#     print(spt_str)
#     return Counter(spt_str)

# print(count_str("Gfg is best . Geeks are good and Geeks like Gfg"))



def count_str(s):
    spt_str = s.split()
    # print(s)
    c = 0
    dec = {}
    for i in range(len(spt_str)):
        for j in range(i+1,len(spt_str)):
            if spt_str[i] == spt_str[j]:
                if spt_str[i] not in dec:
                    c = c + 1
                    dec[spt_str[i]] = c     
    return dec


print(count_str("Gfg is best . Geeks are good and Geeks like Gfg"))

