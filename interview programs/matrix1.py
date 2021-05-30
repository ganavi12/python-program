 
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
 
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]
 
# result = [[0,0,0],
#         [0,0,0],
#         [0,0,0]]

# for i in range(len(X)):
#     for j in range(len(X[i])):
#         result[i][j] = X[i][j] + Y[i][j]
 
# for r in result:
#     print(r)

result = [[X[i][j] + Y[i][j]  for j in range (len(X[i]))] for i in range(len(X))]
  
for r in result:
    print(r)