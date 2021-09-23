str1 = "apple"
str2 = "oppa"

# 对字符串进行初始化，最前面加上一个相同的字符，方便后面矩阵初始化
str1 = "#" + str1
str2 = "#" + str2

# 构建一个len(str1) * len(str2)的矩阵
dp = [[0 for i in range(len(str2))] for i in range(len(str1))]

# 对矩阵进行初始化
for i in range(len(str1)):
    dp[i][0] = i
for j in range(len(str2)):
    dp[0][j] = j

# 开始推导，遍历矩阵
for i in range(1,len(str1)):
    for j in range(1,len(str2)):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min([dp[i-1][j], dp[i][j-1], dp[i-1][j-1]]) + 1

# 输出最小编辑距离
print(dp[len(str1)-1][len(str2)-1])