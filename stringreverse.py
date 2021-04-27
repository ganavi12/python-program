def stringreverse(request):
    a = ""
    # for i in request[-1:-len(request)-1:-1]:
    for i in request[::-1]:
        a = a + i
    print(a)


request = input("enter the string")
stringreverse(request)
