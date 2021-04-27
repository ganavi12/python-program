'''with open('write.txt','w') as w:
    w.write("this is first line of text \nthis is second line of file \n")
    w.write("this is third line of file ")'''

'''with open('write.txt','r') as f:
    f.seek(10)
    print(f.readline())
    print(f.tell())'''

'''with open('write.txt','r') as r:
    with open('write_copy.txt','w+') as w:
        for i in r:
            w.write(i)'''

with open('image.png','rb') as r:
    with open('image_copy.png','wb') as w:
        for i in r:
            w.write(i)
