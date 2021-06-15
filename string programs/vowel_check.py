def vowel_check(s):
    for i in range(len(s)):
        if s[i] in 'aeiou':
            return "accepted"
        elif s[i] in 'AEIOU':
            return "accepted"
        else:
            return "not accepted"

print(vowel_check("geeksforgeeks"))

print(vowel_check("ABeeIghiObhkUul"))