def div(m,n):
    print("inside div")
    return m/n
def smart_div(func):
    print("inside smart div func")
    def inner(m,n):
        print("inside inner")
        if m<n:
            m,n = n,m
            print(m,n,"val")
        return func(m,n)
    return inner
div = smart_div(div)
print(div(4,2))
