def substring(s1, s2):
    if s1.find(s2) < 0:
        return "no"
    return "yes"

print(substring("geeks for geeks", "for"))
print(substring("geeks for geeks","ganavi"))
    