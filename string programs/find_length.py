# print(len('hello world !'))
def len_str(s):
    c = 0
    for i in s:
        c += 1
    return c

print(len_str('hello world !'))