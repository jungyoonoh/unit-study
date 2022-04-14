test_case = int(input())

for i in range(test_case): # 0
    input_num = bin(int(input()))
    input_num_len = len(input_num) # 6
    for j in range(input_num_len-1, 1, -1): # 5, 4, 3, 2
        if (input_num[j] == "1"):
            print(input_num_len-j-1, end=" ")