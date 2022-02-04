# dynamic programing
# divide the problem into sub problems
# find the sum can generate with the minimum subsets
# use non recursive bottom-up approch
def subset_sum(set_data, sum):
    
    if len(set_data) < 1 or sum < 1:
        return False
    
    amount = sum + 1
    final_list = []
    for i in range(len(set_data)):
        temp = []
        for j in range(amount):
            if j == 0:
                temp.append(1)
                continue
            
            if i == 0:
                if set_data[i] == j:
                   res = 1
                else:
                   res = 0 
                
                temp.append(res) 
                continue
     
            if j < set_data[i]:
                temp.append(final_list[i-1][j])
                continue
            

            if final_list[i-1][j] == 0:
                temp.append(final_list[i-1][j - set_data[i]])
            else:
                temp.append(final_list[i-1][j])
            
        final_list.append(temp)

    return final_list[len(set_data)-1][sum]


if __name__ == "__main__":
    set_a = [2, 3, 5, 7, 10]
    sum = 14
    result = subset_sum(set_a, sum)
    print(result == 1)