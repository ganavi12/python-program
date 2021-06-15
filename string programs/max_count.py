
# test_str = "GeeksforGeeks"
# all_freq = {}
# for i in test_str:
#     if i in all_freq:
#         all_freq[i] += 1
#     else:
#         all_freq[i] = 1
# res = max(all_freq, key=all_freq.get)
# print(res)


def print_sum(arr, n):
    l = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == n:
                l.append((arr[i], arr[j]))
    return l

arr = [1, 5, 7, -1, 5]
print(print_sum(arr,6))



