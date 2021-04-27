class Trycatch:
    try:
        f= open('test.txt','w+')
        data = f.write("hello it's a text file contains no data")
    except fineNotFoundError as e:
        print(e)
    except Exception as e:
        print(e)
    else:
        print(f.read())
        f.close()
    finally:
        print("finally block")
    
