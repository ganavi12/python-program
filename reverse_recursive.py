def rec_string(a, b):
    if a <= len(b)-1:
        rec_string(a+1, b)
        print(b[a], end=' ')


rec_string(0, 'ganavi')
