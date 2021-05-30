def sum(a, n):
    if len(a)>0: 
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if a[i] + a[j] == n:
                    # res.append((a[i]+a[j]))
                    return True 
                else: 
                    return False
a = [1, 3, 8, 2]
n = 8
print(sum(a,n))  