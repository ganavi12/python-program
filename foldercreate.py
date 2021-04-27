# import os
# dirName = 'tempDir'


# def cerateFolder():
#     try:
#         # Create target Directory

#         os.mkdir(dirName)
#         print("Directory ", dirName,  " Created ")

#     except FileExistsError:
#         print("Directory ", dirName,  " already exists")


# def cerateFile():
#     for i in range(11):
#         with open('D:\\python\\python\\'+str(i)+".txt", "w+") as f:
#             f.write("test")


# if __name__ == '__main__':
#     cerateFolder()
#     cerateFile()


# t = ('holberton', [1, 2, 3])
# t[1][0] = 10
# print(t)


nums = [4, 8, 5, 2, 1]
print(sorted(nums))
# sorted_nums = sorted(nums)
# print(sorted_nums)
print(nums)


nums.sort()
print(nums)
